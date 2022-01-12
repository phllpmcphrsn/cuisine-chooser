from flask_sqlalchemy import SQLAlchemy

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuisine = db.Column(db.String(100))