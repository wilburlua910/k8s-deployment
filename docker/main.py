from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    sucess_msg = "Your Kubernetes deployment is successful!"
    return render_template("index.html", message=sucess_msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)