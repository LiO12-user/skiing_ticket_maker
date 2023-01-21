from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("home.html")

num1 = 0
num2 = 0

def print_something(val):
    print(val)

def make_int(data):
    new_data = int(data)
    return new_data

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        sum = make_int(request.form["num1"]) + make_int(request.form["num2"])
        print(sum)


    return render_template("service.html")



@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run()