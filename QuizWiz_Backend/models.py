from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
from .extensions import db


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
    options = db.Column(ARRAY(db.Text), nullable=False) 
