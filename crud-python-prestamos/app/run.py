from flask import Flask
from controllers.prestamos_controller import prestamo_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database import db

app = Flask(__name__)

# Configuración de Swagger
SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "API de Préstamos"})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prestamos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Registro del blueprint de préstamos
app.register_blueprint(prestamo_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
    db.create_all()

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run(debug=True)
