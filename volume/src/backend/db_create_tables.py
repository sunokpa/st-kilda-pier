from run import db

from models.token import RevokedToken
from models.account import Account

import sqlalchemy
import os, uuid, base62
from passlib.hash import pbkdf2_sha256 as sha256

DB_HOST = "mysql-skp"
DB_USER = "root"
DB_PW =  os.environ['MYSQL_ROOT_PASSWORD']
DB_NAME = "flask_skp"
DB_ENGINE_URI = "mysql://{}:{}@{}/{}".format(DB_USER, DB_PW, DB_HOST, DB_NAME)

engine = sqlalchemy.create_engine(DB_ENGINE_URI)

def create_table(model):
    try:
        model.__table__.drop(engine)
        model.__table__.create(engine)
    except:
        model.__table__.create(engine)

create_table(RevokedToken)
create_table(Account)

# add Admin
admin = Account()
admin.id = "admin"
admin.pw = sha256.hash("admin")
admin.level = "A"
admin.active = "Y"

db.session.add(admin)
db.session.commit()
