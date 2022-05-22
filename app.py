from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>¡Hola, Mundo!</p>"


if __name__ == "pyduo":
    app.run(debug=True)