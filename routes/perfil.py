from flask import Blueprint, render_template

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
    ...


@perfil_bp.route("/<int:id_perfil>/editar")
def form_editar_perfil(id_perfil):
    ...


@perfil_bp.route("/atualiza", methods=["POST"])
def atualiza_perfil():
    ...


@perfil_bp.route("/<int:id_perfil>/delete")
def delete(id_perfil):
    ...
    