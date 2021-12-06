from webapp.models import *

def TableValues(elemento):

    if elemento == "laboratorista":
        return {'uncalled': Laboratorista,'model' : Laboratorista(), 'search_item' : 'username', 'table_header' : Laboratorista.__table__.columns.keys(), 'breakpoint': None}
    elif elemento == "clientes":
        return {'uncalled': Cliente,'model' : Cliente(), 'search_item' : 'rfc', 'table_header' : Cliente.__table__.columns.keys() , 'breakpoint': 'personalizado_far'}
    elif elemento == "equipo":
        return {'uncalled': EquipoLab,'model' : EquipoLab(),'search_item' : 'clave', 'table_header' : EquipoLab.__table__.columns.keys() , 'breakpoint': 'descripcionl'}
    elif elemento == "certificados":
        return {'uncalled': Certificado,'model' : Certificado(), 'search_item' : 'ncertificado', 'table_header' : Certificado.__table__.columns.keys() , 'breakpoint': 'idl'}
    elif elemento == "inspeccion":
        return {'uncalled': Inspeccion,'model' : Inspeccion(),'search_item' : 'idi', 'table_header' : Inspeccion.__table__.columns.keys() , 'breakpoint': None}
    else:
        return {'error message' : 'Query Invalido', 'type':'alert'}


def universal(equipo):
    if equipo == "farinografo":
        class unidades():
              absorcion_agua= '51.6–63.4 ml/100g'
              tolerancia_ub= '20 - 28 '
              elasticidad= ''
              viscodidad= ''
              act_enzimatica= ''
              trigo_germinado= '60 - 75'
              tiempo_amasado= ''
              cantidad_gluten= ''
              calidad_gluten= ''
              indoneidad= ''
              dureza= '54-145 FU'
              reblandecimiento= ' '
              estabilidad= '4.45–11.20 min'
              tiempo_desarrollo= '8.3 - 9.3 min'
              qnumber= '24 - 125'
                
    if equipo == "alveografo":
        class unidades():
            tenacidad= '45'
            extensibilidad= '71.96'
            fuerza_panadera= '60'
            indice_elasticidad= '47'
            configuracion_curva= '0.99'
    
    return unidades