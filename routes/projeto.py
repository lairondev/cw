from flask import Blueprint, render_template, request, url_for, redirect
from config import db
from models.model import Cliente, Projeto

# CRIANDO VARIÁVEL DE ROTA BP
projeto_bp = Blueprint("projeto", __name__)

@projeto_bp.route("/")
def lista_projetos():
    page = "Projetos"
    title = "Listando projetos"
    projetos = Projeto.query.all()
    return render_template("lista_projetos.html", page=page, title=title, projetos=projetos)
    
    
@projeto_bp.route("/novo")
def form_novo_projeto():
    page = "Projetos"
    title = "Novo projeto"
    clientes = Cliente.query.all()
    return render_template("novo_projeto.html", page=page, title=title, clientes=clientes)
    
    
@projeto_bp.route("/cadastra", methods=["POST", "GET"])
def cadastra_projeto():
    if request.method == "POST":
        titulo = request.form["nome"]
        tipo = request.form["tipo"]
        tec = request.form["tec"]
        desc = request.form["desc"]
        valor = request.form["valor"]
        metodo_pag = request.form["metodo_pag"]
        data = request.form["data"]
        status = request.form["status"]
        dono_proj = request.form["solic"]
        
        try:
            new_projeto = Projeto(
                titulo, tipo, tec, desc, valor, metodo_pag, data, status, dono_proj
            )
            db.session.add(new_projeto)
            db.session.commit()
            msg = f"Novo projeto {titulo} cadastrado com sucesso!"
            alert = "success"
            return redirect(url_for('projeto.form_novo_projeto', msg=msg, alert=alert))
            
        except Exception as e:
            db.session.rollback()
            msg = f"Não foi possível cadastrar o projeto <strong>{titulo}</strong> - Erro {str(e)}"
            alert = "danger"
            return redirect(url_for('cliente.form_novo_projeto', msg=msg, alert=alert))
           
    
    
@projeto_bp.route("/<int:id_projeto>/editar")
def form_editar_projeto(id_projeto):
    page = "Projetos"
    title = "Alterar dados"
    projeto = Projeto.query.get(id_projeto)
    clientes = Cliente.query.all()
    
    if not projeto:
        msg = "O projeto selecionado não existe, selecione um projeto válido."
        alert = "warning"
        return  redirect(url_for('projeto.lista_projetos', msg=msg, alert=alert))
    
    return render_template("editar_projeto.html", page=page, title=title, projeto=projeto, clientes=clientes)
    
    
@projeto_bp.route("/atualiza", methods=["POST", "GET"])
def atualiza_projeto():
    if request.method == "POST":
        id_projeto = request.form["id_projeto"]
        proj = Projeto.query.get(id_projeto)
        
        if proj:
            titulo = request.form["titulo"]
            tipo = request.form["tipo"]
            tec = request.form["tec"]
            desc = request.form["desc"]
            valor = request.form["valor"]
            metodo_pag = request.form["metodo_pag"]
            data = request.form["data"]
            dono_proj = request.form["dono_proj"]
            
            try:
                proj.titulo = titulo
                proj.tipo = tipo
                proj.tecnologia = tec
                proj.detalhes = desc
                proj.valor = valor
                proj.metodo_pag = metodo_pag
                proj.data_entrega = data
                proj.cliente_id = dono_proj
                
                db.session.commit()
                msg = "Dados atualizados com sucesso!"
                alert = "success"
                return redirect(url_for('projeto.lista_projetos', msg=msg, alert=alert))
            
            except Exception as e:
                db.session.rollback()
                msg = f"Não foi possível atualizar - Erro {str(e)}"
                alert = "danger"    
                return redirect(url_for('projeto.lista_projetos', msg=msg, alert=alert))
           
        
    
    
@projeto_bp.route("/<int:id_projeto>/delete")
def delete(id_projeto):
    pass