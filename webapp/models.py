from datetime import datetime
from sqlalchemy.orm import backref, column_property, defaultload, lazyload
from webapp import db, login_manager
from flask_login import UserMixin

# id_far = db.Column(db.Integer, db.ForeignKey("farinografo.id_far"))
# certificados = db.relationship("Certificado", backref="inspeccion")

@login_manager.user_loader
def load_user(user_id):
    return Laboratorista.query.get(int(user_id))

class Laboratorista(db.Model, UserMixin):
    idl = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    active = db.Column(db.Boolean, nullable=False) 

    #! Relationship
    equipolab = db.relationship("EquipoLab", backref="laboratorista")
    certificado = db.relationship("Certificado", backref="laboratorista")


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
    fecha_adquisicion = db.Column(db.DateTime, nullable=False) 
    garantia = db.Column(db.DateTime, nullable=False)
    ubicacion = db.Column(db.String(50), nullable=False)
    mantenimiento = db.Column(db.DateTime, nullable=False) 
    descripcionc = db.Column(db.String(20), nullable=False)
    descripcionl = db.Column(db.String(100), nullable=False)

    #! Relationship
    inspeccion = db.relationship("Inspeccion", backref="equipolab")

    #!Foranea
    idl = db.Column(db.Integer, db.ForeignKey("laboratorista.idl"))
    id_far = db.Column(db.Integer, db.ForeignKey("farinografo.id_far"))
    id_alv = db.Column(db.Integer, db.ForeignKey("alveografo.id_alv"))



    def __repr__(self):
        return f"Equipo('{self.clave}','{self.marca}','{self.modelo}')"

class Farinografo(db.Model):
    id_far = db.Column(db.Integer, primary_key=True, nullable=False)
    # Farinografo
    absorcion_agua = db.Column(db.String(20), nullable=False)
    tolerancia_ub = db.Column(db.String(20), nullable=False)
    elasticidad = db.Column(db.String(20), nullable=False)
    viscodidad = db.Column(db.String(20), nullable=False)
    act_enzimatica = db.Column(db.String(20), nullable=False)
    trigo_germinado = db.Column(db.String(20), nullable=False)
    tiempo_amasado = db.Column(db.String(20), nullable=False)
    cantidad_gluten = db.Column(db.String(20), nullable=False)
    calidad_gluten = db.Column(db.String(20), nullable=False)
    indoneidad = db.Column(db.String(20), nullable=False)
    dureza = db.Column(db.String(20), nullable=False)
    reblandecimiento = db.Column(db.String(20), nullable=False) 
    estabilidad = db.Column(db.String(20), nullable=False)
    tiempo_desarrollo = db.Column(db.String(20), nullable=False)  
    qnumber = db.Column(db.String(20), nullable=False)

    #! Relationship
    inspeccion = db.relationship("Inspeccion", backref="farinografo")
    equipolab = db.relationship("EquipoLab", backref="farinografo")
    cliente = db.relationship("Cliente", backref="farinografo")
 

class Alveografo(db.Model):
    id_alv = db.Column(db.Integer, primary_key=True, nullable=False)
    # Alveografo
    tenacidad = db.Column(db.String(20), nullable=False)
    extensibilidad = db.Column(db.String(20), nullable=False)
    fuerza_panadera = db.Column(db.String(20), nullable=False)
    indice_elasticidad = db.Column(db.String(20), nullable=False)
    configuracion_curva = db.Column(db.String(20), nullable=False)

    #! Relationship
    equipolab = db.relationship("EquipoLab", backref="alveografo")
    inspeccion = db.relationship("Inspeccion", backref="alveografo")
    cliente = db.relationship("Cliente", backref="alveografo")

class Cliente(db.Model):
    idc = db.Column(db.Integer, primary_key=True, nullable=False)
    rfc = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(30), nullable=False)
    apellido = db.Column(db.String(30), nullable=False)
    domicilio = db.Column(db.String(70), nullable=False)
    ncontacto = db.Column(db.String(30), nullable=False)
    # Pesonalizado
    personalizado_far = db.Column(db.Boolean, nullable=False)
    personalizado_alv = db.Column(db.Boolean, nullable=False)

    #!Foranea
    id_far = db.Column(db.Integer, db.ForeignKey("farinografo.id_far"))
    id_alv = db.Column(db.Integer, db.ForeignKey("alveografo.id_alv"))

    #! Relationship
    orden = db.relationship("Orden", backref="cliente")
    
    def __repr__(self):
        return f"Cliente('{self.idc}','{self.rfc}','{self.nombre}')"


class Orden(db.Model):
    norden = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad_solicitada = db.Column(db.Float(), nullable=False) 

    fecha_creada = db.Column(db.DateTime(), nullable=False)
    precio = db.Column(db.Float(), nullable=False) 

    #! Relationship
    certificado = db.relationship("Certificado", backref="orden")

    #!Foranea
    idc = db.Column(db.Integer, db.ForeignKey("cliente.idc"))

    def __repr__(self):
        return f"Orden('{self.norden}','{self.fecha_creada}')"


class Lote(db.Model):
    idlote = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad = db.Column(db.Float(), nullable=False) 
    
    #! Relationship
    inspeccion = db.relationship("Inspeccion", backref="lote")

    def __repr__(self):
        return f"Lote('{self.idlote}','{self.cantidad}')"

class Inspeccion(db.Model):
    idi = db.Column(db.Integer, primary_key=True, nullable=False)
    id_inspeccion = db.Column(db.Integer, nullable=False)
    
    #! Relationship
    certificado = db.relationship("Certificado", backref="inspeccion")

    #!Foranea
    clave = db.Column(db.Integer, db.ForeignKey("equipo_lab.clave"))
    id_far = db.Column(db.Integer, db.ForeignKey("farinografo.id_far"))
    id_alv = db.Column(db.Integer, db.ForeignKey("alveografo.id_alv"))
    idlote = db.Column(db.Integer, db.ForeignKey("lote.idlote"))


    def __repr__(self):
        return f"Inspeccion('{self.idi}','{self.absorcion}','{self.estabilidad}','{self.qnumber}')"

class Certificado(db.Model):
    ncertificado = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad_solicitada = db.Column(db.Float(), nullable=False)
    cant_total = db.Column(db.Float(), nullable=False) 
    factura = db.Column(db.Integer, nullable=False)
    fecha_envio = db.Column(db.DateTime, nullable=False, default=datetime.now())
    fecha_caducidad = db.Column(db.DateTime, nullable=False, default=datetime.now())

    #!Foranea
    idl = db.Column(db.Integer, db.ForeignKey("laboratorista.idl"))
    idi = db.Column(db.Integer, db.ForeignKey("inspeccion.idi"))
    norden = db.Column(db.Integer, db.ForeignKey("orden.norden"))

    
    def __repr__(self):
        return f"Certificado('{self.ncertificado}','{self.norden}','{self.factura}','{self.cant_total}')"