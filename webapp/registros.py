from webapp.forms import *
from webapp import db, bcrypt
from flask_login import current_user
from webapp.utils import *

def regOrden(form):
    orden = Orden(cantidad_solicitada=form.cantidad_solicitada.data, fecha_creada=form.fecha_creada.data, precio=form.precio.data)
    return orden

def regFarinografo(form):
    farinografo = Farinografo(absorcion_agua=form.absorcion_agua.data, tolerancia_ub=form.tolerancia_ub.data, elasticidad=form.elasticidad.data, viscodidad=form.viscodidad.data, act_enzimatica=form.act_enzimatica.data, trigo_germinado=form.trigo_germinado.data, tiempo_amasado=form.tiempo_amasado.data, cantidad_gluten=form.cantidad_gluten.data, calidad_gluten=form.calidad_gluten.data, indoneidad=form.indoneidad.data, dureza=form.dureza.data, reblandecimiento=form.reblandecimiento.data, estabilidad=form.estabilidad.data, tiempo_desarrollo=form.tiempo_desarrollo.data,qnumber=form.qnumber.data)
    return farinografo

def regAlveografo(form):
    alveografo = Alveografo(tenacidad=form.tenacidad.data, extensibilidad=form.extensibilidad.data, fuerza_panadera=form.fuerza_panadera.data, indice_elasticidad=form.indice_elasticidad.data, configuracion_curva=form.configuracion_curva.data) 
    return alveografo

def regLaboratorista(form):
    if form.password.name =="password":
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = Laboratorista(username=form.username.data, password=hashed_password, role=form.role.data, active=form.active.data)
    db.session.add(user)
    db.session.commit()
    return{"message": f"El usuario {user.username} ha sido registrado con exito" , "type": "success"}

def regEquipo(form):
    equipo = EquipoLab(marca=form.marca.data, modelo=form.modelo.data, serie=form.serie.data, proveedor=form.proveedor.data, fecha_adquisicion=form.fecha_adquisicion.data, garantia=form.garantia.data, ubicacion=form.ubicacion.data, mantenimiento=form.mantenimiento.data, descripcionc=form.descripcionc.data, descripcionl=form.descripcionl.data)


    if form.tipo.data == "alv":
        alveografo = regAlveografo(form.alveografo)
        db.session.add(alveografo)
        new_alv_id = str(getLastId(Alveografo).id_alv)
        equipo.id_alv = new_alv_id
    elif form.tipo.data == "far":
        farinografo = regFarinografo(form.farinografo)
        db.session.add(farinografo)
        new_far_id =  str(getLastId(Farinografo).id_far)
        equipo.id_far = new_far_id

    db.session.add(equipo)
    db.session.commit()
    return{"message": f"El equipo {equipo.marca} ha sido registrado con exito" , "type": "success"}
    
def regCliente(form):
    cliente = Cliente(rfc=form.rfc.data, nombre=form.nombre.data, apellido=form.apellido.data, domicilio=form.domicilio.data, ncontacto=form.ncontacto.data, personalizado_far=form.personalizado_far.data, personalizado_alv=form.personalizado_alv.data)

    if cliente.personalizado_alv == True:
        alveografo = regAlveografo(form.alveografo)
        db.session.add(alveografo)
        new_alv_id = str(getLastId(Alveografo).id_alv)
        cliente.id_alv = new_alv_id


    if cliente.personalizado_far == True:
        farinografo = regFarinografo(form.farinografo)
        db.session.add(farinografo)
        new_far_id =  str(getLastId(Farinografo).id_far)
        cliente.id_far = new_far_id

    db.session.add(cliente)
    db.session.commit()

    return{"message": f"{cliente.nombre} ha sido registrado con exito" , "type": "success"}

def regLote(form):
    lote = Lote(cantidad=form.cantidad.data) 
    return lote

def regInspeccion(form, l_nuevo = "no"):
    # Registro de campos basicos en inspeccion
    inspeccion = Inspeccion(id_inspeccion=form.id_inspeccion.data, clave_alv=form.equipo_alv.data, clave_far=form.equipo_far.data)

    # creacion de alveofrafo y farinografo nuevo
    alveografo = regAlveografo(form.alveografo)
    db.session.add(alveografo)
    new_alv_id = str(getLastId(Alveografo).id_alv)
    inspeccion.id_alv = new_alv_id
    farinografo = regFarinografo(form.farinografo)
    db.session.add(farinografo)
    new_far_id =  str(getLastId(Farinografo).id_far)
    inspeccion.id_far = new_far_id

    
    # asignacion del campo lote
    if l_nuevo == "no":
        # select:  Se selecciona el campo de select en el formulario y se guarda en la base
        inspeccion.idlote = form.loteSelect.data
    else:
        # Formulario: Se crea un nuevo lote y se adquire su id para agregarlo a la base
        lote = regLote(form.loteForm)
        db.session.add(lote)
        new_lote_id = str(getLastId(Lote).idlote)
        inspeccion.idlote = new_lote_id

    db.session.add(inspeccion)
    db.session.commit()
    return{"message": f"{inspeccion.id_inspeccion} ha sido registrada con exito" , "type": "success"}

def regCertificado(form):

    certificado = Certificado(
                                
                                factura=form.factura.data,
                                fecha_envio=form.fecha_envio.data,
                                fecha_caducidad=form.fecha_caducidad.data,
                                idi=form.inspeccion.data,
                                idl=current_user.idl,
                                norden=form.orden.data

                                )

    db.session.add(certificado)
    db.session.commit()

    return {'message': f'El certificado con factura: {certificado.factura} ha sido registrado', 'type': 'info'}
