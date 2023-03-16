from flask import Flask, render_template, request
from requests import get, patch
from db.db_ap import Database_API
from statistics import mean
from data_entry import DataEntry, Control, Entry_Lims

db = Database_API('./db/database.db')
app = Flask(__name__)  # создаём объект класса Flask
app.config["SECRET_KEY"] = "secret_key"
for i in range(1, 5):
    data = get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}").json()  # кидаем Гет запрос
    db.create_recort(id_sensor=(i - 1) * 2, temperature=data['temperature'], hum=data["humidity"],
                     hum_ground=data['humidity'])

times = []
datas_t = []
datas_h = []
data_hground = []


def values():
    times.clear()
    datas_t.clear()
    datas_h.clear()
    data_hground.clear()
    for j in range(1, 8):
        conter = db.get_values(j)
        for elem in conter:
            times.append(elem['n_time'])
            datas_t.append(elem['temperature'])
            datas_h.append(elem['hum'])
            data_hground.append(elem['hum_ground'])


values()


@app.route('/')  # Отслеживание(переход) на главную страницу
@app.route('/home')
def main():
    return render_template('index.html', title='Главная страница')


@app.route('/data_entry', methods=['GET', 'POST'])
def data_entry():
    form = DataEntry()
    if request.method == 'POST':
        idi = form.idi.data
        temperature = form.temperature.data
        humidification = form.humidification.data
        groundhumidification = form.humidificationground.data
        print(idi, temperature, humidification, groundhumidification)
        if idi and temperature and humidification and groundhumidification:
            db.create_recort(id_sensor=int(idi), temperature=int(temperature), hum=float(humidification),
                             hum_ground=float(groundhumidification))
    return render_template('dataentry.html', title='Ручное внесение данных', form=form)


@app.route('/charts', methods=['GET', 'POST'])
def charts():
    if request.method == 'POST':
        values()
    return render_template('charts.html', title='Графики', label=times, values=datas_t, values2=datas_h,
                           values3=data_hground, lenth=len(datas_t))


@app.route('/lim', methods=['GET', 'POST'])
def limit():
    form = Entry_Lims()
    if request.method == 'POST':
        t = form.T.data
        h = form.H.data
        h_and_g = form.Hb.data
        with open('limits', 'w', encoding='UTF-8') as file_lims:
            file_lims.seek(0)
            print(t, h, h_and_g)
            file_lims.write(str(t) + " " + str(h) + " " + str(h_and_g))

    return render_template('lim.html', title='Указать пределы температуры и влажности')


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
    flag_t = True
    flag_h = True
    flag_dh = True

    def validate():
        with open('limits', 'r', encoding='UTF-8') as file_lims:
            values_lims = list(map(int, file_lims.readlines()[0].split()))
            if mean(datas_t) < int(values_lims[0]):
                flag_t = False
                if not flag_t:
                    flag_h = True
                    flag_dh = True
            elif mean(datas_h) > int(values_lims[1]):
                flag_h = False
                if not flag_h:
                    flag_t = True
                    flag_dh = True
            elif mean(data_hground) > int(values_lims[-1]):
                flag_dh = False
                if not flag_dh:
                    flag_h = True
                    flag_t = True
        return flag_t, flag_h, flag_dh

    validate()
    return render_template('control.html', form=formas, flag_t=flag_t, flag_h=flag_h, flag_dh=flag_dh)


@app.route('/tables')
def tables():
    return render_template('tables.html', title='Таблица', lenth=len(datas_t), label=times, values=datas_t,
                           values2=datas_h,
                           values3=data_hground)


@app.route('/extra', methods=['GET', 'POST'])
def etra_control():
    pass  # Сделать экстренное управление


if __name__ == '__main__':  # условие запуска локального сервера
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на самой странице
