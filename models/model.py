from werkzeug.security import generate_password_hash, check_password_hash
from config import db, app

class Cliente(db.Model):
    __tablename__ = "cliente"
    
    id_cliente = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(49))
    email = db.Column(db.String(49))
    fone = db.Column(db.String(49))
    cpf_cnpj = db.Column(db.String(49))
    logradouro = db.Column(db.String(80))
    cep = db.Column(db.String(49))
    bairro = db.Column(db.String(49))
    complemento = db.Column(db.String(49))
    cidade = db.Column(db.String(49))
    uf = db.Column(db.String(49))
    status = db.Column(db.String(49))
    
    projetos = db.relationship("Projeto", backref="cliente", cascade="all, delete-orphan", lazy=True)
    
    def __init__(self, nome, email, fone, cpf_cnpj, logradouro, cep, bairro, complemento, cidade, uf, status):
        self.nome = nome
        self.email = email
        self.fone = fone
        self.cpf_cnpj = cpf_cnpj
        self.logradouro = logradouro
        self.cep = cep
        self.bairro = bairro
        self.complemento = complemento
        self.cidade = cidade
        self.uf = uf
        self.status = status
        
class Projeto(db.Model):
    __tablename__ = "projeto"

    id_projeto = db.Column(db.Integer, autoincrement=True, primary_key=True)
    titulo = db.Column(db.String(49))
    tipo = db.Column(db.String(49))
    tecnologia = db.Column(db.String(49))
    detalhes = db.Column(db.Text(49))
    valor = db.Column(db.String(49))
    metodo_pag = db.Column(db.String(49))
    data_entrega = db.Column(db.String(49))
    status = db.Column(db.String(49))
    
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id_cliente"))
    
    def __init__(self, titulo, tipo, tecnologia, detalhes, valor, metodo_pag, data_entrega, status, cliente_id):
        self.titulo = titulo
        self.tipo = tipo
        self.tecnologia = tecnologia
        self.detalhes = detalhes
        self.valor = valor
        self.metodo_pag = metodo_pag
        self.data_entrega = data_entrega
        self.status = status
        self.cliente_id = cliente_id
    


class User(db.Model):
    __tablename__ = "user"
    
    id_user = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nick = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    nome = db.Column(db.String(20))
    sobrenome = db.Column(db.String(20))
    skill = db.Column(db.String(10))
    fone = db.Column(db.String(15))
    foto = db.Column(db.String(255))
    senha = db.Column(db.String(200))
    
    def __init__(self, nick, email, nome, sobrenome, skill, fone, foto, senha):
        self.nick = nick
        self.email = email
        self.nome = nome
        self.sobrenome = sobrenome
        self.skill = skill
        self.fone = fone
        self.foto = foto
        self.senha = generate_password_hash(senha)

    def verify_password(self, senha):
        return check_password_hash(self.senha, senha)


with app.app_context():
  db.create_all()