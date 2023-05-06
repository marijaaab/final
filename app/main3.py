from flask import Flask, render_template, request



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
    data = {'xOsa': x, 'yOsa': y}
    return data


@app.route('/')
def index():
    data2021 = generate_charts('oi2021.txt')
    data2016 = generate_charts('oi2016.txt')
    data2012 = generate_charts('oi2012.txt')
    return render_template('index.html', data2021=data2021, data2016=data2016, data2012=data2012)


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
