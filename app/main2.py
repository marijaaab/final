from flask import Flask, render_template
import matplotlib.pyplot as plt


def generate_graph():
    x_data = []
    y_data = []
    with open('data.txt', 'r') as f:
        for line in f:
            columns = line.split(",")
            x_data.append(columns[0])
            y_data.append(float(columns[1]))

    print(x_data)
    print(y_data)

    plt.bar(x_data, y_data, color=['red','blue', 'green', 'purple', 'pink', 'yellow', 'black', 'orange', 'brown'])

    plt.xlabel('Gradovi')
    plt.ylabel('Temperatura')

    plt.annotate("Temperatura u \ngradovima Srbije", xy=('Zupa',6))

    plt.savefig('static/graph.png')


app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    generate_graph()
    app.run()
