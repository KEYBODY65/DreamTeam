from flask import Flask, render_template, request
from requests import get, patch
from db.db_ap import Database_API
from data_entry import DataEntry, Recharging, Control
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
    return render_template('index.html')


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
    formas = Control()
    if formas.door_open():
        open = 1
        patch('https://dt.miet.ru/ppo_it/api/fork_drive/ ', params={'state': open})
        if formas.door_close():
            close = 0
            patch('https://dt.miet.ru/ppo_it/api/fork_drive/ ', params={'state': close})
    elif formas.hum_on():
        on = 1
        patch('https://dt.miet.ru/ppo_it/api/total_hum', params={'state': on})
        if formas.hum_off():
            off = 0
            patch('https://dt.miet.ru/ppo_it/api/total_hum', params={'state': off})
    elif formas.watringa1():
        on_w = 1
        id = 1
        patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': on_w})
        if formas.watringa1_off():
            off_w = 0
            id = 12
            patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': off_w})
    elif formas.watringa2():
        on_w = 1
        id = 2
        patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': on_w})
        if formas.watringa2_off():
            off_w = 0
            id = 2
            patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': off_w})
    elif formas.watringa3():
        on_w = 1
        id = 3
        patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': on_w})
        if formas.watringa3_off():
            off_w = 0
            id = 3
            patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': off_w})
    elif formas.watringa4():
        on_w = 1
        id = 4
        patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': on_w})
        if formas.watringa4_off():
            off_w = 0
            id = 4
            patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': off_w})
    elif formas.watringa5():
        on_w = 1
        id = 5
        patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': on_w})
        if formas.watringa5_off():
            off_w = 0
            id = 5
            patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': off_w})
    elif formas.watringa6():
        on_w = 1
        id = 6
        patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': on_w})
        if formas.watringa6_off():
            off_w = 0
            id = 6
            patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': id, 'state': off_w})
    elif formas.watringa_on_all():
        on_w = 1
        for i in range(1, 7):
            patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': i, 'state': on_w})
        if formas.watringa_off_all():
            off_w = 0
            for j in range(1, 7):
                patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': j, 'state': off_w})

    return render_template('control.html', title='Ручное управление теплицей', form=formas)


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

    return render_template('charts.html', form=forma)


if __name__ == '__main__':  # условие запуска локального сервера
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на самой странице
