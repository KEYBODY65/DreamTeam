import matplotlib.pyplot as plt


class makes_charts:
    def make_chart_for_temperature(self, data, time):
        datas = []
        times = []
        if time == '00:00:00':
            datas.clear()
            times.clear()
        else:
            datas.append(data)
            times.append(time)
        time = times
        value = datas

        plt.plot(time, value, color='orangered', marker='o', markersize=7)

        plt.legend(title='Температура, °C', facecolor='oldlace', edgecolor='orangered')

        plt.xlabel('Время')
        plt.ylabel('Значение')
        plt.title('Просмотр  температуры в теплице 1-го датчика')

        plt.savefig('graph_temperature.png')

    def make_chart_for_humidification(self, data, time):
        datas = []
        times = []
        if time == '00:00:00':
            datas.clear()
            times.clear()
        else:
            datas.append(data)
            times.append(time)
        time = times
        value = datas

        plt.plot(time, value, color='skyblue', marker='o', markersize=7)

        plt.legend(title='Влажность, кг/м3', facecolor='oldlace', edgecolor='skyblue')

        plt.xlabel('Время')
        plt.ylabel('Значение')
        plt.title('Просмотр  влажности в теплице 1-го датчика')

        plt.savefig('graph_humidity.png')
