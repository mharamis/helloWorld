from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World from Michael Haramis!'

@app.route('/hello')
def hello_world2():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

@app.route('/profit-summary')
def aboutcss():
    return render_template('profit-summary.html')


if __name__ == '__main__':
    app.run(debug=True)
