from flask import request, render_template, redirect, url_for, Blueprint
from blueprintapp.app import db
from blueprintapp.clientes.models import Cliente

bp_clientes = Blueprint('bp_clientes', __name__, template_folder='templates')

@bp_clientes.route("/")
def index():
    clientes = Cliente.query.all()
    return render_template('clientes/index.html', clientes=clientes)

@bp_clientes.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('clientes/create.html')
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')
        cliente = Cliente(nombre=nombre, telefono=telefono)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('bp_clientes.index'))

@bp_clientes.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.nombre = request.form.get('nombre')
        cliente.telefono = request.form.get('telefono')
        db.session.commit()
        return redirect(url_for('bp_clientes.index'))
    return render_template('clientes/edit.html', cliente=cliente)

@bp_clientes.route("/delete/<int:id>")
def delete(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('bp_clientes.index'))