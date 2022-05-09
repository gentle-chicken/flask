from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print("Printing Hello World")
    return "Hello World"

@app.route('/home')
def home():
    return "This is home page"



app.run(debug=True)