from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', name= "Your Name")

@app.route("/function1")
def function1():
    return render_template('function1.html')


if __name__ == '__main__':
    app.run(debug=True)
    