from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_marshmallow import Marshmallow
#https://python-forum.io/Thread-Flask-Implementing-SQLAlchemy-with-Blueprints
#https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login-es

db = SQLAlchemy()
ma = Marshmallow()


# modelo de usuario
class User(UserMixin, db.Model):
    __tablename__ = 'user'  
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    business= db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))    
    codeConfi = db.Column(db.String(50))
    userTipe = db.Column(db.String(50))
    dates = db.Column(db.Date)

    #https://j2logo.com/tutorial-flask-leccion-5-base-de-datos-con-flask-sqlalchemy/
    #is_admin = db.Column(db.Boolean, default=False)
    # tipos https://overiq.com/flask-101/database-modelling-in-flask/#:~:text=SQLAlchemy%20and%20Flask%2DSQLAlchemy,SQL%2C%20SQLite%20and%20so%20on.
    #date_created = Column(DateTime, auto_now_add=True)

    def __ini__(self, email, name, business, password, codeConfi, userTipe, dates):
        self.email = email
        self.name = name
        self.business = business        
        self.password = password        
        self.codeConfi = codeConfi
        self.userTipe = userTipe
        self.dates = dates

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserSchema(ma.Schema):
    class Meta:
        # Campos de la tabla
        fields  = ('id', 'email', 'name', 'business', 'password', 'codeConfi', 'userTipe', 'dates' )


# modelo de codigo
class Codes(db.Model):
    __tablename__ = 'codes'  
    id = db.Column(db.Integer, primary_key=True)
    codes = db.Column(db.String(100), unique=True)
    types = db.Column(db.String(100))
    states = db.Column(db.Integer)

    def __ini__(self, codes, types, states):
        self.codes = codes
        self.types = types
        self.states = states


class CodesSchema(ma.Schema):
    class Meta:
        # Campos de la tabla
        fields  = ('id', 'codes', 'type', 'states' )


# modelo de proyecto
class Projects(db.Model):
    __tablename__ = 'project'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    localization = db.Column(db.String(255))
    favorites = db.Column(db.Integer)
    date_=db.Column(db.Date)
    
    def __ini__(self, name, localization, favorites, date_):
        self.name = name
        self.localization = localization
        self.favorites = favorites
        self.date_ = date_
        
class ProjectsSchema(ma.Schema):
    class Meta:
        # Campos de la tabla
        fields  = ('id', 'name', 'localization', 'favorites','date_' )
