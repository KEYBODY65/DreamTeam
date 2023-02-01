from flask import Flask

app = Flask(__name__)  # созжаём объект класса Flask


@app.route('/')  # Отслеживание(переход) на главную страницу
def main():
    return "Привет, это главная странца"


@app.route('/reg')
def registration():
    return 'Страница регистарации пользователя'


@app.route('/history')
def history():
    return 'Показания датчиков теплицы за всё время'


if __name__ == '__main__':  # условие запуска локального сервера
    app.run(debug=True)  # debug стоит временно, он показывается все ошибки на смой странице
