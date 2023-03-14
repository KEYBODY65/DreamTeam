from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class DataEntry(FlaskForm):
    idi = StringField("Номер датчика: ", validators=[Length(min=1)])
    temperature = StringField("Температура: ", validators=[Length(min=2, max=3)])
    humidification = StringField("Влажность: ", validators=[Length(min=2, max=3)])
    humidificationground = StringField("Влажность почвы: ", validators=[Length(min=2, max=3)])
    submit = SubmitField("Внести данные")


class Entry_Lims(FlaskForm):
    T = StringField("T")
    H = StringField("H%")
    Hb = StringField("Hb%")
    Submit_button = SubmitField("Указать")


class Control(FlaskForm):
    hum_on = SubmitField('Увалжанить')
    hum_off = SubmitField('Прекратить увдажнение')
    door_open = SubmitField('Открыть')
    door_close = SubmitField('Заркыть')
    watringa_all_on = SubmitField('Полить все Бороздки')
    watringa_all_off = SubmitField('Выключить полив всех бороздок')
    idi_of_wtringa = StringField('Номер бороздки: ', validators=[Length(min=1)])
    watringa_on = SubmitField('Включить полив этой бороздки')
    watringa_off = SubmitField('Выключить полив этой бороздки')
