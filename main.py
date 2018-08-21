from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\nOperation/Value1/Value2>'


if __name__ == "__main__":
    app.run()
