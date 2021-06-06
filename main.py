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
        Error_msg = "Please enter inputs properly not in p/q form"
        return Error_msg


@app.route('/min')
def minimum():
    values = yeshw()
    if not type(values) is str:
        values.sort()
        if values[0].is_integer():
            return str(int(values[0]))
        else:
            return str(float(round(values[0], 1)))
    else:
        return values


if __name__ == "__main__":
    app.run()
