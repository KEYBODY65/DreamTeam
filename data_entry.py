from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class DataEntry(FlaskForm):
    id = StringField("Номер датчика: ", validators=[Length(min=1)])
    temperature = StringField("Температура: ", validators=[Length(min=2, max=3)])
    humidification = StringField("Влажность: ", validators=[Length(min=2, max=3)])
    submit = SubmitField("Внести данные")


class Control(FlaskForm):
    fork_drive_submit = SubmitField("Открыть дверцу / Закрыть дверцу")
    watering_submit = SubmitField("Включить Полив / Выключить полив")
    total_hum_submit = SubmitField("Увалжанить / Не Увлажнять")


class Recharging(FlaskForm):
    recharging = SubmitField("Обновить")
