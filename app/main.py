from flask import Flask, render_template, request
import calc


app = Flask(__name__, template_folder='.')


def generate_charts(filename):
    x_data = []
    y_data = []
    with open(filename, 'r') as f:
        for line in f:
            columns = line.split(",")
            x_data.append(columns[0])
            y_data.append(columns[1].split('\n')[0])
    x = ','.join(x_data)
    y = ','.join(y_data)
    dataR = {'xOsa': x, 'yOsa': y}
    return dataR


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
    app.run()
