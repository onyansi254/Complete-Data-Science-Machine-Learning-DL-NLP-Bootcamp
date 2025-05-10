from flask import Flask, render_template

'''
It creates an instance of the Flsk class,
which will be your WSGI(Web Server Gateway Interface) application.'''

# wsgi: Web Server Gateway Interface
app = Flask(__name__)

@app.route("/")
def hello():
    return "New here worry not, I gatchu"

@app.route("/hello")
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)