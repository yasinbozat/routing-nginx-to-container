from flask import Flask

su = Flask(__name__)



@su.route("/su")
def main():
    return "su"

@su.route("/su/kapak")
def kapak():
    return "su>kapak"


if __name__ == '__main__':
    su.run(debug=True,port=4000)