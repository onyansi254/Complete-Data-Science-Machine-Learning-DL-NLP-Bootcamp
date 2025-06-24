from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to the Flask application!"


@app.route("/greet", methods=['GET'])
def greet():
    return render_template('greet.html')


@app.route("/submit1", methods=['GET', 'POST'])
def submit1():
    if request.method == 'POST':
        name = request.form['name']
        return f'Form submitted successfully! Hello, {name}'
    else:
        return render_template('submit1.html')


@app.route('/success/<score>')
def success(score):
    res = ""
    if int(score) >= 50:
        res = "You have passed the exam!"
    else:
        res = "You have failed the exam!"
    return render_template('result.html', results=res)


@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "You have passed the exam!"
    else:
        res = "You have failed the exam!"

    exp = {'score': score, 'result': res}
    return render_template('result1.html', results=exp)


@app.route('/success_int/<int:score>')
def success_int(score):
    return render_template('result1.html', results=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result1.html', results=score)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        math = float(request.form['math'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = (science + math + c + datascience) / 4
        return redirect(url_for('successres', score=total_score))
    else:
        return render_template('getresult.html')


if __name__ == '__main__':
    app.run(debug=True)
