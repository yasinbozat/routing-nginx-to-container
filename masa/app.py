from flask import Flask

masa = Flask(__name__)

@masa.route("/masa")
def main():
    return "masa"

if __name__ == '__main__':
    masa.run(debug=True,port=3000)