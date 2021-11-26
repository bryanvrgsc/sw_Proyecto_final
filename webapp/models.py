from datetime import datetime
from sqlalchemy.orm import backref, defaultload, lazyload
from webapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Laboratorista.query.get(int(user_id))

class Laboratorista(db.Model, UserMixin):
    idl = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    active = db.Column(db.Boolean, nullable=False) #! Boolean
    role = db.Column(db.String(20), nullable=False)

    # Relacion a muchos
    certificados = db.relationship("Certificado", backref="laboratorista")
    EquipoLab = db.relationship("EquipoLab", backref="laboratorista")


    def get_id(self):
           return (self.idl)


    def __repr__(self):
        return f"Laboratorista('{self.idl}','{self.username}','{self.active}','{self.role}')"

class EquipoLab(db.Model):
    clave = db.Column(db.Integer, primary_key=True, nullable=False)
    marca = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(30), nullable=False)
    serie = db.Column(db.Integer, nullable=False)
    proveedor = db.Column(db.String(50), nullable=False)
    DescripcionC = db.Column(db.String(20), nullable=False)
    DescripcionL = db.Column(db.String(100), nullable=False)
    fecha_adquisicion = db.Column(db.DateTime, nullable=False) #! Date
    garantia = db.Column(db.String(20), nullable=False)
    ubicacion = db.Column(db.String(50), nullable=False)
    mantenimiento = db.Column(db.DateTime, nullable=False) #! Date
    factor_analisis = db.Column(db.Integer, nullable= False)
    medida_factor = db.Column(db.Integer, nullable= False)
    lim_inferior = db.Column(db.Integer, nullable= False)
    lim_superior = db.Column(db.Integer, nullable= False)
    especificacion = db.Column(db.String(100), nullable=False)

    #!ForeignKey
    idl = db.Column(db.Integer, db.ForeignKey('laboratorista.idl'))  



    def __repr__(self):
        return f"Equipo('{self.clave}','{self.marca}','{self.modelo}')"


class Cliente(db.Model):
    idc = db.Column(db.Integer, primary_key=True, nullable=False)
    rfc = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(30), nullable=False)
    apellido = db.Column(db.String(30), nullable=False)
    domicilio = db.Column(db.String(70), nullable=False)
    ncontacto = db.Column(db.String(30), nullable=False)
    factor_analisis = db.Column(db.Integer, nullable=False)
    lim_inferior = db.Column(db.Integer, nullable=False)
    lim_superior = db.Column(db.Integer, nullable=False)
    clave_factor = db.Column(db.Integer, nullable=False)
    medida = db.Column(db.Integer, nullable=False)

    # Relacion a muchos
    ordenes = db.relationship("Orden", backref="cliente")
    certificados = db.relationship("Certificado", backref="cliente")

    

    def __repr__(self):
        return f"Cliente('{self.idc}','{self.rfc}','{self.nombre}')"


class Orden(db.Model):
    norden = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad_solicitada = db.Column(db.Float(), nullable=False) #! Real
    fecha_creada = db.Column(db.DateTime(), nullable=False)
    precio = db.Column(db.Float(), nullable=False) #! Real

    # Llaves foraneas
    idc = db.Column(db.Integer, db.ForeignKey("cliente.idc"))

    # Relacion uno a uno
    certificados = db.relationship("Certificado", backref="orden")


    def __repr__(self):
        return f"Orden('{self.norden}','{self.fecha_creada}')"


class Lote(db.Model):
    idlote = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad = db.Column(db.Float(), nullable=False) #! Real
    inspecciones = db.relationship("Inspeccion", backref="lote")

    def __repr__(self):
        return f"Lote('{self.idlote}','{self.cantidad}')"

class Inspeccion(db.Model):
    idi = db.Column(db.Integer, primary_key=True, nullable=False)
    absorcion = db.Column(db.Float(), nullable=False) # ! Real 
    tiempo_desarrollo = db.Column(db.Float(), nullable=False) # !Real
    estabilidad = db.Column(db.Float(), nullable=False) #! Real
    reblandecimiento = db.Column(db.Float(), nullable=False) #! Real
    qnumber = db.Column(db.Integer(), nullable=False)
    tenacidad = db.Column(db.Float(), nullable=False) #! Real
    extensibilidad = db.Column(db.Float(), nullable=False) #! Real
    configuracion_curva = db.Column(db.Float(), nullable=False) #! Real
    indice_elasticidad = db.Column(db.Float(), nullable=False) #! Real
    fuerza_panadera = db.Column(db.Float(), nullable=False) #! Real


    certificados = db.relationship("Certificado", backref="inspeccion")
    idLote = db.Column(db.Integer, db.ForeignKey("lote.idlote"))



    def __repr__(self):
        return f"Inspeccion('{self.idi}','{self.absorcion}','{self.estabilidad}','{self.qnumber}')"

class Certificado(db.Model):
    ncertificado = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad_solicitada = db.Column(db.Float(), nullable=False)# !Real
    norden = db.Column(db.Integer(), nullable=False)
    cant_total = db.Column(db.Float(), nullable=False) #!Real
    factura = db.Column(db.Integer, nullable=False)
    fecha_envio = db.Column(db.DateTime, nullable=False, default=datetime.now())
    fecha_caducidad = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # Llaves foraneas
    idc = db.Column(db.Integer, db.ForeignKey("cliente.idc"))
    idl = db.Column(db.Integer, db.ForeignKey("laboratorista.idl"))

    # Relacion uno a uno orden
    norden = db.Column(db.Integer, db.ForeignKey("orden.norden"))

     # Relacion uno a uno inspeccion
    idi = db.Column(db.Integer, db.ForeignKey("inspeccion.idi"))
    
    def __repr__(self):
        return f"Certificado('{self.ncertificado}','{self.norden}','{self.factura}','{self.cant_total}')"