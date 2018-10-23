from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "G'day, From W.A."

if __name__ == "__main__":
    print("G'day - 1")
    application.run()
