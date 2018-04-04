import mlab
from flask import Flask, render_template
from mongoengine import *
from faker import Faker
from random import randint,choice
fake = Faker()
# from models.customer import Customer
app = Flask(__name__)
mlab.connect()
class Customer(Document):
    name = StringField()

    gender = IntField() #0: female, 1:male

    phone = StringField()
    contacted = BooleanField()
    job = StringField()
    company = StringField()

#create collection
#design database
# for i in range(50):
#     print('Saving customer inf', i+1, '........')
#     new_customer = Customer(name=fake.name(), gender=randint(0,1),phone=fake.phone_number(), contacted=choice([True, False],job=fake.job(), company=fake.company())
#     new_customer.save()

#create a document
# for i in range(50):
#     print('Saving.......', i+1)
#     new_customer = Customer(name=fake.name(), job=fake.job(), gender=randint(0,1),phone=fake.phone_number(), contacted=choice([True,False]) )
#     new_customer.save()


@app.route('/customer')
def index():
    all_customer = Customer.objects()
    return render_template('search.html', all_customer=all_customer)
@app.route('/uncontacted')
def ucc():
    uc_cus = Customer.objects(gender=1, contacted=False)
    # uc_cus.limit(10)
    return render_template('search.html',all_customer=uc_cus.limit(10))
# @app.route('/search/<int:gender>')
# def search(gender):
#     all_services = Service.objects(gender=gender, yob__lte=1998, address__icontains='Ha Noi') #find all object with yob <= 1998,address: Ha Noi
#
#     return render_template('search.html', all_services=all_services)

if __name__ == '__main__':
  app.run( debug=True)
