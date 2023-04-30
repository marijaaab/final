# from flask import Flask, render_template
# import matplotlib
# import matplotlib.pyplot as plt
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time
#
# matplotlib.use('Agg')
#
#
# app = Flask(__name__, template_folder='.')
#
#
# def generate_plot():
#     # Code to generate plot here
#     x_data = []
#     y_data = []
#     with open('data.txt', 'r') as f:
#         for line in f:
#             columns = line.split(",")
#             x_data.append(columns[0])
#             y_data.append(float(columns[1]))
#
#     print(x_data)
#     print(y_data)
#
#     plt.bar(x_data, y_data, color=['red', 'blue', 'green', 'purple', 'pink', 'yellow', 'black', 'orange', 'brown'])
#
#     plt.xlabel('Gradovi')
#     plt.ylabel('Temperatura')
#
#     plt.annotate("Temperatura u \ngradovima Srbije", xy=('Zupa', 6))
#
#     filename = f"static/graph_{int(time.time())}.png"
#     plt.savefig(filename)
#     return filename
#
#
# class CodeChangeHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         if event.src_path.endswith('.py'):
#             generate_plot()
#
#
# event_handler = CodeChangeHandler()
# observer = Observer()
# observer.schedule(event_handler, '.', recursive=True)
# observer.start()
#
#
# @app.route('/')
# def index():
#     filename = generate_plot()
#     return render_template('index.html', filename=filename)
#
#
# if __name__ == '__main__':
#     generate_plot()
#     app.run()
#     observer.join()

# from flask import Flask, render_template
# import matplotlib
# import matplotlib.pyplot as plt
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time
#
# matplotlib.use('Agg')
#
#
# app = Flask(__name__, template_folder='.')
# # filename = generate_plot()
#
#
# def generate_plot():
#     # Code to generate plot here
#     x_data = []
#     y_data = []
#     with open('data.txt', 'r') as f:
#         for line in f:
#             columns = line.split(",")
#             x_data.append(columns[0])
#             y_data.append(float(columns[1]))
#
#     print(x_data)
#     print(y_data)
#
#     plt.bar(x_data, y_data, color=['red', 'blue', 'green', 'purple', 'pink', 'yellow', 'black', 'orange', 'brown'])
#
#     plt.xlabel('Gradovi')
#     plt.ylabel('Temperatura')
#
#     plt.annotate("Temperatura u \ngradovima Srbije", xy=('Zupa', 6))
#
#     global filename
#     filename = f"static/graph_{int(time.time())}.png"
#     plt.savefig(filename)
#     return filename
#
#
# class CodeChangeHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         if event.src_path.endswith('.py'):
#             generate_plot()
#
#
# event_handler = CodeChangeHandler()
# observer = Observer()
# observer.schedule(event_handler, '.', recursive=True)
# observer.start()
#
#
# @app.route('/')
# def index():
#     return render_template('index.html', filename=filename + "?" + str(time.time()))
#
#
# if __name__ == '__main__':
#     generate_plot()
#     app.run()
#     observer.join()

from flask import Flask, render_template, request
import matplotlib
import matplotlib.pyplot as plt
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import json

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
    print(y)
    data = {'xOsa': x, 'yOsa': y}
    return data

    # plt.figure(figsize=(12, 7))
    #
    # plt.bar(x_data, y_data, color=['red', 'blue', 'green', 'purple', 'pink', 'yellow', 'grey', 'orange', 'brown',
    #                                'turquoise', 'limegreen', 'powderblue', 'magenta', 'white', 'firebrick',
    #                                'darkturquoise'], label="Inline label", edgecolor="black", linewidth=1.2)
    #
    # plt.title("Grafik", size=28, weight="bold", style="oblique")
    # plt.legend()
    #
    # plt.xlabel('Gradovi', size=16, weight="bold")
    # plt.ylabel('Temperatura', size=16, weight="bold")
    #
    # # plt.annotate("Temperatura u \ngradovima Srbije", xy=('Zupa', 6))
    #
    # filename = f"static/graph_{int(time.time())}.png"
    # # plt.savefig(filename)
    # return filename

# class CodeChangeHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         if event.src_path.endswith('.py'):
#             generate_plot()

# event_handler = CodeChangeHandler()
# observer = Observer()
# observer.schedule(event_handler, '.', recursive=True)
# observer.start()


@app.route('/')
def index():
    # filename = generate_plot()

    data = generate_plot()

    # data = {'xOsa': 'Buba,Buba2', 'yOsa': '55, 49, 44, 24, 15'}
    # data = {x_data, y_data}
    # user = {'name': 'Buba', 'lastname': 'Bubic'}
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/facts')
def didyouknow():
    return render_template('didyouknow.html')

if __name__ == '__main__':
    print("Hello")
    # generate_plot()
    app.run(debug=True)
    print("Bye")
    # observer.join()
