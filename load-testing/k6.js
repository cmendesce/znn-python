import http from "k6/http";
import { check } from "k6";

export let options = {
    stages: [

        { duration: "30s", target: 50 },

        { duration: "60s", target: 50 },

        { duration: "10s", target: 70 },

        { duration: "60s", target: 70 },

        { duration: "10s", target: 90 },

        { duration: "60s", target: 90 },

        { duration: "10s", target: 70 },

        { duration: "60s", target: 70 },

        { duration: "10s", target: 50 },

        { duration: "60s", target: 50 },

        { duration: "10s", target: 0 }
    ]
};

export default function() {
    let res = http.get("http://nginx-ingress.default.svc/news.php");
    check(res, { "status is 200": (r) => r.status === 200 });
}
