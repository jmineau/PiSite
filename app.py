from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/AboutMe')
def about():
    return render_template('AboutMe.html')


@app.route('/Birds')
def Birds():
    return render_template('Birds.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
