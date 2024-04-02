from flask import Blueprint, render_template

# CRIANDO VARIÁVEL DE ROTA BP
home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    page = "Início"
    title = "Visão geral"
    return render_template("home.html", title=title, page=page)