from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "G'day, from W.A."

if __name__ == "__main__":
    application.run()
