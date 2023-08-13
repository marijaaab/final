from flask import Flask, render_template
import calc

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    dataR = calc.calculate()
    return render_template('index.html', dataR=dataR)


@app.route('/aboutApp')
def about_app():
    return render_template('aboutapp.html')


@app.route('/facts')
def did_you_know():
    return render_template('didyouknow.html')


@app.route('/aboutAuthor')
def about_author():
    return render_template('aboutauthor.html')

if __name__ == '__main__':
    app.run(debug=True)
