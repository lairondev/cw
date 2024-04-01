from flask import Blueprint, render_template

# CRIANDO VARIÁVEL DE ROTA BP
home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    title = "Início"
    return "Olá estamos iniciando a CriativaWeb"
    #return render_template("index.html")