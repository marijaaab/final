from flask import Flask, render_template, request
import matplotlib

matplotlib.use('Agg')

app = Flask(__name__, template_folder='.')


def generate_plot():
    x_data = []
    y_data = []
    with open('data.txt', 'r') as f:
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
    data = generate_plot()
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/facts')
def didyouknow():
    return render_template('didyouknow.html')


if __name__ == '__main__':
    app.run(debug=True)
