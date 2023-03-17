from flask import Flask, render_template, request
from requests import get, patch
from db.db_ap import Database_API
from statistics import mean
from data_entry import DataEntry, Control, Entry_Lims

db = Database_API('./db/database.db')
app = Flask(__name__)  # создаём объект класса Flask
app.config["SECRET_KEY"] = "secret_key"


def values():
    for i in range(1, 5):
        data = get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}").json()  # кидаем Гет запрос
        db.create_recort(id_sensor=(i - 1) * 2, temperature=data['temperature'], hum=data["humidity"],
                         hum_ground=data['humidity'])
    times = []
    d_t_1, d_t_2, d_t_3, d_t_4, d_t_5, d_t_6, d_t_7 = [], [], [], [], [], [], []
    d_h_1, d_h_2, d_h_3, d_h_4, d_h_5, d_h_6, d_h_7 = [], [], [], [], [], [], []
    d_hg_1, d_hg_2, d_hg_3, d_hg_4, d_hg_5, d_hg_6, d_hg_7 = [], [], [], [], [], [], []
    if len(d_t_1) == 25:
        d_t_1.clear()
        d_t_2.clear()
        d_t_3.clear()
        d_t_4.clear()
        d_t_5.clear()
        d_t_6.clear()
        d_t_7.clear()
        d_h_1.clear()
        d_h_2.clear()
        d_h_3.clear()
        d_h_4.clear()
        d_h_5.clear()
        d_h_6.clear()
        d_h_7.clear()
        d_hg_1.clear()
        d_hg_2.clear()
        d_hg_3.clear()
        d_hg_4.clear()
        d_hg_5.clear()
        d_hg_6.clear()
        d_hg_7.clear()
    for j in range(1, 8):
        conter = db.get_values(j)
        for elem in conter:
            times.append(elem['n_time'])
            if elem['id_sensor'] == 1:
                d_t_1.append(elem['temperature'])
                d_h_1.append(elem['hum'])
                d_hg_1.append(elem['hum_ground'])
            elif elem['id_sensor'] == 2:
                d_t_2.append(elem['temperature'])
                d_h_2.append(elem['hum'])
                d_hg_2.append(elem['hum_ground'])
            elif elem['id_sensor'] == 3:
                d_t_3.append(elem['temperature'])
                d_h_3.append(elem['hum'])
                d_hg_3.append(elem['hum_ground'])
            elif elem['id_sensor'] == 4:
                d_t_4.append(elem['temperature'])
                d_h_4.append(elem['hum'])
                d_hg_4.append(elem['hum_ground'])
            elif elem['id_sensor'] == 5:
                d_t_5.append(elem['temperature'])
                d_h_5.append(elem['hum'])
                d_hg_5.append(elem['hum_ground'])
            elif elem['id_sensor'] == 6:
                d_t_6.append(elem['temperature'])
                d_h_6.append(elem['hum'])
                d_hg_6.append(elem['hum_ground'])
            elif elem['id_sensor'] == 7:
                d_t_7.append(elem['temperature'])
                d_h_7.append(elem['hum'])
                d_hg_7.append(elem['hum_ground'])

    return d_t_1, d_t_2, d_t_3, d_t_4, d_t_5, d_t_6, d_t_7, d_h_1, d_h_2, d_h_3, d_h_3, d_h_4, d_h_5, d_h_6, \
           d_h_7, d_hg_1, d_hg_2, d_hg_3, d_hg_4, d_hg_5, d_hg_6, d_hg_7, times


def val_lim():
    datas_t = []
    datas_h = []
    data_hground = []
    for j in range(1, 8):
        conter = db.get_values(j)
        for elem in conter:
            datas_t.append(elem['temperature'])
            datas_h.append(elem['hum'])
            data_hground.append(elem['hum_ground'])

    return datas_t, datas_h, data_hground


@app.route('/')  # Отслеживание(переход) на главную страницу
@app.route('/home')
def main():
    d_t_1, d_t_2, d_t_3, d_t_4, d_t_5, d_t_6, d_t_7, d_h_1, d_h_2, d_h_3, d_h_3, d_h_4, d_h_5, d_h_6, \
    d_h_7, d_hg_1, d_hg_2, d_hg_3, d_hg_4, d_hg_5, d_hg_6, d_hg_7, times = values()
    return render_template('index.html', title='Главная страница')


@app.route('/data_entry', methods=['GET', 'POST'])
def data_entry():
    form = DataEntry()
    if request.method == 'POST':
        idi = form.idi.data
        temperature = form.temperature.data
        humidification = form.humidification.data
        groundhumidification = form.humidificationground.data
        if idi and temperature and humidification and groundhumidification:
            db.create_recort(id_sensor=int(idi), temperature=int(temperature), hum=float(humidification),
                             hum_ground=float(groundhumidification))
    return render_template('dataentry.html', title='Ручное внесение данных', form=form)


