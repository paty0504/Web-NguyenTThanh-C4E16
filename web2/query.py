from models.service import Customer
import mlab

mlab.connect()
id_to_find = '5ac2419571305f3720b19f3c'
# kieu_anh = Customer.objects.get(id=id_to_find)
service = Customer.objects.with_id(id_to_find)
if service is None:
    print('service not found')
else:
    # print(linh_ka.to_mongo())
    service.update(set__gender=1)
    service.reload()
    print(service.gender)
