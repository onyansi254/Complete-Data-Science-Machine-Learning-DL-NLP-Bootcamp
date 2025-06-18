from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to the Flask application!"

@app.route("/greet", methods=['GET'])
def greet():
    return render_template('greet.html')

@app.route("/submit", methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        # Handle form submission logic here
        #return "Form submitted successfully!"
        name=request.form.get('name')
    else:
        # Render the form for GET requests
        return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
