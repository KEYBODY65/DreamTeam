from db.db_ap import Database_API
import numpy as np
import matplotlib.pyplot as plt

d = Database_API('db/databse.db')


def make_chats(time, value, id):  # Значения по у, сами значения столбцов
    fig2 = plt.figure(figsize=(8, 4))
    ax2 = fig2.add_subplot()

    ax2.set_ylabel('Влажность почвы, %', color='mediumturquoise')
    ax2.set_xlabel('Время')

    time = [f'{11 + i}:00' for i in range(6)]
    value = [d.connect("SELECT * FROM sensor_values", off=False, fetchall=True)]
    print(value)

for i in d.connect("SELECT * FROM sensor_values", off=False, fetchall=True):
    print(f"{i['id_sensor']}, {i['val']}, {i['n_time']}")
