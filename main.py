from flask import Flask, render_template, request
from requests import get, patch
from db.db_ap import Database_API
from data_entry import DataEntry, Control

db = Database_API('./db/database.db')
app = Flask(__name__)  # создаём объект класса Flask
app.config["SECRET_KEY"] = "secret_key"
for i in range(1, 5):
    data = get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}").json()  # кидаем Гет запрос
    db.create_recort(id_sensor=(i - 1) * 2, temperature=data['temperature'], hum=data["humidity"],
                     hum_ground=data['humidity'])


@app.route('/')  # Отслеживание(переход) на главную страницу
@app.route('/home')
def main():
    return render_template('index.html', title='Главная страница')


@app.route('/data_entry', methods=['GET', 'POST'])
def data_entry():
    form = DataEntry()
    if form.submit():
        idi = request.form.get("id")
        temperature = request.form.get("temperature")
        humidification = request.form.get("humidification")
        groundhumidification = request.form.get("groundhumidification")
        if idi and temperature and humidification and groundhumidification:
            db.create_recort(id_sensor=int(idi), temperature=int(temperature), hum=float(humidification),
                             hum_ground=float(groundhumidification))
    return render_template('dataentry.html', title='Ручное внесение данных', form=form)


@app.route('/charts')
def charts():
    times = []
    datas_t = []
    datas_h = []
    datas_gh = []
    data_hground = []
    if '00:00:00' in times:
        times.clear()
        datas_t.clear()
        datas_h.clear()
        data_hground.clear()
    for i in range(1, 8):
        conter = db.get_values(i)
        for elem in conter:
            times.append(elem['n_time'])
            datas_h.append(elem['temperature'])
            datas_gh.append(elem['hum_ground'])

    return render_template('charts.html', title='Графики', label=times, values=datas_t, values2=datas_h)


@app.route('/lim')
def limit():
    return render_template('lim.html')


def validate():
    pass


@app.route('/control', methods=['GET', 'POST'])
def control():
    formas = Control()
    if Control.door_open:
        patch('https://dt.miet.ru/ppo_it/api/fork_drive/ https://dt.miet.ru/ppo_it/api/fork_drive/',
              params={"state": 1})
        if Control.door_close:
            patch('https://dt.miet.ru/ppo_it/api/fork_drive/ https://dt.miet.ru/po_it/api/fork_drive/',
                  params={"state": 0})
    elif Control.hum_on:
        patch('https://dt.miet.ru/ppo_it/api/total_hum', params={"state": 1})
        if Control.hum_off:
            patch('https://dt.miet.ru/ppo_it/api/total_hum', params={"state": 0})
    elif Control.idi_of_wtringa != 0 and Control.watringa_on:
        number = Control.idi_of_wtringa
        patch('https://dt.miet.ru/ppo_it/api/total_hum', params={'id': number, 'state': 1})
        if Control.watringa_off:
            patch('https://dt.miet.ru/ppo_it/api/total_hum', params={'id': number, 'state': 0})
    elif Control.watringa_all_on:
        for v in range(1, 7):
            patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': v, 'state': 1})
        if Control.watringa_all_off:
            for j in range(1, 7):
                patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': j, 'state': 0})

    return render_template('control.html', form=formas)


if __name__ == '__main__':  # условие запуска локального сервера
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на самой странице
