
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello ! "

@app.route("/hello/<name>")
def hello_name(name):
    return render_template('hello.html', hi = name)
    # render_template(hello.html, hi = pooja)

if __name__ == "__main__":
    app.run(debug = True)
