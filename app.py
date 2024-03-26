from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LatinoGang'


@app.route('/')
def index():
    return "Hello Team 4, ready to add some verbs???"


if __name__ == '__main__':
    app.run(debug=True)