@app.route('/charts', methods=['GET', 'POST'])
def charts():
    d_t_1, d_t_2, d_t_3, d_t_4, d_t_5, d_t_6, d_t_7, d_h_1, d_h_2, d_h_3, d_h_3, d_h_4, d_h_5, d_h_6, \
    d_h_7, d_hg_1, d_hg_2, d_hg_3, d_hg_4, d_hg_5, d_hg_6, d_hg_7, times = values()
    return render_template('charts.html', title='Графики', times=times, temp1=d_t_1, temp2=d_t_2,
                           temp3=d_t_3, temp4=d_t_4, temp5=d_t_5, temp6=d_t_6, temp7=d_t_7, hum1=d_h_1, hum2=d_h_2,
                           hum3=d_h_3, hum4=d_h_4, hum=d_h_5, hum6=d_h_6, hum7=d_h_7,
                           hum_ground1=d_hg_1, hum_ground2=d_hg_2, hum_ground3=d_hg_3, hum_ground4=d_hg_4,
                           hum_ground5=d_hg_5, hum_ground6=d_hg_6, hum_ground7=d_hg_7, lenth=25)


@app.route('/lim', methods=['GET', 'POST'])
def limit():
    form = Entry_Lims()
    if request.method == 'POST':
        t = form.T.data
        h = form.H.data
        h_and_g = form.Hb.data
        with open('limits', 'w', encoding='UTF-8') as file_lims:
            file_lims.seek(0)
            file_lims.write(str(t) + " " + str(h) + " " + str(h_and_g))

    return render_template('lim.html', title='Указать пределы температуры и влажности')


@app.route('/control', methods=['GET', 'POST'])
def control():
    formas = Control()
    if formas.door_open:
        patch('https://dt.miet.ru/ppo_it/api/fork_drive/ https://dt.miet.ru/ppo_it/api/fork_drive/',
              params={"state": 1})
        if formas.door_close:
            patch('https://dt.miet.ru/ppo_it/api/fork_drive/ https://dt.miet.ru/po_it/api/fork_drive/',
                  params={"state": 0})
    elif formas.hum_on:
        patch('https://dt.miet.ru/ppo_it/api/total_hum', params={"state": 1})
        if formas.hum_off:
            patch('https://dt.miet.ru/ppo_it/api/total_hum', params={"state": 0})
    elif formas.idi_of_wtringa != 0 and formas.watringa_on:
        number = formas.idi_of_wtringa
        patch('https://dt.miet.ru/ppo_it/api/total_hum', params={'id': number, 'state': 1})
        if formas.watringa_off:
            patch('https://dt.miet.ru/ppo_it/api/total_hum', params={'id': number, 'state': 0})
    elif formas.watringa_all_on:
        for v in range(1, 7):
            patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': v, 'state': 1})
        if formas.watringa_all_off:
            for j in range(1, 7):
                patch('https://dt.miet.ru/ppo_it/api/watering', params={'id': j, 'state': 0})
    flag_t = True
    flag_h = True
    flag_dh = True

    def validate():
        flag_t = True
        flag_h = True
        flag_dh = True
        datas_t, datas_h, data_hground = val_lim()
        with open('limits', 'r', encoding='UTF-8') as file_lims:
            values_lims = list(map(int, file_lims.readlines()[0].split()))
            if mean(datas_t) < int(values_lims[0]):
                flag_t, flag_h, flag_dh = False, True, True
            elif mean(datas_h) > int(values_lims[1]):
                flag_h, flag_t, flag_dh = False, True, True
            elif mean(data_hground) > int(values_lims[-1]):
                flag_dh, flag_h, flag_h = False, True, True
        return flag_t, flag_h, flag_dh

    validate()
    if Control.extra_control:
        flag_t, flag_h, flag_dh = True, True, True
    return render_template('control.html', form=formas, flag_t=flag_t, flag_h=flag_h, flag_dh=flag_dh)


@app.route('/tables')
def tables():
    d_t_1, d_t_2, d_t_3, d_t_4, d_t_5, d_t_6, d_t_7, d_h_1, d_h_2, d_h_3, d_h_3, d_h_4, d_h_5, d_h_6, \
    d_h_7, d_hg_1, d_hg_2, d_hg_3, d_hg_4, d_hg_5, d_hg_6, d_hg_7, times = values()
    return render_template('tables.html', title='Таблица', lenth=25, times=times, temp1=d_t_1, temp2=d_t_2,
                           temp3=d_t_3, temp4=d_t_4, temp5=d_t_5, temp6=d_t_6, temp7=d_t_7, hum1=d_h_1, hum2=d_h_2,
                           hum3=d_h_3, hum4=d_h_4, hum=d_h_5, hum6=d_h_6, hum7=d_h_7,
                           hum_ground1=d_hg_1, hum_ground2=d_hg_2, hum_ground3=d_hg_3, hum_ground4=d_hg_4,
                           hum_ground5=d_hg_5, hum_ground6=d_hg_6, hum_ground7=d_hg_7)


if __name__ == '__main__':  # условие запуска локального сервера
    db.create_tables()
    app.run(debug=True)  # debug стоит временно, он показывает все ошибки на самой странице
