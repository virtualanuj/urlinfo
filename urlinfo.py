# Dependencies:
# pip install flask
# pip install redis

from flask import Flask, jsonify
import redis


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '\x81\xa24\xe0\xfe\xdb\xe6\x0f\x14\xfa\x038\xfd\xda\xf1".\xb3\xa4&\x1a\xfc\xd1\xb8'
db = redis.Redis('localhost')

@app.route('/', defaults={'url': ''}, methods = ['GET'])
@app.route('/<path:url>', methods = ['GET'])
def home(url):
    result = {}
    result['url'] = url
    if(db.exists(url)):
        result['response_code'] = 1
        result['message'] = str(db.get(url),'utf-8')
    else:
        result['response_code'] = 0
        result['message'] = 'ok'
    return jsonify(result)

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug(error)
    return jsonify('not found'), 404


@app.errorhandler(500)
def internal_error(error):
    app.logger.debug(error)
    return jsonify('server error'), 500


if __name__ == '__main__':
    app.run()
