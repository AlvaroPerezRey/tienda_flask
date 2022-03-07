from shop import db

class Cliente(db.Model):
    __tablename__ = 'cliente'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    email = db.column(db.String(50))
    telefono = db.Column(db.Integer(12))
    password = db.Column(db.String(80))
    dni = db.Column(db.String(9))
    direcciones = db.relationship("Direccion", backref="clientes")
    pedidos = db.relationship("Pedido", backref="clientes")

    def __repr__(self):
        return f"Cliente('{self.nombre}', '{self.apellidos}', '{self.email}'," \
               f"'{self.telefono}', '{self.password}', '{self.dni}')"

class Direccion(db.Model):
    __tablename__ = 'direccion'
    __table_args__ = {"useexisting": True}
    via = db.Column(db.String(100))
    nombre = db.Column(db.String(50))
    numero = db.Column(db.Integer())
    cod_postal = db.Column(db.Integer())
    ciudad = db.Column(db.String(50))
    cliente_id = db.Column(db.Integer(), db.ForeignKey('cliente.id'))

    def __repr__(self):
        return f"Direccion('{self.via}', '{self.nombre}', '{self.numero}'," \
               f"'{self.cod_postal}', '{self.ciudad}')"

class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    cif = db.Column(db.String(9))
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    email = db.column(db.String(50))
    telefono = db.Column(db.Integer(12))

    def __repr__(self):
        return f"Proveedor('{self.cif}', '{self.nombre}', '{self.direccion}'," \
               f"'{self.email}', '{self.telefono}')"

class Producto(db.Model):
    __tablename__ = 'producto'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    stock = db.Column(db.Integer())
    precio_unidad = db.Column(db.Integer())
    categoria = db.Column(db.String(20))
    proveedor_id = db.Column(db.Integer(), db.ForeignKey('proveedor.id'))
    proveedores = db.relationship("Proveedor", backref="productos")


    def __repr__(self):
        return f"Producto('{self.nombre}', '{self.marca}', '{self.stock}'," \
               f"'{self.precio_unidad}', '{self.categoria}')"

class Pedido(db.Model):
    __tablename__ = 'pedido'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    fecha = db.Column(db.DateTime())
    cantidad = db.Column(db.Integer())
    total = db.Column(db.Integer())
    cliente_id = db.Column(db.Integer(), db.ForeignKey('cliente.id'))
    producto_id = db.Column(db.Integer(), db.ForeignKey('producto.id'))
    productos = db.relationship("Productos", backref="pedidos")

    def __repr__(self):
        return f"Pedido('{self.fecha}', '{self.cantidad}', '{self.total}')"

class Factura(db.Model):
    __tablename__ = 'factura'
    __table_args__ = {"useexisting": True}    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    fecha = db.Column(db.DateTime())
    importe_total = db.Column(db.Integer())
    pedido_id = db.Column(db.Integer(), db.ForeignKey('pedido.id'))

    def __repr__(self):
        return f"Factura('{self.fecha}', '{self.importe_total}')"

class Pago(db.Model):
    __tablename__ = 'pago'
    __table_args__ = {"useexisting": True}    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    factura_id = db.Column(db.Integer(), db.ForeignKey('factura.id'))

    def __repr__(self):
        return f"Pago('{self.id}', '{self.factura_id}')"

class Tarjeta(db.Model):
    __tablename__ = 'tarjeta'
    __table_args__ = {"useexisting": True}    
    num_tarjeta = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    titular = db.Column(db.String(100))
    caducidad = db.Column(db.String(5))
    cliente_id = db.Column(db.Integer(), db.ForeignKey('cliente.id'))

    def __repr__(self):
        return f"Tarjeta('{self.num_tarjeta}', '{self.titular}', '{self.caducidad}')"

class Cuenta_Bancaria(db.Model):
    __tablename__ = 'cuenta_bancaria'
    __table_args__ = {"useexisting": True}
    num_cuenta = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    titular = db.Column(db.String(100))
    entidad = db.Column(db.String(100))
    cliente_id = db.Column(db.Integer(), db.ForeignKey('cliente.id'))

    def __repr__(self):
        return f"C.Bancaria('{self.num_cuenta}', '{self.titular}', '{self.entidad}')"