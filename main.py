from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?X=<input>\n'

if __name__ == "__main__":
    app.run()
