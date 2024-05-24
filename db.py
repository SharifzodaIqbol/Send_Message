from peewee import *

db = SqliteDatabase('people.db')

class User(Model):
    id_telegram = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Student(Model):
    user_id = CharField()

    class Meta:
        database = db

class Messages(Model):
    send_message_time = CharField()
    date_time = DateTimeField()

    class Meta:
        database = db
db.connect()
db.create_tables([User, Student, Messages])

