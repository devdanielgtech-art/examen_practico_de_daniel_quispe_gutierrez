from blueprintapp.app import db

class Cliente(db.Model):
    __tablename__ = "clientes"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    
    # Relación con Pedidos
    pedidos = db.relationship('Pedido', back_populates='cliente', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<Cliente: {self.nombre}>"