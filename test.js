import http from 'k6/http';

export let options = {
    stages: [

        { duration: "10s", target: 5 },

        { duration: "10s", target: 5 },

        { duration: "10s", target: 7 },

        { duration: "10s", target: 7 },

        { duration: "10s", target: 12 },

        { duration: "10s", target: 12 },

        { duration: "10s", target: 7 },

        { duration: "10s", target: 7 },

        { duration: "10s", target: 5 },

        { duration: "10s", target: 5 },

        { duration: "10s", target: 0 }
    ]
};

export default function () {
  const response = http.get("https://test-api.k6.io/");
};
