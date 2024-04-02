from flask import Flask, url_for

# IMPORTANDO VARIÁVEIS DE ROTA BP
from routes.home import home_bp
from routes.cliente import cliente_bp
from routes.projeto import projeto_bp

app = Flask(__name__)

# REGISTRANDO AS ROTAS BP
app.register_blueprint(home_bp)
app.register_blueprint(cliente_bp, url_prefix="/cliente")
app.register_blueprint(projeto_bp, url_prefix="/projeto")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")