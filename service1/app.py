from flask import Flask

app = Flask(__name__)

@app.route("/service1")
def main():
    return "service1"

if __name__ == '__main__':
    app.run(debug=True,port=3000)