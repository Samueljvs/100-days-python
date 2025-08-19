from flask import Flask

app = Flask(__name__)

# Make underline decorator

def underline(function):
    def wrapper():
        return f"<u> {function()} </u>"
    return wrapper

# make Bold decorator
def bold(function):
    def wrapper():
        return f"<b> {function()} </b>"
    return wrapper

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@underline
@bold
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)

# py -m flask --app main.py --debug run ---- use this to serve up the app for the command terminal, note you'll need to navigate to the folder
