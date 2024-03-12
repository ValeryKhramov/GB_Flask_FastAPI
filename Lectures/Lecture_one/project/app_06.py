from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hi!'


@app.route('/index/')
def html_index():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон'
    }
    return render_template('index.html', **context)


@app.route('/if/')
def show_if():
    context = {
        'title': 'Ветвление',
        'user': 'Крутой хакер!',
        'number': 1
    }
    return render_template('show_if.html', **context)


@app.route('/poems/')
def poems():
    context = {'title': 'Циклы',
               'poem': ['Вот не думал, не гадал,',
                        'Программистом взял и стал.',
                        'Хитрый знает он язык,',
                        'Он к другому не привык.',
                        ]}
    # txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return render_template('show_for.html', **context)


@app.route('/users/')
def users():
    _users = [{
        'name': 'Никанор',
        'mail': 'nik@mail.ru',
        'phone': '+7-987-897-89-25'},
        {
            'name': 'Феофан',
            'mail': 'nrdftgvbhk@mail.ru',
            'phone': '+7-989-800-00-55'},
        {
            'name': 'Овернар',
            'mail': 'niyhgffwk@mail.ru',
            'phone': '+7-555-555-55-55'}
    ]
    context = {'users': _users,
               'title': 'Точечная нотация'}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
