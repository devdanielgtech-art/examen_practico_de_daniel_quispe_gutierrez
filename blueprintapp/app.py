from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///techbol_de_daniel.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Importar modelos para que Flask-Migrate los detecte
    from blueprintapp.clientes.models import Cliente
    from blueprintapp.productos.models import Producto
    from blueprintapp.pedidos.models import Pedido
    
    # Importar y registrar blueprints
    from blueprintapp.clientes.routes import bp_clientes
    from blueprintapp.productos.routes import bp_productos
    from blueprintapp.pedidos.routes import bp_pedidos
    
    app.register_blueprint(bp_clientes, url_prefix="/clientes")
    app.register_blueprint(bp_productos, url_prefix="/productos")
    app.register_blueprint(bp_pedidos, url_prefix="/pedidos")
    
    @app.route("/")
    def index():
        return render_template('base.html') 
    
    return app