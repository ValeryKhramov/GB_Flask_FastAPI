from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'about'


@app.route('/')
def contact():
    return 'contact'


@app.route('/sum/<int:num_1>/<int:num_2>/')
def sum_nums(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)


@app.route('/string/<string:line>/')
def len_line(line: str) -> str:
    return str(len(line))


@app.route('/world/')
def world():
    return render_template('index.html')


@app.route('/students/')
def students():
    head = {
        'first_name': 'Имя',
        'last_name': 'Фамилия',
        'age': 'Возраст',
        'rating': 'Средний балл'
    }

    students_list = [
        {
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'age': 18,
            'rating': 4
        },
        {
            'first_name': 'Петр',
            'last_name': 'Петров',
            'age': 19,
            'rating': 3
        },
        {
            'first_name': 'Семен',
            'last_name': 'Семенов',
            'age': 20,
            'rating': 5
        }
    ]
    return render_template('index.html', **head, students_list=students_list)


@app.route('/news/')
def get_news():
    news_block = [
        {
            'title': 'Новость № 1',
            'description': 'Описание № 1',
            'create_at': datetime.datetime.now().strftime('%H:%M - %m.%d.%Y года.'),
        },
        {
            'title': 'Новость № 2',
            'description': 'Описание № 2',
            'create_at': datetime.datetime.now().strftime('%H:%M - %m.%d.%Y года.')
        },
        {
            'title': 'Новость № 3',
            'description': 'Описание № 3',
            'create_at': datetime.datetime.now().strftime('%H:%M - %m.%d.%Y года.')
        }
    ]
    return render_template('news.html', news_block=news_block)


if __name__ == '__main__':
    app.run(debug=True)
