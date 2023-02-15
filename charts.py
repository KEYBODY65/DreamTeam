import pandas as pd
import matplotlib.pyplot as plt


class makes_charts:
    def make_chart_for_temperature(data, time):
        datas = []
        times = []
        datas.append(data)
        times.append(time)
        print(times)
        if time == '00:00:00':
            datas.clear()
            times.clear()
        df = pd.DataFrame({
            'Время': times,
            'Температура, °C': datas,
        })
        ax = df.plot(x="Время", y="Температура, °C", kind="bar", color="orangered")

        ax.set_ylabel('Значение')

        ax.grid()

        plt.title('Просмотр температуры 1-го датчика')

    def make_chart_for_humidification(data, time):
        datas = []
        times = []
        datas.append(data)
        times.append(time)
        if time == '00:00:00':
            datas.clear()
            times.clear()
        df = pd.DataFrame({
            'Время': times,
            'Влажность, кг/м3': datas,
        })
        ax = df.plot(x="Время", y="Влажность, кг/м3", kind='bar')

        plt.title('Просмотр  влажности в теплице 1-го датчика')

        ax.grid()

        ax.set_ylabel('Значение')

        plt.show()
