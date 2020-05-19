import http from "k6/http";
import { check } from "k6";

export let options = {
    stages: [

        { duration: "30s", target: 500 },

        { duration: "60s", target: 500 },

        { duration: "10s", target: 700 },

        { duration: "60s", target: 700 },

        { duration: "10s", target: 900 },

        { duration: "60s", target: 900 },

        { duration: "10s", target: 700 },

        { duration: "60s", target: 700 },

        { duration: "10s", target: 500 },

        { duration: "60s", target: 500 },

        { duration: "10s", target: 0 }
    ]
};

export default function() {
    let res = http.get("http://nginx-ingress.default.svc/news");
    check(res, { "status is 200": (r) => r.status === 200 });
}
