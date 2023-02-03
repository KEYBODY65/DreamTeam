from flask import Flask, render_template
from datetime import datetime
import sqlite3
import requests

app = Flask(__name__)  # создаём объект класса Flask
data = requests.get("https://dt.miet.ru/ppo_it/api/temp_hum/<number>")  # кидаем Гет запрос


def make_a_database():
    with sqlite3.connect("db/databse.db") as db:
        db.cursor()
        for_tem_sensor = 'CREATE TABLE IF NOT EXISTS temperature_sensor (id serial4, temperature int, humidity int);'
        for_door = 'CREATE TABLE IF NOT EXISTS auto_door (state bool);'
        for_wat_machine = 'CREATE TABLE IF NOT EXISTS "WATERING MACHINE" (id serial4, state bool);'
        for_humid = 'CREATE TABLE IF NOT EXISTS "humidification system" (id serial4, state bool);'
        db.execute(for_tem_sensor)
        db.execute(for_door)
        db.execute(for_wat_machine)
        db.execute(for_humid)

def time(year,month, day):
    return datetime.timestamp(datetime)


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
