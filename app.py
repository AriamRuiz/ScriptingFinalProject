from flask import Flask
from database.__init__ import conn
from views.user_view import user
from views.verb_view import verb
#pip install flask

app = Flask(__name__)

print(conn.database)

app.register_blueprint(user)
app.register_blueprint(verb)

@app.route("/")
def index():
    return "HOME"


if __name__ == "__main__":
    app.run()

#flask --app app run