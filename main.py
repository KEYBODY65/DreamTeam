from flask import Flask

app = Flask(__name__)  # созжаём объект класса Flask


@app.route('/')  # Отслеживание(переход) на главную страницу
@app.route('/home')
def main():
    return "Управление теплицей"


@app.route('/user')
def history():
    return 'Ручное внесение изменений'


@app.route('/testimony')
def testimony():
    return 'Таблица с показаниями + средняя температура'


if __name__ == '__main__':  # условие запуска локального сервера
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на смой странице
