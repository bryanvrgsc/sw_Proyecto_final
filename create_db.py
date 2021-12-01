from webapp import db
from webapp.models import *

db.create_all()

db.session.commit()

