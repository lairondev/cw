from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# CRIA E CONFIGURA OBJETOS DO FLASK E BANCO DE DADOS
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://lairondev:Dontcare_30@localhost/criativaweb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
