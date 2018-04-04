from models.service import  Customer
import mlab
from faker import Faker
from random import randint,choice

mlab.connect()

fake = Faker()

# for i in range(100):
#     print('Saving service', i + 1, '.........')
# new_customer = Customer(name=fake.name(), gender=randint(0,1),phone=fake.phone_number(),company=fake.company(), contacted=choice([True, False], job=fake.job())
# new_customer.save()
for i in range(100):
    print('Saving customer', i + 1, "...")
    new_customer = Customer(name=fake.name(), gender=randint(0,1),phone=fake.phone_number(), contacted=choice([True, False],job=fake.job(), company=fake.company())
    new_customer.save()
