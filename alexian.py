from flask import Flask
app = Flask(__name__)

@app.route("/four")
def hello():
    return "site par Alexian et Sylvain"

if __name__ == "__main__":
    app.run(port=8080)
