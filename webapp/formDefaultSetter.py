from webapp.forms import *
from webapp.utils import *

def setLaboratorista(id, elemento):
    lab = getObject(id, elemento)
    form = RegiseterLab(role= lab.role)
    return form

    