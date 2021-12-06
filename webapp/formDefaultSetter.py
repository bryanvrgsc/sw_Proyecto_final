from webapp.forms import *
from webapp.utils import *

def setLaboratorista(id, elemento):
    lab = getObject(id, elemento)
    form = RegiseterLab(role= lab.role)
    return form

def setCliente(id, elemento):
    form = RegisterCliente()
    return form

def setEquipo(id,elemento):
    equipo = getObject(id, elemento)
    if equipo.id_far == None:
        tipo = "alv"
    else:
        tipo = "far"
    form = RegisterEquipo(tipo=tipo, descripcionl=equipo.descripcionl)
    return form

def setInspeccion(id, elemento, l_nuevo):
    certificado = getObject(id, elemento)
    if l_nuevo == 'no':
        form = RegisterInspeccionNo(equipo_alv=certificado.clave_alv, equipo_far=certificado.clave_far, loteSelect=certificado.idlote)
    else:
        form = RegisterInspeccionSi(equipo_alv=certificado.clave_alv, equipo_far=certificado.clave_far)


    return form

def setCertificado(id, elemento):
    certificado = getObject(id, elemento)
    form = RegisterCertificado(inspeccion=certificado.idi, orden=certificado.norden)
    return form
    

def updateForms(elemento):
    if elemento == "laboratorista":
        return setLaboratorista
    elif elemento == "clientes":
        return setCliente
    elif elemento == "equipo":
        return setEquipo
    elif elemento == "certificados":
        return setCertificado
    elif elemento == "inspeccion":
        return setInspeccion
    else:
        return {'error message' : 'Query Invalido', 'type':'alert'}

    