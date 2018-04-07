from mongoengine import *

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0: female, 1:male

    phone = StringField()
    contacted = BooleanField()
    address = StringField()
    status = BooleanField()
