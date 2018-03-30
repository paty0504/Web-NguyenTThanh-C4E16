from flask import Flask
app = Flask(__name__)
@app.route('/<num1>/<num2>/<sum>')
def sum(num1, num2, sum):
    sum = num1 + num2
    return sum
if __name__ == '__main__':
  app.run( debug=True)  
