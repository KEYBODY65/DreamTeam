from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)  # создаём объект класса Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)
data = requests.get("https://dt.miet.ru/ppo_it/api/temp_hum/<number>")  # кидаем Гет запрос


class Indications(db.Model):
    """
        CREATE TABLE IF NOT EXISTS temperature_sensor (id serial4, temperature int, humidity int);
        CREATE TABLE IF NOT EXISTS auto_door (state bool);
        CREATE TABLE IF NOT EXISTS "WATERING MACHINE" (id serial4, state bool);
        CREATE TABLE IF NOT EXISTS "humidification system" (id serial4, state bool);
    """

@app.route('/')  # Отслеживание(переход) на главную страницу
@app.route('/home')
def main():
    return render_template('index.html')


@app.route('/user')
def history():
    return render_template ('user.html')


@app.route('/history')
def testimony():
    return render_template('history.html')

@app.route('/control')
def control():
    return render_template('control.html')

if __name__ == '__main__':  # условие запуска локального сервера
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на смой страни
