from flask import Flask, render_template
from datetime import datetime
import sqlite3
import requests

app = Flask(__name__)  # создаём объект класса Flask
for i in range(1, 5):
    data = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}").json()  # кидаем Гет запрос


def make_a_database():
    with sqlite3.connect("db/databse.db") as db:
        db.cursor()
        for_tem_sensor = 'CREATE TABLE IF NOT EXISTS temperature_sensor (id int, temperature int, humidity int);'
        for_door = 'CREATE TABLE IF NOT EXISTS auto_door (state bool);'
        for_wat_machine = 'CREATE TABLE IF NOT EXISTS WATERING MACHINE (id int, state bool);'
        for_humid = 'CREATE TABLE IF NOT EXISTS humidification system (id int, state bool);'
        # Сначала создать таблицы, команды выше
        # Потом выполнить команды ниже:
        # for_tem_sensor = 'INSERTS INTO temperature_sensor (id int, temperature int, humidity int) VALUES(1, 27, 56)'
        # for_door = 'INSERTS INTO auto_door (state bool) VALUES(1);'
        # for_wat_machine = 'INSERTS INTO WATERING MACHINE (id int, state bool) VALUES(2, 0);'
        # for_humid = 'INSERTS INTO humidification system (id int, state bool) VALUES(3, 1);'
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
    date = """ CREATE TABLE IF NOT EXISTS date (day int, month str, year int); """
    time = """ CREATE TABLE IF NOT EXISTS time; """
    # date = """ INSERTS INTO date (day int, month str, year int) VALUES(25, 01, 2023); """
    # time = """ INSERTS INTO time (tmsm) VALUES(0-53-50); """
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
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на самой страни
