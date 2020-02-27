from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Automate The Changes will work now because of a syntax ERROR! that I finally found"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
