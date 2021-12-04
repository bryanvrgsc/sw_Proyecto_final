from webapp import db
from webapp.models import Lote, Laboratorista, EquipoLab, Farinografo, Alveografo, Cliente, Orden, Inspeccion, Certificado


db.create_all()

db.session.commit()

