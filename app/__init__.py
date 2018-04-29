from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['SECRET_KEY'] = "some$3448eiwjkse3"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:secret@localhost/project1"
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://abmszhfntszpqc:1ae49005b227ad8399e0b43ecd8d8b73b516eb8d75485a74e58960ec0ecc8e60@ec2-54-83-23-91.compute-1.amazonaws.com:5432/dej8jsv085l7ip'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
csrf = CSRFProtect(app)
from app import views