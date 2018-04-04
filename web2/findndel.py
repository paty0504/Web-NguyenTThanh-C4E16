from models.service import Customer
import mlab
mlab.connect()

cus = Customer.objects.get(id='5ac2421f71305f05c86ec887')
cus.delete()
