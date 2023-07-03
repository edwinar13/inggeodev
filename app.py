from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager

# API fazt
#https://www.youtube.com/watch?v=MvVqjQqSdM4

# organizacion ficheros
#https://hackersandslackers.com/flask-blueprints/

app = Flask(__name__)

# Configuración 
app.config['SECRET_KEY'] = '8659dgf6584sehy'
app.config['UPLOAD_FOLDER'] = './Archivos_PDF'
PORT=5000
DEBUG=True



# Conexión  MySQL local
'''
server = 'localhost'
username = 'root'
password = 'password'
database = 'inggeosoftmysql'
'''
# Conexión  MySQL clever cloud

server = 'bloci4hdgp2hd4tshe0q-mysql.services.clever-cloud.com'
username = 'unamxdpmr7hw93zb'
password = 'owz2w5yTRyur3CWSFuyA'
database = 'bloci4hdgp2hd4tshe0q'


# Conexión  MySQL

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}".format(username, password, server, database)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20


from models import db
db.init_app(app)

#db = SQLAlchemy(app)
#ma = Marshmallow(app)
from models import ma
ma.init_app(app)


login_manager = LoginManager()
login_manager.login_view = 'authPage.login'
login_manager.init_app(app)



from models import User
@login_manager.user_loader
def load_user(user_id):   
    print('='*100) 
    print(user_id)
    print('='*100) 
    return User.query.get(int(user_id))




# rutas - endpoint
@app.route('/addUser', methods=['POST'])
def registerUser():
    print(request)
    return 'recivido'


# blueprint for non-auth parts of app
from BPindex.indexPage  import indexPage as index_blueprint
app.register_blueprint(index_blueprint)

# blueprint for non-auth parts of app
from BPapplication.appPage import appPage as app_blueprint
app.register_blueprint(app_blueprint)

# blueprint for auth routes in our app
from BPauthentication.authPage import authPage as auth_blueprint
app.register_blueprint(auth_blueprint)




@app.errorhandler(404)
def not_found(error):
    return 'Esta página no existe! visita inggeodev.com'


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)