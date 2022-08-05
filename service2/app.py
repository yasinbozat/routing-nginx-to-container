from flask import Flask

app = Flask(__name__)

@app.route("/service2")
def main():
    return "service2"

if __name__ == '__main__':
    app.run(debug=True,port=4000)