from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class DataEntry(FlaskForm):
    id = StringField("Номер датчика: ", validators=[Length(min=1)])
    temperature = StringField("Температура: ", validators=[Length(min=2, max=3)])
    humidification = StringField("Влажность: ", validators=[Length(min=2, max=3)])
    submit = SubmitField("Внести данные")


class Control(FlaskForm):
    hum_on = SubmitField('Увалжанить')
    hum_off = SubmitField('Прекратить увдажнение')
    door_open = SubmitField('Открыть')
    door_close = SubmitField('Заркыть')
    watringa1 = SubmitField('Полить (Бороздка №1)')
    watringa1_off = SubmitField('Выключить полив (Бороздка №1)')
    watringa2 = SubmitField('Полить (Бороздка №2)')
    watringa2_off = SubmitField('Выключить полив (Бороздка №1)')
    watringa3 = SubmitField('Полить (Бороздка №3)')
    watringa3_off = SubmitField('Выключить полив (Бороздка №1)')
    watringa4 = SubmitField('Полить (Бороздка №4)')
    watringa4_off = SubmitField('Выключить полив (Бороздка №1)')
    watringa5 = SubmitField('Полить (Бороздка №5)')
    watringa5_off = SubmitField('Выключить полив (Бороздка №1)')
    watringa6 = SubmitField('Полить (Бороздка №6)')
    watringa6_off = SubmitField('Выключить полив (Бороздка №1)')
    watringa_on_all = SubmitField('Включить полив всех бороздок')
    watringa_off_all = SubmitField('Выключить полив всех бороздок')


class Recharging(FlaskForm):
    recharging = SubmitField("Обновить")
