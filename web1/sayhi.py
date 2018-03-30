from flask import Flask
app = Flask(__name__)
@app.route('/')
def hi():
    return "Hi Thanh"
if __name__ == __main__:
    sayhi.run(debug=True)
