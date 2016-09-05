# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
from flask import Flask
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


@app.route('/search/exemptions/<term>/<filters>/<start_date>/<end_date>/<offset>/<size>')
def search_exemptions(term, filters, start_date, end_date, offset, size):
    ret = elastic.search_exemptions(term, filters, start_date, end_date, offset, size)
    return json.dumps(ret)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
# [END app]
