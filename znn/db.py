import os
import pymysql
from pymysql import cursors

def find_random_news():
    try:
        connection = pymysql.connect(host=os.getenv('DB_HOST', 'localhost'),
                             user=os.getenv('DB_USER', 'root'),
                             password=os.getenv('DB_PASS', 'root'),
                             db=os.getenv('DB_NAME', 'znn'),
                             charset='utf8mb4',
                             cursorclass=cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = """SELECT 
                        n.news_id, 
                        n.news_title, 
                        n.news_text, 
                        i.img_res 
                    FROM news n 
                    JOIN img i ON i.news_id = n.news_id 
                    ORDER BY RAND() LIMIT 1;"""

            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    finally:
        if connection:
            connection.close()

def count_news():
    try:
        connection = pymysql.connect(host=os.getenv('DB_HOST', 'localhost'),
                             user=os.getenv('DB_USER', 'root'),
                             password=os.getenv('DB_PASS', 'root'),
                             db=os.getenv('DB_NAME', 'znn'),
                             charset='utf8mb4',
                             cursorclass=cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = 'SELECT COUNT(1) FROM news;'
            cursor.execute(sql)
            result = cursor.fetchone()
            return True
    finally:
        if connection:
            connection.close()
