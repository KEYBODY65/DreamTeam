from flask import Flask, render_template
import requests
from db.db_ap import Database_API
db = Database_API('db/databse.db')
app = Flask(__name__)  # создаём объект класса Flask
for i in range(1, 5):
    data = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}").json()  # кидаем Гет запрос
    db.create_recort(id_sensor=(i - 1) * 2, values=data['temperature'])
    db.create_recort(id_sensor=(i - 1) * 2 + 1, values=data['humidity'])




@app.route('/')  # Отслеживание(переход) на главную страницу
@app.route('/home')
def main():
    return render_template('index.html')


@app.route('/user')
def history():
    return render_template('user.html')


@app.route('/history')
def testimony():
    return render_template('history.html')


@app.route('/control')
def control():
    return render_template('control.html')


if __name__ == '__main__':  # условие запуска локального сервера
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на самой странице
