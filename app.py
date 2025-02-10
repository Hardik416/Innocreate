from flask import Flask

app = Flask(__name__) 

@app.route("/")
def hello_world():
  return "hiiiii innocreaters"

@app.route("/about")
def about():
  return "This is about page"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)