from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/div')
def division():
    try:
        value1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value1='None'
    try:
        value2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value2='None'
    if value1 == 'None' or value2 == 'None' :
        return 'None'
    else:
        val_1 = Fraction(value1)
        val_2 = Fraction(value2)
        try:
            result = val_1/val_2
            return str(float(result))
        except ZeroDivisionError as error:
            return 'None'


if __name__ == "__main__":
    app.run()
