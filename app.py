from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "nv ignore chesthe mi chelle venuka padtha number ivvu!!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
