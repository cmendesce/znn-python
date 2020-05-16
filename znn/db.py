import os
import mysql.connector

db = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASS', 'root'),
    database=os.getenv('DB_NAME', 'znn'),
)

def find_random_news():
    cursor = db.cursor() 
    news_query = 'SELECT news_id, news_title, news_text, news_img_cnt FROM news ORDER BY RAND() LIMIT 1;'
    cursor.execute(news_query)
    results = cursor.fetchall()
    news = {
        'id': results[0][0],
        'title': results[0][1],
        'text': results[0][2]
    }
    cursor.close()

    image_query = f'SELECT img_id, img_res FROM img WHERE news_id = {news["id"]} ORDER BY img_id;'
    cursor = db.cursor()
    cursor.execute(image_query)
    results = cursor.fetchall()
    news['image_path'] = results[0][1]
    cursor.close()

    return news


def count_news():
    cursor = db.cursor() 
    query = 'SELECT COUNT(1) FROM news;'
    cursor.execute(query)
    results = cursor.fetchall()
    return True