import http from 'k6/http';

export let options = {
    stages: [

        { duration: "20s", target: 10 },

        { duration: "20s", target: 10 },

        { duration: "20s", target: 20 },

        { duration: "20s", target: 20 },

        { duration: "20s", target: 40 },
        
        { duration: "20s", target: 40 },

        { duration: "20s", target: 40 },

        { duration: "20s", target: 20 },

        { duration: "20s", target: 20 },

        { duration: "20s", target: 10 },

        { duration: "20s", target: 10 },

        { duration: "20s", target: 0 }
    ]
};

export default function () {
  const response = http.get("http://znn:5000/news");
};
