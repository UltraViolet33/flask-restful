from email import message
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

#from models import TodoModel


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)


class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'task': self.task}

# db.create_all()

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

parser = reqparse.RequestParser()
parser.add_argument('task', type='string', help='task of todo, cannot be empty')

def abort_if_todo_doesnt_exist(todo_id):
    abort(404, message="Todo {} doesn't exist".format(todo_id))

class Todo(Resource):
    def get(self, todo_id):
        todo = TodoModel.query.get(todo_id)
        if not todo:
            abort_if_todo_doesnt_exist(todo_id)
        return todo.to_dict()

    def delete(self, todo_id):
        todo = TodoModel.query.get(todo_id)
        if not todo:
            abort_if_todo_doesnt_exist(todo_id)
        todo.delete()
        db.session.commit()
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        todo = TodoModel.query.get(todo_id)
        if not todo:
            abort_if_todo_doesnt_exist(todo_id)
        todo.task = args['task']
        db.session.commit()
        return task, 201


class TodoList(Resource):
    def get(self):
        todos = [] 
        for todo in TodoModel.query.all():
            todos.append(todo.to_dict())
        return todos


    def post(self):
        args = parser.parse_args()
        todo  = TodoModel(task=args['task'])
        db.session.add(todo)
        db.session.commit()
        return todo.to_dict(), 201

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == "__main__":
    app.run(debug=True)
