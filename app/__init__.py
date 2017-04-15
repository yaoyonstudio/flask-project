from flask import Flask, request

app = Flask(__name__)

app.config.from_object('app.config')

# send CORS headers
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response

from app.models import db
db.init_app(app)


from app.routes import Api
# init_api(app)
