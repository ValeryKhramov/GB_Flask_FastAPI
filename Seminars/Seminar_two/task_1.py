import logging
from pathlib import PurePath, Path
from flask import Flask, render_template, request, abort, redirect, url_for, flash
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'dfc2bfb34cc2888a9a7491adc9842762dd270d4cdbf99447a22fbda5856c3f26'
logger = logging.getLogger(__name__)


@app.route('/next_page/')
def next_page():
    context = {'title': 'Задание №1'}
    return render_template('page_1.html', **context)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/load_image/', methods=['GET', 'POST'])
def load_image():
    context = {'title': 'Задание №2'}
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл {escape(file_name)} загружен на сервер!'
    return render_template('page_2.html', **context)


@app.route("/authorization/", methods=['GET', 'POST'])
def authorization():
    context = {'title': 'Задание №3'}
    login = {
        'login': 'login',
        'password': '123'
    }
    if request.method == 'POST':
        login_user = request.form.get('login')
        password_user = request.form.get('password')
        if login.get('login') == login_user and login.get('password') == password_user:
            return f'Вход с логином : {escape(login_user)} выполнен успешно!'
        else:
            return 'Ошибка'
    return render_template('authorization.html', **context)


@app.route('/counter/', methods=['GET', 'POST'])
def counter():
    context = {'title': 'Задание №4'}
    if request.method == 'POST':
        text = request.form.get('text')
        return f'Количество слов:{str(len(text.split()))}'
    return render_template('counter.html', **context)


@app.route('/calculator/', methods=['GET', 'POST'])
def calculator():
    context = {'title': 'Задание № 5'}
    if request.method == 'POST':
        first_num = request.form.get('number_1')
        second_num = request.form.get('number_2')
        operation = request.form.get('operation')
        match operation:
            case 'add':
                return f'{first_num} + {second_num} = {int(first_num) + int(second_num)}'
            case 'subtract':
                return f'{first_num} - {second_num} = {int(first_num) - int(second_num)}'
            case 'multiply':
                return f'{first_num} * {second_num} = {int(first_num) * int(second_num)}'
            case 'divide':
                if int(second_num) == 0:
                    return 'На ноль делить нельзя!'
                else:
                    return f'{first_num} / {second_num} = {int(first_num) / int(second_num)}'

    return render_template('calculator.html', **context)


@app.errorhandler(403)
def page_not_found(e):
    logger.warning(e)
    context = {'title': 'Доступ запрещен по возрасту'}
    return render_template('403.html', **context)


@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    context = {'title': 'Задание № 6'}
    MIN_AGE = 18
    MAX_AGE = 100
    if request.method == 'POST':
        age = request.form.get('age')
        name = request.form.get('name')
        if MIN_AGE <= int(age) <= MAX_AGE:
            return f'{name}, вы вошли!'

        abort(403)

    return render_template('age.html', **context)


@app.route('/quadro/', methods=['GET', 'POST'])
def quadro():
    NUMBER = 5
    return redirect(url_for('quadro_result', number=int(NUMBER ** 2)))


@app.route('/quadro/<int:number>/')
def quadro_result(number):
    return str(number)


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
