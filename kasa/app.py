from flask import Flask

kasa = Flask(__name__)

@kasa.route("/kasa")
@kasa.route("/")
def main():
    return "kasa"

@kasa.route("/kasa/usb")
@kasa.route("/usb")
def usb():
    return "kasa>usb"



if __name__ == '__main__':
    kasa.run(debug=True,port=5000)