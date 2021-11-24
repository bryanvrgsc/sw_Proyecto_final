from datetime import datetime
from sqlalchemy.orm import backref, defaultload, lazyload
from webapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Laboratorista(db.Model, UserMixin):
    idl = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    active = db.Column(db.Boolean, nullable=False) #! Boolean
    role = db.Column(db.String(20), nullable=False)

    # Relation to payment
    payment = db.relationship("Payments", backref="user")


    def __repr__(self):
        return f"User('{self.username}','{self.f_name}','{self.l_name}','{self.mail}','{self.b_date}')"

class EquipoLab(db.Model):
    clave = db.Column(db.Integer, primary_key=True, nullable=False)
    marca = db.Column(db.String(30), nullable=False)
    idl = db.Column(db.Integer, nullable=False, db.ForeignKey('laboratorista.idl')) #!ForeignKey
    modelo = db.Column(db.String(30), nullable=False)
    DescripcionL = db.Column(db.String(100), nullable=False)
    DescripcionC = marca = db.Column(db.String(20), nullable=False)
    serie = db.Column(db.Integer, nullable=False)
    proveedor = db.Column(db.String(50), nullable=False)
    fecha_adquisicion = db.Column(db.DateTime, nullable=False) #! Date
    garantia = db.Column(db.String(20), nullable=False)
    ubicacion = db.Column(db.String(50), nullable=False)
    mantenimiento = db.Column(db.DateTime, nullable=False) #! Date
    factor_analisis = db.Column(db.Integer, nullable= False)
    medida_factor = db.Column(db.Integer, nullable= False)
    lim_inferior = db.Column(db.Integer, nullable= False)
    lim_superior = db.Column(db.Integer, nullable= False)
    especificacion = db.Column(db.String(100), nullable=False)


    # Relation to User
    users = db.relationship("User", backref="program")

    # Relation to Payments
    payments = db.relationship("Payments", backref="program")

    # Foreign Key for Location
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))

    # Relation to Payments
    schedules = db.relationship("Schedule", backref="program")

    # Foreign Key for Location
    coach_id = db.Column(db.Integer, db.ForeignKey("directive.id"))


    def __repr__(self):
        return f"Program('{self.p_name}','{self.start_date}','{self.end_date}')"


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

    # Foreign Key Location
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))

    # Foreign Key Program
    program_id = db.Column(db.Integer, db.ForeignKey("program.id"))

    def __repr__(self):
        return f"Schedule('{self.program_id}','{self.start}','{self.end}')"


class Orden(db.Model):
    norden = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad_solicitada = db.Column(db.Float(), nullable=False) #! Real
    idc = db.Column(db.Integer, nullable=False)
    fecha_creada = db.Column(db.DateTime(), nullable=False)
    precio = db.Column(db.Float(), nullable=False) #! Real

    # Schedule relationship
    schedules = db.relationship("Schedule", backref="event_location")

    # Program relationship
    programs = db.relationship("Program", backref="program_location")

    def __repr__(self):
        return f"Location('{self.name}','{self.location}')"


class Lote(db.Model):
    idlote = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad = db.Column(db.Float(), nullable=False) #! Real
    

    # Program relationship
    programs = db.relationship("Program", backref="Coach")


    def __repr__(self):
        return f"Coach('{self.d_name}','{self.user}','{self.mail}')"

class Inspeccion(db.Model):
    idi = db.Column(db.Integer, primary_key=True, nullable=False)
    absorcion = db.Column(db.Float(), nullable=False) # ! Real 
    idlote = db.Column(db.Integer(), nullable=False)
    tiempo_desarrollo = db.Column(db.Float(), nullable=False) # !Real
    estabilidad = db.Column(db.Float(), nullable=False) #! Real
    reblandecimiento = db.Column(db.Float(), nullable=False) #! Real
    qnumber = db.Column(db.Integer(), nullable=False)
    tenacidad = db.Column(db.Float(), nullable=False) #! Real
    extensibilidad = db.Column(db.Float(), nullable=False) #! Real
    configuracion_curva = db.Column(db.Float(), nullable=False) #! Real
    indice_elasticidad = db.Column(db.Float(), nullable=False) #! Real
    fuerza_panadera = db.Column(db.Float(), nullable=False) #! Real

    # Foreign Key User
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # Foreign Key Program
    program_id = db.Column(db.Integer, db.ForeignKey("program.id"))

    def __repr__(self):
        return f"payments('{self.date}','{self.amount}','{self.user_id}','{self.program_id}')"

class Certificado(db.Model):
    ncertificado = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad_solicitada = db.Column(db.Float(), nullable=False)# !Real
    norden = db.Column(db.Integer(), nullable=False)
    cant_total = db.Column(db.Float(), nullable=False) #!Real
    factura = db.Column(db.Integer, nullable=False)
    fecha_envio = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    fecha_caducidad = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    idc = db.Column(db.Integer(), nullable=False) #! fk
    idi = db.Column(db.Integer(), nullable=False) #! fk
    idl = db.Column(db.Integer(), nullable=False) #! fk
    idlote = db.Column(db.Integer(), nullable=False) #! fk
    
    def __repr__(self):
        return f"payments('{self.date}','{self.amount}','{self.user_id}','{self.program_id}')"