import os
from shop import db, migrate, create_app
from shop.models import Cliente, Direccion, Pedido, Producto, Proveedor, Factura, Pago, Tarjeta, Cuenta_Bancaria


env = os.environ.get('SHOP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=Cliente, Direccion=Direccion, Pedido=Pedido, Producto=Producto, Proveedor=Proveedor, Factura=Factura, Pago=Pago, Tarjeta=Tarjeta, Cuenta_Bancaria=Cuenta_Bancaria, migrate=migrate)
