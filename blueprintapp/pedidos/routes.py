from flask import request, render_template, redirect, url_for, Blueprint
from blueprintapp.app import db
from blueprintapp.pedidos.models import Pedido
from blueprintapp.clientes.models import Cliente
from blueprintapp.productos.models import Producto
from datetime import datetime

bp_pedidos = Blueprint('bp_pedidos', __name__, template_folder='templates')

@bp_pedidos.route("/")
def index():
    pedidos = Pedido.query.all()
    return render_template('pedidos/index.html', pedidos=pedidos)

@bp_pedidos.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        clientes = Cliente.query.all()
        productos = Producto.query.all()
        return render_template('pedidos/create.html', clientes=clientes, productos=productos)
    elif request.method == 'POST':
        cliente_id = int(request.form.get('cliente_id'))
        producto_id = int(request.form.get('producto_id'))
        producto = Producto.query.get(producto_id)
        monto = producto.precio
        pedido = Pedido(cliente_id=cliente_id, producto_id=producto_id, monto=monto)
        db.session.add(pedido)
        db.session.commit()
        return redirect(url_for('bp_pedidos.index'))

@bp_pedidos.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    pedido = Pedido.query.get_or_404(id)
    if request.method == 'GET':
        clientes = Cliente.query.all()
        productos = Producto.query.all()
        return render_template('pedidos/edit.html', pedido=pedido, clientes=clientes, productos=productos)
    elif request.method == 'POST':
        pedido.cliente_id = int(request.form.get('cliente_id'))
        pedido.producto_id = int(request.form.get('producto_id'))
        pedido.fecha = datetime.strptime(request.form.get('fecha'), '%Y-%m-%d')
        db.session.commit()
        return redirect(url_for('bp_pedidos.index'))

@bp_pedidos.route("/delete/<int:id>")
def delete(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('bp_pedidos.index'))