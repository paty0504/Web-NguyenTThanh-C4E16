from models.service import Customer
import mlab
mlab.connect()
all_customer = Customer.objects()
print(all_customer[100].name)
