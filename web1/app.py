from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') #tại địa chỉ server ==> trang chủ
def index():#function . Khi người dùng vào đường dẫn thì chạy hàm index

    # post_title = 'THơ con ếch'
    # post_content = '????'
    # post_author = 'Thanh'


    posts = [
    {'title' : 'Tho con ech',
    'content' : '???',
    'gender' : 1,
    'author' : 'Thanh',},

    {    'title' : 'Tho con coc',
    'content' : '...',
    'gender' : 1,
    'author' : 'Thanh1',},

    {'title' : 'Không biết làm thơ',
    'content' : 'Chịu',
    'gender' : 0,
    'author' : 'Hồng Anh'

    }

    ]

    return render_template('index.html',posts=posts)
@app.route('/hello')
def hello():
    return "Hello C4E 16"
@app.route('/sayhi/<name>/<age>')
def hi(name, age):
    return "Hi " + name + "You're " + age

if __name__ == '__main__':
  app.run( debug=True)   #khi file này chạy trực tiếp thì chạy
 #debug = True: mỗi lần sửa code thì tự động cập nhật lại
