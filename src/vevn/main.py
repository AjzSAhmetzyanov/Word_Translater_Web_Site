from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse
import requests

app = Flask(__name__)
api = Api(app)

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'Zjc0MjExYTUtY2RhYy00ZmQxLTliYWItYzBiMGI5ZjE2MzE2OjJlMDNkNjk1NjEwOTRkZDM4N2YzMWM2MWY2ZTUzNmMy'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)


@app.route('/')
def __init__():
    mess = "";
    if auth.status_code == 200:
        token = auth.text
        word = request.args.get("textin")
        print(word)
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1049
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            mess = res['Translation']['Translation']
    else:
        print("Error!")
    return render_template('index.html', message=mess)


api.init_app(app)
if __name__ == "__main__":
    app.run(port=4000, host="127.0.0.1")
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
