from flask import Blueprint, render_template, request, url_for, redirect
from config import db
from models.cliente_model import Cliente
from models.projeto_model import Projeto

# CRIANDO VARIÁVEL DE ROTA BP
projeto_bp = Blueprint("projeto", __name__)

@projeto_bp.route("/")
def lista_projetos():
    page = "Projetos"
    title = "Listando projetos"
    return render_template("lista_projetos.html", page=page, title=title)
    
    
@projeto_bp.route("/novo")
def form_novo_projeto():
    page = "Projetos"
    title = "Novo projeto"
    clientes = Cliente.query.all()
    return render_template("novo_projeto.html", page=page, title=title, clientes=clientes)
    
    
@projeto_bp.route("/cadastra", methods=["POST", "GET"])
def cadastra_projeto():
    if request.method == "POST":
        solic = request.form["solic"]
        nome = request.form["nome"]
        tipo = request.form["tipo"]
        tec = request.form["tec"]
        desc = request.form["desc"]
        valor = request.form["valor"]
        metodo_pag = request.form["metodo_pag"]
        data = request.form["data"]
        status = request.form["status"]
        
        cliente = Cliente.query.get(solic)
        
        try:
            new_projeto = Projeto(
                solic, nome, tipo, tec, desc, valor, metodo_pag, data, status, cliente
            )
            db.session.add(new_projeto)
            db.session.commit()
            msg = f"Novo projeto {nome} cadastrado com sucesso!"
            alert = "success"
            return redirect(url_for('projeto.form_novo_projeto', msg=msg, alert=alert))
            
        except Exception as e:
            db.session.rollback()
            msg = f"Não foi possível cadastrar o projeto <strong>{nome}</strong> - Erro {str(e)}"
            alert = "danger"
            return redirect(url_for('cliente.form_novo_cliente', msg=msg, alert=alert))
           
    
    
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