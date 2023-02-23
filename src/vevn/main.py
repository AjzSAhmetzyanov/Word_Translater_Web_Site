from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse
import requests

app = Flask(__name__)
api = Api(app)

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'YTExYTEyYTQtZmQxYS00YzhjLThhNTMtNmQ2YjdhN2MxZmMwOmY1N2VjZGRiZjI0NzQ3MjI5MGY1MDVmYzY1NmM3YzM5'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)


@app.route('/')
def __init__():
#     return render_template('index.html')
#
#
# @app.get('/')
# def get(self):
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
            try:
                print(res['Translation']['Translation'])
            except:
                print("Не найдено слов для перевода")
    else:
        print("Error!")
    return render_template('index.html', message=res['Translation']['Translation'])


api.init_app(app)
if __name__ == "__main__":
    app.run(port=4000, host="127.0.0.1")
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
