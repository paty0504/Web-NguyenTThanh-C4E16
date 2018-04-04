from models.service import Customer
import mlab
mlab.connect()
id_to_find = '5ac2419171305f14c89e43bb'
cus = Customer.objects.get(id='5ac2421f71305f05c86ec887')
cus.delete()
