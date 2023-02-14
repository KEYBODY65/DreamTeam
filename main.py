from flask import Flask, render_template, request
from requests import get
from db.db_ap import Database_API
from data_entry import DataEntry

db = Database_API('db/databse.db')

app = Flask(__name__)  # создаём объект класса Flask
app.config["SECRET_KEY"] = "secret_key"
for i in range(1, 5):
    data = get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}").json()  # кидаем Гет запрос
    db.create_recort(id_sensor=(i - 1) * 2, values=data['temperature'])
    db.create_recort(id_sensor=(i - 1) * 2 + 1, values=data['humidity'])


@app.route('/')  # Отслеживание(переход) на главную страницу
@app.route('/home')
def main():
    return render_template('index.html')


@app.route('/data_entry', methods=['GET', 'POST'])
def data_entry():
    form = DataEntry()
    if form.submit():
        id = request.form.get("id_sensor")
        temperature = request.form.get("temperature")
        humidification = request.form.get("humidification")
        if id and temperature and humidification:
            db.create_recort(id_sensor=int(id), values=int(temperature))
            db.create_recort(id_sensor=int(id), values=int(humidification))
    return render_template('dataentry.html', title='Ручное внесение данных', form=form, menu='index.html')


@app.route('/control')
def control():
    return render_template('control.html')


@app.route('/charts')
def charts():
    return render_template('charts.html')

if __name__ == '__main__':  # условие запуска локального сервера
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на самой странице
