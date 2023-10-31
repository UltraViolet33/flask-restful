from email import message
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

# db.create_all()


# video_put_args = reqparse.RequestParser()
# video_put_args.add_argument(
#     "name", type=str, help="Name of the video is required", required=True)
# video_put_args.add_argument(
#     "views", type=int, help="views of the video is required", required=True)
# video_put_args.add_argument(
#     "likes", type=int, help="likes on the video is required", required=True)


# video_update_args = reqparse.RequestParser()
# video_update_args.add_argument(
#     "name", type=str, help="Name of the video is required")
# video_update_args.add_argument(
#     "views", type=int, help="views of the video is required")
# video_update_args.add_argument(
#     "likes", type=int, help="likes on the video is required")


# resource_field = {
#     "id": fields.Integer,
#     "name": fields.String,
#     "views": fields.Integer,
#     "likes": fields.Integer
# }


# class Video(Resource):

#     @marshal_with(resource_field)
#     def get(self, video_id):
#         result = VideoModel.query.filter_by(id=video_id).first()
#         if not result:
#             abort(404, message="This video does not exist")
#         return result

#     @marshal_with(resource_field)
#     def put(self, video_id):
#         args = video_put_args.parse_args()
#         result = VideoModel.query.filter_by(id=video_id).first()
#         if result:
#             abort(409, message="This video ID already exists")
#         video = VideoModel(
#             id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
#         db.session.add(video)
#         db.session.commit()
#         return video, 201

#     @marshal_with(resource_field)
#     def patch(self, video_id):
#         args = video_update_args.parse_args()
#         result = VideoModel.query.filter_by(id=video_id).first()
#         if not result:
#             abort(404, message="This video does not exists")

#         if args['name']:
#             result.name = args['name']
#         if args['views']:
#             result.views = args['views']
#         if args['likes']:
#             result.likes = args['likes']

#         db.session.commit()
#         return result

#     # def delete(self, video_id):
#     #     del videos[video_id]
#     #     return '', 204


# api.add_resource(Video, "/video/<int:video_id>")

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

parser = reqparse.RequestParser()
parser.add_argument('task')

class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

api.add_resource(TodoList, '/todos')

if __name__ == "__main__":
    app.run(debug=True)
