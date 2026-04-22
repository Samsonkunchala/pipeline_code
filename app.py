from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Good job thokka ivvi odhu isthe mudhu ivvu intha kastapadda!!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
