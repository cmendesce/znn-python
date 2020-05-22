import http from 'k6/http';

export let options = {
    stages: [

        { duration: "3s", target: 5 },

        { duration: "6s", target: 5 },

        { duration: "1s", target: 7 },

        { duration: "6s", target: 7 },

        { duration: "1s", target: 9 },

        { duration: "6s", target: 9 },

        { duration: "1s", target: 7 },

        { duration: "6s", target: 7 },

        { duration: "1s", target: 5 },

        { duration: "6s", target: 5 },

        { duration: "1s", target: 0 }
    ]
};

export default function () {
  const response = http.get("https://test-api.k6.io/");
};
