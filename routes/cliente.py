from flask import Blueprint, render_template, request, url_for, redirect
from config import db
from models.model import Cliente

# CRIANDO VARIÁVEL DE ROTA BP
cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/")
def lista_clientes():
    page = "Clientes"
    title = "Lista de clientes"
    clientes = Cliente.query.all()
    return render_template("lista_clientes.html", page=page, title=title, clientes=clientes)
  
  
@cliente_bp.route("/novo")
def form_novo_cliente():
    page = "Clientes"
    title = "Novo cliente"
    return render_template("novo_cliente.html", page=page, title=title)
  
  
@cliente_bp.route("/cadastra", methods=["POST", "GET"])
def cadastra_cliente():
    
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        fone = request.form["fone"]
        cpf_cnpj = request.form["cpf_cnpj"]
        logra = request.form["logra"]
        cep = request.form["cep"]
        bairro = request.form["bairro"]
        comple = request.form["comple"]
        cidade = request.form["cidade"]
        uf = request.form["uf"]
        status = request.form["status"]
        
        try:
            new_cliente = Cliente(
                nome, email, fone, cpf_cnpj, logra, cep, bairro, comple, cidade, uf, status
            )
            
            db.session.add(new_cliente)
            db.session.commit()
            msg = "Cadastro efetuado com sucesso!"
            alert = "success"
            return redirect(url_for('cliente.form_novo_cliente', msg=msg, alert=alert))
            
        except Exception as e:
            db.session.rollback()
            msg = f"Não foi possível cadastrar - Erro {str(e)}"
            alert = "danger"
            return redirect(url_for('cliente.form_novo_cliente', msg=msg, alert=alert))
 
 
@cliente_bp.route("/<int:id_cliente>/editar")
def form_editar_cliente(id_cliente):
    page = "Clientes"
    title = "Alterar dados"
    msg = ""
    alert = ""
    cliente = Cliente.query.get(id_cliente)
    if not cliente:
        msg = "O cliente selecionado não existe, selecione um cliente válido."
        alert = "warning"
        return  redirect(url_for('cliente.lista_clientes', msg=msg, alert=alert))
    
    return render_template("editar_cliente.html", page=page, title=title, cliente=cliente, id_cliente=id_cliente)
  
  
@cliente_bp.route("/atualiza", methods=["POST"])
def atualiza_cliente():
    if request.method == "POST":
        id_cliente = request.form["id_cliente"]
        cli = Cliente.query.get(id_cliente)
        
        if cli:
            nome = request.form["nome"]
            email = request.form["email"]
            fone = request.form["fone"]
            cpf_cnpj = request.form["cpf_cnpj"]
            logra = request.form["logradouro"]
            cep = request.form["cep"]
            bairro = request.form["bairro"]
            comple = request.form["complemento"]
            cidade = request.form["cidade"]
            uf = request.form["uf"]
        
            try:
                cli.nome = nome
                cli.email = email
                cli.fone = fone
                cli.cpf_cnpj = cpf_cnpj
                cli.logradouro = logra
                cli.cep = cep
                cli.bairro = bairro
                cli.complemento = comple
                cli.cidade = cidade
                cli.uf = uf
                
                db.session.commit()
                msg = "Dados atualizados com sucesso!"
                alert = "success"
                print(msg)
                return redirect(url_for('cliente.lista_clientes', msg=msg, alert=alert))
                
            except Exception as e:
                db.session.rollback()
                msg = f"Não foi possível atualizar - Erro {str(e)}"
                alert = "danger"    
                print(msg)
                return redirect(url_for('cliente.lista_clientes', msg=msg, alert=alert))
                
   
@cliente_bp.route("/<int:id_cliente>/delete")
def delete(id_cliente):
    pass