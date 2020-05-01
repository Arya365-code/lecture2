from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world!"

#So if you go to the default route which just ends in a /
#the page will show "Hello, world!". 
