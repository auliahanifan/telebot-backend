import datetime
from peewee import MySQLDatabase, Model, CharField, DateTimeField
from config import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER

db = MySQLDatabase(DB_DATABASE, user=DB_USER, password=DB_PASSWORD,
                         host=DB_HOST, port=DB_PORT)

class Chat(Model):
    id = CharField(primary_key=True)
    timestamp = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db
