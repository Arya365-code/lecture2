from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world!"

@app.route("/<string:name>")
def hello(name):
  name = name.capitalize()
  return f"Hello, {name}!"

#So if you go to the default route which just ends in a /
#the page will show "Hello, world!". But if you add '/name'
#to the end of the URL, it will show 'Hello, name!'
