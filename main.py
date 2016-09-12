
from flask import Flask, request
import elastic
import json


app = Flask(__name__)

#
# @app.route('/search/<term>/')
# def search(term):
#     return json.dumps(elastic.search(term))
#
# @app.route('/search/<term>/<filters>')
# def search_with_filters(term, filters):
#     return json.dumps(elastic.search(term))
#
#
# @app.route('/search/<term>/<next_id>')
# def search_with_next_id(term, next_id):
#     return json.dumps(elastic.search(term))


# Search APIs

@app.route('/search/exemption/<term>/<filters>/<start_date>/<end_date>/<offset>/<size>', methods=['GET'])
def search_exemptions(term, filters, start_date, end_date, offset, size):
    ret = elastic.search_exemptions(term, filters, start_date, end_date, offset, size)
    return json.dumps(ret)


# Index data API
@app.route('/index/<type>', methods=['POST'])
def index_exemption():
    print request.data, type
    return "SABABA"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
