from db.db_ap import Database_API
import numpy as np
import matplotlib.pyplot as plt
d = Database_API('db/databse.db')


def make_chats(id, value, time):
    # d.get_values() отсюда брать значения
    fig2 = plt.figure(figsize=(8, 4))
    ax2 = fig2.add_subplot()

    ax2.set_ylabel('Влажность почвы, %', color='mediumturquoise')
    ax2.set_xlabel('Время')

    x2 = [f'{11 + i}:00' for i in range(6)]
    y2 = [90, 95, 100, 89, 92, 95]

    ax2.bar(x2, y2, color='mediumturquoise')
    ax2.grid()

    plt.title('Просмотр влажности почвы 1-го датчика')

    fig2 = plt.figure(figsize=(8, 4))
    ax2 = fig2.add_subplot()

    ax2.set_ylabel('Влажность почвы, %', color='aquamarine')
    ax2.set_xlabel('Время')

    x2 = [f'{11 + i}:00' for i in range(6)]
    y2 = [90, 95, 100, 89, 92, 95]

    ax2.bar(x2, y2, color='aquamarine')
    ax2.grid()

    plt.title('Просмотр влажности почвы 2-го датчика')

    fig2 = plt.figure(figsize=(8, 4))
    ax2 = fig2.add_subplot()

    ax2.set_ylabel('Влажность почвы, %', color='aqua')
    ax2.set_xlabel('Время')

    x2 = [f'{11 + i}:00' for i in range(6)]
    y2 = [90, 95, 100, 89, 92, 95]

    ax2.bar(x2, y2, color='aqua')
    ax2.grid()

    plt.title('Просмотр влажности почвы 3-го датчика')

    fig2 = plt.figure(figsize=(8, 4))
    ax2 = fig2.add_subplot()

    ax2.set_ylabel('Влажность почвы, %', color='dodgerblue')
    ax2.set_xlabel('Время')

    x2 = [f'{11 + i}:00' for i in range(6)]
    y2 = [90, 95, 100, 89, 92, 95]

    ax2.bar(x2, y2, color='dodgerblue')
    ax2.grid()

    plt.title('Просмотр влажности почвы 4-го датчика')

    fig2 = plt.figure(figsize=(8, 4))
    ax2 = fig2.add_subplot()

    ax2.set_ylabel('Влажность почвы, %', color='lightseagreen')
    ax2.set_xlabel('Время')

    x2 = [f'{11 + i}:00' for i in range(6)]
    y2 = [90, 95, 100, 89, 92, 95]

    ax2.bar(x2, y2, color='lightseagreen')
    ax2.grid()

    plt.title('Просмотр влажности почвы 5-го датчика')

    fig2 = plt.figure(figsize=(8, 4))
    ax2 = fig2.add_subplot()

    ax2.set_ylabel('Влажность почвы, %', color='deepskyblue')
    ax2.set_xlabel('Время')

    x2 = [f'{11 + i}:00' for i in range(6)]
    y2 = [90, 95, 100, 89, 92, 95]

    ax2.bar(x2, y2, color='deepskyblue')
    ax2.grid()

    plt.title('Просмотр влажности почвы 6-го датчика')

    plt.show()

