from mongoengine import *

class Customer(Document):
    name = StringField()

    gender = IntField() #0: female, 1:male

    phone = StringField()
    contacted = BooleanField()
    job = StringField()
    company = StringField()
