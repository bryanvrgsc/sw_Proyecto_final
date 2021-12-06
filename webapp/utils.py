from webapp.dictionaries import *
from flask import request

def getObject(id, elemento):
    table = TableValues(elemento)
    table_header = table['table_header']
    filter = {table_header[0] : id}
    object = table['model'].query.filter_by(**filter).first()
    return object


def getFirstUrl():
    url = str(request.path)
    url = url.split('/')[1]
    return url


def getLastId(Table):
    obj = Table().query.all()
    return obj[-1]
    

def whichFar(certificado):
    values = dict()
    if certificado.orden.cliente.personalizado_far == True:
        return certificado.orden.cliente.farinografo
    else:
        return universal("farinografo")

def whichAlv(certificado):
    values = dict()
    if certificado.orden.cliente.personalizado_alv == True:
        return certificado.orden.cliente.alveografo
    else:
        return universal("alveografo")