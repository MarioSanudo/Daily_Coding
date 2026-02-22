from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()

class User(db.Model):
    __tablename__="user"

    id=db.Column(db.Integer(), primary_key=True)
    email=db.Column(db.String(64), nullable=False, index=True)
    
    user_jwt=db.relationship("User_Jwt", back_populates="user_info", lazy="selectin")



class Jwt_Revoque(db.Model):
    __tablename__="jwt_revoque"

    id=db.Column(db.Integer(), primary_key=True)
    jti=db.Column(db.String(64), nullable=False, index=True)
    created_at=db.Column(db.DateTime(), nullable=False, default=datetime.now())
    
    user_jwt=db.relationship("User_Jwt", back_populates="jwt", lazy="selectin")



class User_Jwt(db.Model):
    __tablename__="user_jwt"

    id=db.Column(db.Integer(), primary_key=True)
    user_id=db.Column(db.ForeignKey("user.id"), nullable=False, unique=True)
    jwt_id=db.Column(db.ForeignKey("jwt_revoque.id", nullable=False, unique=True))

    user_info=db.relationship("User", back_populates="user_jwt")
    jwt=db.relationship("Jwt_Revoque", back_populates="user_jwt")
