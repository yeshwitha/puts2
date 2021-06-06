from flask import Flask, request
from fractions import Fraction
from decimal import Decimal
import statistics
app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\nOperation?A=<Value1>&B=<Value2>\n'

@app.route('/add')
def addition():
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
        result = val_1+val_2
        return str(float(result))

@app.route('/sub')
def subtraction():
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
        result = val_1-val_2
        return str(float(result))

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

@app.route('/mul')
def multiplication():
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
        result = val_1*val_2
        return str(float(result))

def yeshw():
    try:
        inputs = request.args.get('X', type=str)
        inputs = inputs.split(',')
        values = []
        for value in inputs:
            value = float(value)
            values.append(value)
        return values
    except ValueError:
        Error_msg = "Please enter inputs properly not in p/q form \n"
        return Error_msg


@app.route('/average')
@app.route('/avg')
@app.route('/mean')

def average():
    values = yeshw()
    if not type(values) is str:
        avrg = statistics.mean(values)
        if avrg.is_integer():
            return str(int(avrg))
        else:
            return str(float((avrg)))
    else:
        return values

@app.route('/min')
def minimum():
    values = yeshw()
    if not type(values) is str:
        values.sort()
        if values[0].is_integer():
            return str(int(values[0]))
        else:
            return str(float((values[0])))
    else:
        return values

@app.route('/max')
def maximum():
    values = yeshw()
    if not type(values) is str:
        values.sort(reverse=True)
        if values[0].is_integer():
            return str(int(values[0]))
        else:
            return str(values[0])
    else:
        return values

@app.route('/median')
def median():
    values = yeshw()
    if not type(values) is str:
        avrg = statistics.median(values)
        if avrg.is_integer():
            return str(int(avrg))
        else:
            return str(float((avrg)))
    else:
        return values


if __name__ == "__main__":
    app.run()
