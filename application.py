from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/<string:name>")
def hello(name):
  name = name.capitalize()
  return f"<h1>Hello, {name}!<h1>"

#So if you go to the default route which just ends in a /
#the page will show "Hello, world!". But if you add '/name'
#to the end of the URL, it will show 'Hello, name!'
