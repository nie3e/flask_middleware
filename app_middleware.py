from werkzeug.middleware.http_proxy import ProxyMiddleware
from werkzeug.serving import run_simple
from app_v1 import app

app = ProxyMiddleware(app, {
    "/v1/": {
        "target": "http://127.0.0.1:5000/v1/"
    },
    "/v2/": {
        "target": "http://127.0.0.1:5001/v2/"
    }
})

if __name__ == "__main__":
    run_simple("0.0.0.0", 5555, app, use_debugger=True)
