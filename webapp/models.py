 from datetime import datetime
from sqlalchemy.orm import backref, column_property, defaultload, lazyload
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


    #!ForeignKey
    idl = db.Column(db.Integer, db.ForeignKey('laboratorista.idl'))  


    def __repr__(self):
        return f"Equipo('{self.clave}','{self.marca}','{self.modelo}')"

class Farinografo(db.Model):
    id_far = db.Column(db.Integer, primary_key=True, nullable=False)
    # Farinografo
    absorcion_agua_sup = db.Column(db.Float(), nullable=False)
    absorcion_agua_inf = db.Column(db.Float(), nullable=False)
    absorcion_agua = db.Column(db.Float(), nullable=False)
    tolerancia_ub_sup = db.Column(db.Float(), nullable=False)
    tolerancia_ub_inf = db.Column(db.Float(), nullable=False)
    tolerancia_ub = db.Column(db.Float(), nullable=False)
    elasticidad_sup = db.Column(db.Float(), nullable=False)
    elasticidad_inf = db.Column(db.Float(), nullable=False)
    elasticidad = db.Column(db.Float(), nullable=False)
    viscodidad_sup = db.Column(db.Float(), nullable=False)
    viscodidad_inf = db.Column(db.Float(), nullable=False)
    viscodidad = db.Column(db.Float(), nullable=False)
    act_enzimatica_sup = db.Column(db.Float(), nullable=False)
    act_enzimatica_inf = db.Column(db.Float(), nullable=False)
    act_enzimatica = db.Column(db.Float(), nullable=False)
    trigo_germinado_sup = db.Column(db.Float(), nullable=False)
    trigo_germinado_inf = db.Column(db.Float(), nullable=False)
    trigo_germinado = db.Column(db.Float(), nullable=False)
    tiempo_amasado_sup = db.Column(db.Float(), nullable=False)
    tiempo_amasado_inf = db.Column(db.Float(), nullable=False)
    tiempo_amasado = db.Column(db.Float(), nullable=False)
    cantidad_gluten_sup = db.Column(db.Float(), nullable=False)
    cantidad_gluten_inf = db.Column(db.Float(), nullable=False)
    cantidad_gluten = db.Column(db.Float(), nullable=False)
    calidad_gluten_sup = db.Column(db.Float(), nullable=False)
    calidad_gluten_inf = db.Column(db.Float(), nullable=False)
    calidad_gluten = db.Column(db.Float(), nullable=False)
    indoneidad_sup = db.Column(db.Float(), nullable=False)
    indoneidad_inf = db.Column(db.Float(), nullable=False)
    indoneidad = db.Column(db.Float(), nullable=False)
    dureza_sup = db.Column(db.Float(), nullable=False)
    dureza_inf = db.Column(db.Float(), nullable=False)
    dureza = db.Column(db.Float(), nullable=False)
    reblandecimiento_sup = db.Column(db.Float(), nullable=False)
    reblandecimiento_inf = db.Column(db.Float(), nullable=False)
    reblandecimiento = db.Column(db.Float(), nullable=False) 
    estabilidad_sup = db.Column(db.Float(), nullable=False)
    estabilidad_inf = db.Column(db.Float(), nullable=False)
    estabilidad = db.Column(db.Float(), nullable=False)
    tiempo_desarrollo = db.Column(db.Float(), nullable=False) 
    tiempo_desarrollo_sup = db.Column(db.Float(), nullable=False) 
    tiempo_desarrollo_inf = db.Column(db.Float(), nullable=False) 
    qnumber_sup = db.Column(db.Integer(), nullable=False)
    qnumber_inf = db.Column(db.Integer(), nullable=False)
    qnumber = db.Column(db.Integer(), nullable=False)

    cliente = db.relationship("Cliente", backref="farinografo")
    inspeccion = db.relationship("Inspeccion", backref="farinografo")
 

class Alveografo(db.Model):
    id_alv = db.Column(db.Integer, primary_key=True, nullable=False)
    # Alveografo
    tenacidad_sup = db.Column(db.Float(), nullable=False)
    tenacidad_inf = db.Column(db.Float(), nullable=False)
    tenacidad = db.Column(db.Float(), nullable=False)
    extensibilidad_sup = db.Column(db.Float(), nullable=False)
    extensibilidad_inf = db.Column(db.Float(), nullable=False)
    extensibilidad = db.Column(db.Float(), nullable=False)
    fuerza_panadera_sup = db.Column(db.Float(), nullable=False)
    fuerza_panadera_inf = db.Column(db.Float(), nullable=False)
    fuerza_panadera = db.Column(db.Float(), nullable=False)
    indice_elasticidad_sup = db.Column(db.Float(), nullable=False)
    indice_elasticidad_inf = db.Column(db.Float(), nullable=False)
    indice_elasticidad = db.Column(db.Float(), nullable=False)
    configuracion_curva = db.Column(db.Float(), nullable=False)

    cliente = db.relationship("Cliente", backref="alveografo")
    inspeccion = db.relationship("Inspeccion", backref="alveografo")

 

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

    # Llaves foraneas
    id_far = db.Column(db.Integer, db.ForeignKey("farinografo.id_far"))
    id_alv = db.Column(db.Integer, db.ForeignKey("alveogrado.id_alv"))

    # Relacion a muchos
    
    ordenes = db.relationship("Orden", backref="cliente")
    certificados = db.relationship("Certificado", backref="cliente")

    
    def __repr__(self):
        return f"Cliente('{self.idc}','{self.rfc}','{self.nombre}')"


class Orden(db.Model):
    norden = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad_solicitada = db.Column(db.Float(), nullable=False) 
    # idc = db.Column(db.Integer, nullable=False)
    fecha_creada = db.Column(db.DateTime(), nullable=False)
    precio = db.Column(db.Float(), nullable=False) 

    # Llaves foraneas
    idc = db.Column(db.Integer, db.ForeignKey("cliente.idc"))

    # Relacion uno a uno
    certificados = db.relationship("Certificado", backref="orden")


    def __repr__(self):
        return f"Orden('{self.norden}','{self.fecha_creada}')"


class Lote(db.Model):
    idlote = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad = db.Column(db.Float(), nullable=False) 
    inspecciones = db.relationship("Inspeccion", backref="lote")

    def __repr__(self):
        return f"Lote('{self.idlote}','{self.cantidad}')"

class Inspeccion(db.Model):
    idi = db.Column(db.Integer, primary_key=True, nullable=False)

    certificados = db.relationship("Certificado", backref="inspeccion")
    idLote = db.Column(db.Integer, db.ForeignKey("lote.idlote"))

    # Llaves foraneas
    id_far = db.Column(db.Integer, db.ForeignKey("farinografo.id_far"))
    id_alv = db.Column(db.Integer, db.ForeignKey("alveogrado.id_alv"))

    def __repr__(self):
        return f"Inspeccion('{self.idi}','{self.absorcion}','{self.estabilidad}','{self.qnumber}')"

class Certificado(db.Model):
    ncertificado = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad_solicitada = db.Column(db.Float(), nullable=False)
    norden = db.Column(db.Integer(), nullable=False)
    cant_total = db.Column(db.Float(), nullable=False) 
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