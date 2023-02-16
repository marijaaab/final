from flask import Flask, render_template
import pandas as pd
import plotly
import plotly.graph_objs as go
import matplotlib.pyplot as plt


app = Flask(__name__, template_folder='.')



@app.route('/')

def index():
    ######### VERSION 1 #########
    # Read data from file
    # df = pd.read_csv("data.txt", sep=' ', header=None)
    #
    # # Create the scatter plot
    # trace = go.Scatter(x=df[0], y=df[1], mode='markers')
    # data = [trace]
    #
    # # Generate the HTML code for the plot
    # plot_html = plotly.offline.plot(data, include_plotlyjs=False, output_type='div')
    #
    # return render_template('index.html', plot_html=plot_html)

    ######### VERSION 1 #########
    # Read values from a .txt file
    x_data = []
    y_data = []
    with open('data.txt', 'r') as f:
        for line in f:
            columns = line.split(",")
            x_data.append(columns[0])
            y_data.append(float(columns[1]))

    print(x_data)
    print(y_data)

    # Draw a graphic using the values
    plt.bar(x_data, y_data, color=['red','blue', 'green', 'purple', 'pink', 'yellow', 'black', 'orange', 'brown'])

    plt.xlabel('Gradovi')
    plt.ylabel('Temperatura')

    plt.annotate("Temperatura u \ngradovima Srbije", xy=('Zupa',6))

    ### plt.show()
    plt.savefig('static/graph.png')
    # plt.show()
    return render_template('index.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
