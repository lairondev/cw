from flask import Flask
from config import app

# IMPORTANDO VARIÁVEIS DE ROTA BP
from routes.home import home_bp
from routes.cliente import cliente_bp
from routes.projeto import projeto_bp
from routes.perfil import perfil_bp


# REGISTRANDO AS ROTAS BP
app.register_blueprint(home_bp)
app.register_blueprint(cliente_bp, url_prefix="/cliente")
app.register_blueprint(projeto_bp, url_prefix="/projeto")
app.register_blueprint(perfil_bp, url_prefix="/perfil")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
