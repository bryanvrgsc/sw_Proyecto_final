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



def setCertificado():
    pass
def setInspeccion():
    pass

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

    