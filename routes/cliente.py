from flask import Blueprint, render_template

# CRIANDO VARIÁVEL DE ROTA BP
cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/")
def lista_clientes():
    page = "Clientes"
    title = "Lista de clientes"
    return render_template("lista_clientes.html", page=page, title=title)
    
@cliente_bp.route("/novo")
def form_novo_cliente():
    pass
    
@cliente_bp.route("/cadastra")
def cadastra_cliente():
    pass
    
@cliente_bp.route("/<int:id_cliente>/editar")
def form_editar_cliente(id_cliente):
    pass
    
@cliente_bp.route("/<int:id_cliente>/atualiza")
def atualiza_cliente():
    pass
    
@cliente_bp.route("/<int:id_cliente>/delete")
def delete(id_cliente):
    pass