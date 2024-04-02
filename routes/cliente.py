from flask import Blueprint, render_template
from cwdb.database import CLIENTES

# CRIANDO VARIÁVEL DE ROTA BP
cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/")
def lista_clientes():
    page = "Clientes"
    title = "Lista de clientes"
    
    global CLIENTES
    return render_template("lista_clientes.html", page=page, title=title, cliente=CLIENTES)
    
@cliente_bp.route("/novo")
def form_novo_cliente():
    page = "Clientes"
    title = "Novo cliente"
    return render_template("novo_cliente.html", page=page, title=title)
    
@cliente_bp.route("/cadastra")
def cadastra_cliente():
    pass
    
@cliente_bp.route("/<int:id_cliente>/editar")
def form_editar_cliente(id_cliente):
    page = "Clientes"
    title = "Alterar dados"
    return render_template("editar_cliente.html", page=page, title=title)
    
@cliente_bp.route("/<int:id_cliente>/atualiza")
def atualiza_cliente(id_cliente):
    pass
    
@cliente_bp.route("/<int:id_cliente>/delete")
def delete(id_cliente):
    pass