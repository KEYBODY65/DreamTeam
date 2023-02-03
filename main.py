from flask import Flask, render_template
from datetime import datetime
import sqlite3
import requests

app = Flask(__name__)  # создаём объект класса Flask
for i in range(1, 5):
    data = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}")  # кидаем Гет запрос


def make_a_database():
    with sqlite3.connect("db/databse.db") as db:
        db.cursor()
        for_tem_sensor = 'CREATE TABLE IF NOT EXISTS temperature_sensor (id INTEGER, temperature INTEGER, humidity int) VALUES();'
        for_door = 'CREATE TABLE IF NOT EXISTS auto_door (state bool) VALUES();'
        for_wat_machine = 'CREATE TABLE IF NOT EXISTS "WATERING MACHINE" (id INTEGER, state bool) VALUES();'
        for_humid = 'CREATE TABLE IF NOT EXISTS "humidification system" (id INTEGER, state bool) VALUES();'
        db.execute(for_tem_sensor)
        db.execute(for_door)
        db.execute(for_wat_machine)
        db.execute(for_humid)
        db2.commit()


def get_date(year, month, day):
    return datetime.timestamp(datetime(year, month, day))


def get_time(tmsm):
    return datetime.fromtimestamp(tmsm).date()


with sqlite3.connect("db/databse.db") as db2:
    db2.cursor()
    date = """ CREATE TABLE IF NOT EXISTS "date" (day INTEGER, month STRING, year INTEGER) VALUES(); """
    time = """ CREATE TABLE IF NOT EXISTS "time" VALUES(); """
    db2.execute(date)
    db2.execute(time)
    db2.commit()


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
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на смой страни
