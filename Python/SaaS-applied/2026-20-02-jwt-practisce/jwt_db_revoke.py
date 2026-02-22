from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()

class User(db.Model):
    __tablename__="user"

    id=db.Column(db.Integer(), primary_key=True)
    email=db.Column(db.String(64), nullable=False, index=True)
    
    jwt=db.relationship("Jwt_Revoque", back_populates="user", lazy=False)



class Jwt_Revoque(db.Model):    #Relación 1:N, un usuario con varios tokens individuales
    __tablename__="jwt_revoque"

    id=db.Column(db.Integer(), primary_key=True)
    jti=db.Column(db.String(64), nullable=False, index=True)
    created_at=db.Column(db.DateTime(), nullable=False, default=datetime.now())

    user_id=db.Column(db.ForeignKey("user.id"), nullable=False)
    user=db.relationship("User", back_populates="jwt")
