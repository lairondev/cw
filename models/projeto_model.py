from config import db, app

class Projeto(db.Model):
  __tablename__ = "projeto"
  
  id_projeto = db.Column(db.Integer, autoincrement=True, primary_key=True)
  solicitante = db.Column(db.String(49))
  nome = db.Column(db.String(49))
  tipo = db.Column(db.String(49))
  tecnologia = db.Column(db.String(49))
  detalhes = db.Column(db.Text(49))
  valor = db.Column(db.String(49))
  metodo_pag = db.Column(db.String(49))
  data_entrega = db.Column(db.String(49))
  status = db.Column(db.String(49))
  
  cliente_rel = db.Column(db.String(49), db.ForeignKey("cliente.id_cliente"), nullable=False)
  
  def __init__(self, solicitante, nome, tipo, tecnologia, detalhes, valor, metodo_pag, data_entrega, status):
    self.solicitante = solicitante
    self.nome = nome
    self.tipo = tipo
    self.tecnologia = tecnologia
    self.detalhes = detalhes
    self.valor = valor
    self.metodo_pag = metodo_pag
    self.data_entrega = data_entrega
    self.status = status
    
with app.app_context():
  db.create_all()