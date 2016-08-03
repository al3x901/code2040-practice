from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, I love continuous delivery a lot! all day every day"

if __name__ == "__main__":
    app.run()
