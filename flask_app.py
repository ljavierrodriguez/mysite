import os
from flask import Flask, jsonify, request, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, Mensajes

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'production.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('api/messages', methods=['GET', 'POST'])
@app.route('api/messages/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def messages(id = None):
    if request.method == 'GET':
        if id is not None:
            message = Mensajes.query.get(id)
            if message:
                return jsonify(message.serialize()), 200
            else:
                return jsonify({"msg":"Message not found"}), 404
        else:
            messages = Mensajes.query.all()
            messages = list(map(lambda msg: msg.serialize(), messages))
            return jsonify(messages), 200

    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


#if __name__ == '__main__':
#    manager.run()