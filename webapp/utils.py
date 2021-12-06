from webapp.dictionaries import TableValues
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


    