from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, незнакомец!'


@app.route('/Николай/')
def nuke():
    return 'Привет, Николай!'


@app.route('/Иван/')
def ivan():
    return 'Привет, Иван!'


# Множественное декорирование
@app.route('/Федор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Федор!'


if __name__ == '__main__':
    app.run(debug=True)
