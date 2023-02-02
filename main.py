from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLalchemy
import requests

app = Flask(__name__)  # создаём объект класса Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLalchemy(app)
data = requests.get("https://dt.miet.ru/ppo_it/api/temp_hum/<number>")  # кидаем Гет запрос


class Indications(db.Model):
    data_base = {'temperature_sensor': {  # датчик температуры
        'id': ' device_id',
        'temperature': ' temp_value',
        'humidity': 'hum_value'
    },

        'auto_door': {  # дверца
            'state': 'state_value'
        },

        'WATERING MACHINE': {  # поливалка
            'id': 'device_id',
            'state': 'state_value'
        },

        'humidification system': {  # система увлажнения
            'state': 'state_value'
        }}


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
