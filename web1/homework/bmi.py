from flask import Flask, render_template
app = Flask(__name__)
@app.route('/bmi/<int:weight>/<int:height>')
#without render_template:
# def cal_bmi(weight,height):
#     bmi = float(weight/((height/100)*(height/100)))
#
#     if bmi < 16:
#         return str(bmi) + ' Severely underweight'
#     elif bmi < 18.5:
#         return str(bmi) + ' Underweight'
#     elif bmi < 25:
#         return str(bmi) + ' Normal'
#     elif bmi < 30:
#         return str(bmi) + ' Overweight'
#     else:
#         return str(bmi) + ' Obese'
#with render_template:
def cal_bmi2(weight,height):
    bmi = float(weight/((height/100)*(height/100)))
    return render_template('bmical.html', bmi=bmi)
if __name__ == '__main__':
  app.run( debug=True)
