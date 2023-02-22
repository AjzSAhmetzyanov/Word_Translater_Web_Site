from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import requests as req
import json

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')


# courses = {
#     1: {"name": "Python", "videos": 13},
#     2: {"name": "Java", "videos": 12}
# }
#
# parser = reqparse.RequestParser()
# parser.add_argument("name", type=str)
# parser.add_argument("videos", type=int)
#
#
# class Main(Resource):
#     def get(self):
#         response = req.get('https://reqres.in/api/users?page=2')
#         if response.status_code == 200:
#             return response.json()
#
#     def delete(self, course_id):
#         del courses[course_id]
#         return courses
#
#     def post(self):
#         payload = {"name": "Anthony", "job": "Programmer"}
#         res = req.post('https://reqres.in/api/users', data=json.dumps(payload))
#         if res.status_code == 200:
#             return res.json()
#
#     def put(self, course_id):
#         courses[course_id] = parser.parse_args()
#         return courses
#
#
# api.add_resource(Main, "/api/courses/<int:course_id>")
api.init_app(app)
if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1")
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
