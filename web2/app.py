import mlab
from flask import *
from mongoengine import *
from faker import Faker
from random import randint,choice
from datetime import *
fake = Faker()
# from models.customer import Customer
app = Flask(__name__)
mlab.connect()
app.secret_key = 'a-super-super-secret-key'
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
class User(Document):
    name = StringField()
    password = StringField()
    username = StringField()
    email = EmailField()
class Order(Document):
    service = ReferenceField(Service)
    user = ReferenceField(User)
    time = StringField()
    is_accepted = BooleanField()
# #
# service1 = Service(name='Hera', phone='01699696969', address='Hà Nội', height='160', yob='1990', measurements=[90, 60, 90], description=['Hot girl streamer' ], img="https://znews-photo-td.zadn.vn/w660/Uploaded/ohunua2/2018_02_24/14504835_310918849274454_2855615938546368512_n.jpg" )
# service1.save()
# service2 = Service(name='Cô giáo Thảo', phone='0987654322', address='Cà Mau', height='150', yob='1997', measurements=[70, 60, 80], description=['Love teaching' ],img='https://znews-photo-td.zadn.vn/w660/Uploaded/neg_ysfyrns/2015_11_18/4.jpg')
# service2.save()
# #create collection

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

@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/customer')
# def index_cus():
#     all_customer = Customer.objects()
#     return render_template('search.html', all_customer=all_customer)
# @app.route('/uncontacted')
# def ucc():
#     uc_cus = Customer.objects(gender=1, contacted=False)
#     # uc_cus.limit(10)
#     return render_template('search.html',all_customer=uc_cus.limit(10))
@app.route('/search/<int:gender>')
def search(gender):
    all_services = Service.objects(gender=gender) #find all object with yob <= 1998,address: Ha Noi

    return render_template('search.html', all_services=all_services)
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

    if "logged_in" in session:
        detail_service = Service.objects.get(id=service_id)
        return render_template('detail.html', detail_service=detail_service)
    else:
        session['service_id'] = service_id
        return redirect(url_for('login'))
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        account = User.objects(username=username, password=password).first()
        if account == None:
            return redirect(url_for('login'))
        else:
            session['logged_in'] = str(account['id'])
            return redirect(url_for('detail', service_id=session['service_id']))




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

@app.route('/signin', methods= ['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    if request.method == 'POST':
        form = request.form
        name = form['name']
        email = form['email']
        username = form['username']
        password = form['password']
        new_user = User(name=name, email=email, username=username, password=password)
        new_user.save()
        return redirect(url_for('service'))

@app.route('/order/<service_id>')
def order(service_id):
    user_id = session['logged_in']
    user = User.objects.get(id=user_id)
    service = Service.objects.get(id=service_id)
    time ='{0:%H:%M %d/%m}'.format(datetime.now())

    new_order = Order(service=service,
                      user=user,
                      time=time,
                      is_accepted=False)
    new_order.save()
    return 'Đã gửi yêu cầu!'
@app.route('/order-page')
def order_page():
    all_order = Order.objects(is_accepted=False)
    return render_template('order-page.html', all_order=all_order)
@app.route('/verify-order/<order_id>')
def verify_order(order_id):
    order_to_verify = Order.objects.get(id=order_id)
    order_to_verify['is_accepted'] = True
    order_to_verify.save()
    return "Your request has been verified, we'll contact you soon!"


if __name__ == '__main__':
  app.run( debug=True)
