from flask import Flask, render_template, url_for

app = Flask(__name__)  # создаём объект класса Flask


@app.route('/')  # Отслеживание(переход) на главную страницу
@app.route('/home')
def main():
    return render_template('index.html')


@app.route('/user')
def history():
    return render_template('user.html')


@app.route('/testimony')
def testimony():
    return render_template('history.html')


if __name__ == '__main__':  # условие запуска локального сервера
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на смой странице