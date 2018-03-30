from flask import Flask
app = Flask(__name__)
@app.route('/<int:num1>/<int:num2>')
def sum(num1, num2,):
    sum = str(num1 + num2)
    return sum
if __name__ == '__main__':
  app.run( debug=True)
  
