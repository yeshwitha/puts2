from flask import Flask, request
import statistics

app = Flask(__name__)


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
            return str(int(avrg)) + ' \n'
        else:
            return str(float((avrg))) + ' \n'
    else:
        return values



if __name__ == "__main__":
    app.run()
