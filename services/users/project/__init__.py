# services/users/project/__init__.py


from flask import Flask
from flask_restful import Resource, Api


# instantiate the app
app = Flask(__name__)
api = Api(app)

# set config via Flask
app.config.from_object('project.config.DevelopmentConfig')


class UsersPing(Resource):
    def get(self):
        return {
            'status': 'successful ping!',
            'message': 'pong!'
        }


api.add_resource(UsersPing, '/users/ping')
