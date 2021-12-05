from webapp.forms import *
from webapp.models import *
from webapp.registros import *


def TableValues(elemento):

    if elemento == "laboratorista":
        return {'uncalled': Laboratorista,'model' : Laboratorista(), 'search_item' : 'username', 'table_header' : Laboratorista.__table__.columns.keys(), 'breakpoint': None, 'registro': regLaboratorista}
    elif elemento == "clientes":
        return {'uncalled': Cliente,'model' : Cliente(), 'search_item' : 'rfc', 'table_header' : Cliente.__table__.columns.keys() , 'breakpoint': 'personalizado_far', 'registro': regCliente}
    elif elemento == "equipo":
        return {'uncalled': EquipoLab,'model' : EquipoLab(),'search_item' : 'clave', 'table_header' : EquipoLab.__table__.columns.keys() , 'breakpoint': 'descripcionl', 'registro': regEquipo}
    elif elemento == "certificados":
        return {'uncalled': Certificado,'model' : Certificado(), 'search_item' : 'ncertificado', 'table_header' : Certificado.__table__.columns.keys() , 'breakpoint': 'idl', 'registro': regCertificado}
    elif elemento == "inspeccion":
        return {'uncalled': Inspeccion,'model' : Inspeccion(),'search_item' : 'idi', 'table_header' : Inspeccion.__table__.columns.keys() , 'breakpoint': None, 'registro': regInspeccion}
    else:
        return {'error message' : 'Query Invalido', 'type':'alert'}
