from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Mensajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    message = db.Column(db.String(400), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "message": self.message
        } 