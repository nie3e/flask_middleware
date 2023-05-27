from werkzeug.middleware.http_proxy import ProxyMiddleware
from werkzeug.serving import run_simple
from flask import Flask
import os

api_v1 = "api_v1" if os.getenv("PLATFORM", None) == "DOCKER" else "localhost"
api_v2 = "api_v2" if os.getenv("PLATFORM", None) == "DOCKER" else "localhost"

app = ProxyMiddleware(Flask(__name__), {
    "/v1/": {
        "target": f"http://{api_v1}:5000/v1/"
    },
    "/v2/": {
        "target": f"http://{api_v2}:5001/v2/"
    }
})

if __name__ == "__main__":
    run_simple("0.0.0.0", 5555, app, use_debugger=True)
