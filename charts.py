import matplotlib.pyplot as plt
from db.db_ap import get_values
fig2 = plt.figure(figsize=(8, 4))
ax2 = fig2.add_subplot()


def make_charts():
    ax2.set_ylabel('Влажность почвы, %', color='mediumturquoise')
    ax2.set_xlabel('Время')

    x2 = [f'{11 + i}:00' for i in range(6)]
    y2 = []
    ax2.bar(x2, y2, color='mediumturquoise')
    ax2.grid()
    for i in make_charts():
        y2.append(i['humidification'])
    plt.title('Просмотр влажности почвы 1-го датчика')

    plt.show()
