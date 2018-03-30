from flask import Flask, render_template, redirect
app = Flask(__name__)
@app.route('/about_me')
def about_me():
    my_self = {
    'name' : 'Nguyễn Tiến Thành',
    'age' : '19',
    'university' : 'HUST',
    'hobbies' : 'gaming, books, surfing web, movies',

    }
    return render_template ('index1.html', posts=my_self)
@app.route('/school')
def link():
    return redirect("http://techkids.vn/")

if __name__ == '__main__':
    app.run( debug=True)
