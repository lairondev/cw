from config import db, app
from models.projeto_model import Projeto

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
    
    projetos = db.relationship("Projeto", backref="cliente", lazy=True)
    
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
        
with app.app_context():   
    db.create_all()