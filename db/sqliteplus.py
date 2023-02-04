"""
Прога для преобразования данных полученных из БД в словарь, где ключами выступают названия полей.
Версия 1.0.0
Написана prok0l:    https://github.com/prok0l/

Инструкция: обернуть функцию connect в декоратор sqlite_dict
"""


def sqlite_dict(func):
    def wrapper(self, text_for_execute: str, fetchall: bool = False, params: tuple = (), off=True):
        if not fetchall or off:
            # запрос без fetchall или сигнал выключения декоратору
            return func(self, text_for_execute=text_for_execute, fetchall=fetchall, params=params)

        # сбор значений
        values = func(self, text_for_execute=text_for_execute, fetchall=fetchall, params=params)

        if text_for_execute.split()[1] == "*":
            # обработка симовла * (SELECT * ....)
            name_of_table = text_for_execute.split("FROM")[1].split()[0].rstrip(";")
            if name_of_table == "?":
                name_of_table = params[0]
            names_not_formated = func(self, text_for_execute=f"pragma table_info({name_of_table});", fetchall=True)
            names = [x[1] for x in names_not_formated]
        else:
            # обработка при передаче нужных полей (SELECT a, b, c FROM ...)
            names_not_formated = text_for_execute.lstrip("SELECT ").split("FROM")[0].split(",")
            names = [x.strip() for x in names_not_formated]
        m = [{names[i]: y[i] for i in range(0, len(y))} for y in values]
        return m

    return wrapper
