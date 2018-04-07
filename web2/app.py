import mlab
from flask import *
from mongoengine import *
from faker import Faker
from random import randint,choice
fake = Faker()
# from models.customer import Customer
app = Flask(__name__)
mlab.connect()
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0: female, 1:male
    img = StringField()
    phone = StringField()
    height = IntField()
    address = StringField()
    # status = BooleanField()
    measurements = ListField()
    description = ListField()
#
# service1 = Service(name='Tú Linh', phone='01699696969', address='Hà Nội', height='163', yob='1990', measurements=[90, 60, 90], description=["ngoan hiền", "dễ thương", "lễ phép với gia đình", ], img="static/image/tulinh.jpg " )
# service1.save()
# service2 = Service(name='Linh Ka', phone='0987654321', address='Hà Nội', height='150', yob='2002', measurements=[70, 60, 70], description=['Hot teen 2017!', ],img='static/image/linka.jpg')
# service2.save()
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
@app.route('/admin')
def admin():
    all_services = Service.objects()
    return render_template('admin.html', services=all_services)
@app.route('/delete/<service_id>')
def delete(service_id):
    delete_service = Service.objects.get(id=service_id)
    if delete_service is None:
        return "Not found"
    else:
        delete_service.delete()
        return redirect(url_for('admin')) #xóa xong quay lại /admin
@app.route('/new-service', methods=['GET', 'POST'])  #khi người dùng vào route cho phép 2 request là get và post
def create():
    if request.method == 'GET':
        return render_template('new-service.html')   #Nếu gửi get thì trả form

    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']  #lấy ra các thông tin từ form
        new_service = Service(name=name, yob=yob, address=address)
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/service')
def service():
    services=Service.objects()
    return render_template('service.html', services=services )
@app.route('/detail/<service_id>')
def detail(service_id):
    detail_service = Service.objects.get(id=service_id)
    return render_template('detail.html', detail_service=detail_service)

@app.route('/update/<service_id>', methods=['GET', 'POST'])
def update(service_id):
    service_update = Service.objects.get(id=service_id)
    if request.method == 'GET':
        return render_template('update.html', service_update=service_update)
    elif request.method == 'POST':
        form = request.form
        service_update.update(set__name = form['name'],
                            set__yob = form['yob'],
                            set__gender = form['gender'],
                            set__height = form['height'],
                            set__address = form["address"],
                            set__phone = form['phone'])
        # service_update.reload()
        return redirect(url_for('service'))

if __name__ == '__main__':
  app.run( debug=True)
