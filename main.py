from flask import Flask, render_template, request
from requests import get
from db.db_ap import Database_API
from data_entry import DataEntry, Recharging
from charts import makes_charts

db = Database_API('db/databse.db')
mc = makes_charts()
app = Flask(__name__)  # создаём объект класса Flask
app.config["SECRET_KEY"] = "secret_key"
for i in range(1, 5):
    data = get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}").json()  # кидаем Гет запрос
    db.create_recort(id_sensor=(i - 1) * 2, values=data['temperature'])
    db.create_recort(id_sensor=(i - 1) * 2 + 1, values=data['humidity'])


@app.route('/')  # Отслеживание(переход) на главную страницу
@app.route('/home')
def main():
    return render_template('index.html', title='Домашняя страница')


@app.route('/data_entry', methods=['GET', 'POST'])
def data_entry():
    form = DataEntry()
    if form.submit():
        idi = request.form.get("id_sensor")
        temperature = request.form.get("temperature")
        humidification = request.form.get("humidification")
        if idi and temperature and humidification:
            db.create_recort(id_sensor=int(idi), values=int(temperature))
            db.create_recort(id_sensor=int(idi), values=int(humidification))
    return render_template('dataentry.html', title='Ручное внесение данных', form=form)


@app.route('/control')
def control():
    return render_template('control.html', title='Внесение данных')


@app.route('/charts')
def charts():
    forma = Recharging()
    if forma.recharging():
        for i in range(1, 8):
            for datas in db.get_values(i):
                if i % 2 == 0:
                     mc.make_chart_for_humidification(datas['val'], datas['n_time'])
                else:
                    mc.make_chart_for_temperature(datas['val'], datas['n_time'])

    return render_template('charts.html', form=forma, title='Управление')


if __name__ == '__main__':  # условие запуска локального сервера
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на самой странице
