from flask import Blueprint, render_template, request, redirect, url_for
from models.model import User
from config import db

# CRIANDO VARIÁVEL DE ROTA BP
perfil_bp = Blueprint("perfil", __name__)


@perfil_bp.route("/")
def lista_perfil():
    ...


@perfil_bp.route("/<string:nome_perfil>")
def perfil_view(nome_perfil):
    page = "Perfil"
    title = "Visualizando perfil"
    return render_template("perfil.html", page=page, title=title)
    

@perfil_bp.route("/novo")
def form_novo_perfil():
    page = "Perfil"
    title = "Novo usuário"
    return render_template("novo_user.html", page=page, title=title)
    

@perfil_bp.route("/cadastra", methods=["POST", "GET"])
def cadastra_perfil():
    if request.method == "POST":
        nick = request.form["nick"]
        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        email = request.form["email"]
        fone = request.form["fone"]
        func = request.form["func"]
        foto = "caminho_da_foto"
        senha1 = request.form["senha1"]
        senha2 = request.form["senha2"]

        verifica_email = User.query.filter_by(email=email).first()

        if not senha1 == senha2:
            msg = "Senhas não coincidem"
            alert = "danger"
            return redirect(url_for('perfil.form_novo_perfil', msg=msg, alert=alert))
        
        elif verifica_email:
            msg = "O email inserido já está em uso"
            alert = "danger"
            return redirect(url_for('perfil.form_novo_perfil', msg=msg, alert=alert))

        else:
            try:
                new_perfil = User(
                    nick, email, nome, sobrenome, func, fone, foto, senha1
                )

                db.session.add(new_perfil)
                db.session.commit()

                msg = "Usuário cadastrado com sucesso!"
                alert = "success"
                return redirect(url_for('perfil.form_novo_perfil', msg=msg, alert=alert))
            
            except Exception as e:
                db.session.rollback()
                msg = "Não foi possível cadastrar, contate o desenvolvedor."
                alert = "danger"
                return redirect(url_for('perfil.form_novo_perfil', msg=msg, alert=alert))


@perfil_bp.route("/<int:id_perfil>/editar")
def form_editar_perfil(id_perfil):
    ...


@perfil_bp.route("/atualiza", methods=["POST"])
def atualiza_perfil():
    ...


@perfil_bp.route("/<int:id_perfil>/delete")
def delete(id_perfil):
    ...
    