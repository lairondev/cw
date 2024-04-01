from flask import Flask

# IMPORTANDO VARIÁVEIS DE ROTA BP
from routes.home import home_bp

app = Flask(__name__)

# REGISTRANDO AS ROTAS BP
app.register_blueprint(home_bp, url_prefix="")

if __name__ == "__main__":
    app.run(debug=True)