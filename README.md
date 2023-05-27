# werkzeug's ProxyMiddleware with Flask
Quick example how to use ProxyMiddleware with Flask Apps

## Introduction
The purpose of this project is to present how to call different API versions
using same host address.

It contains two Flask applications:
* one with `/v1/hello` endpoint - `app_v1.py`
* the other with `/v2/hello` endpoint - `app_v2.py`

What we want to achieve is when we call these enpoints, the Middleware
application will redirect our request to appriopriate Flask application.

### Prerequisities
* python3.10
* docker
* docker compose

### app_v1.py and app_v2.py
Simple flask applications with one endpoint `/hello`.

### app_middleware.py
Middleware layer - groups up our applications and redirects requests to them.

## How to run
### Manually
Install requirements:
```shell
pip install -r requirements.txt
```
or for running tests:
```shell
pip install -r requirements.txt -r requirements-test.txt
```
Run applications:
```shell
python app_v1.py
python app_v1.py
python app_middleware.py
```
Then run in browser:
* `http://127.0.0.1:5555/v1/hello` - returns `{"msg":"Hello from app v1"}`
* `http://127.0.0.1:5555/v2/hello` - returns `{"msg":"Hello from app v2"}`

If you run this manually you can also check:
* `http://127.0.0.1:5000/v1/hello`
* `http://127.0.0.1:5001/v2/hello`

Remember to check if ports 5000, 5001 and 5555 are available.

### Docker compose
Build images and run compose:
```shell
docker compose build
docker compose up -d
```
Now you can run in browser:
* `http://127.0.0.1:5555/v1/hello` - returns `{"msg":"Hello from app v1"}`
* `http://127.0.0.1:5555/v2/hello` - returns `{"msg":"Hello from app v2"}`

In this case check if 5555 port is available, as app_v1 and app_v2 are not
available outside the docker compose.

## More info
[Werkzeug's Basic HTTP Proxy](https://werkzeug.palletsprojects.com/en/latest/middleware/http_proxy/)