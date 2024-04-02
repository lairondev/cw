from flask import Blueprint, render_template
from cwdb.database import PROJETOS

# CRIANDO VARIÁVEL DE ROTA BP
projeto_bp = Blueprint("projeto", __name__)

@projeto_bp.route("/")
def lista_projetos():
    page = "Projetos"
    title = "Listando projetos"
    
    global PROJETOS
    return render_template("lista_projetos.html", page=page, title=title, projeto=PROJETOS)
    
@projeto_bp.route("/novo")
def form_novo_projeto():
    page = "Projetos"
    title = "Novo projeto"
    return render_template("novo_projeto.html", page=page, title=title)
    
@projeto_bp.route("/cadastra")
def cadastra_projeto():
    pass
    
@projeto_bp.route("/<int:id_projeto>/editar")
def form_editar_projeto(id_projeto):
    page = "Projetos"
    title = "Alterar dados"
    return render_template("editar_projeto.html", page=page, title=title)
    
@projeto_bp.route("/<int:id_projeto>/atualiza")
def atualiza_projeto(id_projeto):
    pass
    
@projeto_bp.route("/<int:id_projeto>/delete")
def delete(id_projeto):
    pass