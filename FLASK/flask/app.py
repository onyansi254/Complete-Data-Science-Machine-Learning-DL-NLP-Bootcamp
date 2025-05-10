from flask import Flask

'''
It creates an instance of the Flsk class,
which will be your WSGI(Web Server Gateway Interface) application.'''

# wsgi: Web Server Gateway Interface
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!. how are you?. ok"

if __name__ == '__main__':
    app.run(debug=True)