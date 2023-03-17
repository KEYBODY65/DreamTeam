from db.sqliteplus import sqlite_dict
import sqlite3


class Database_API:
    def __init__(self, name_db):
        self.name_db = name_db

    @sqlite_dict
    def connect(self, text_for_execute: str, fetchall: bool = False, params: tuple = ()):
        with sqlite3.connect(self.name_db) as conn:
            conn.cursor()
            if fetchall:
                return conn.execute(text_for_execute, params).fetchall()
            else:
                conn.execute(text_for_execute, params)
                conn.commit()

    def create_tables(self):
        self.connect(
            'CREATE TABLE IF NOT EXISTS sensor_id (name TEXT, id int, CONSTRAINT sensor_id_pk PRIMARY KEY (id));')
        self.connect(
            'CREATE TABLE IF NOT EXISTS sensor_values (id_sensor int, id int, temperature real, hum real, hum_ground real, n_time time, CONSTRAINT'
            ' sensor_values_pk PRIMARY KEY (id), CONSTRAINT sensor_id_fk FOREIGN KEY (id_sensor) REFERENCES sensor_id(id));')
        self.connect('INSERT INTO sensor_id (name, id) VALUES(\'humidification_sensor1\', 0);')
        self.connect('INSERT INTO sensor_id (name, id) VALUES(\'tem_sensor1\', 1);')
        self.connect('INSERT INTO sensor_id (name, id) VALUES(\'humidification_sensor2\', 2);')
        self.connect('INSERT INTO sensor_id (name, id) VALUES(\'tem_sensor2\', 3);')
        self.connect('INSERT INTO sensor_id (name, id) VALUES(\'humidification_sensor3\', 4);')
        self.connect('INSERT INTO sensor_id (name, id) VALUES(\'tem_sensor3\', 5);')
        self.connect('INSERT INTO sensor_id (name, id) VALUES(\'humidification_sensor4\', 6);')
        self.connect('INSERT INTO sensor_id (name, id) VALUES(\'tem_sensor4\', 7);')
        self.connect('INSERT INTO sensor_id (name, id) VALUES(\'auto_door\', 8);')
        self.connect('INSERT INTO sensor_id (name, id) VALUES(\'watringa\', 9);')

    def create_recort(self, id_sensor: int, temperature: float, hum: float, hum_ground: float):
        last_id = self.connect('SELECT id+1 FROM sensor_values ORDER BY id DESC LIMIT 1;', fetchall=True)
        last_id = 0 if last_id == [] else last_id[0][0]
        self.connect(
            'INSERT INTO sensor_values (id_sensor, id, temperature, hum, hum_ground, n_time) VALUES(?, ?, ?, ?, ?, TIME(\"now\", \"+3 hours\"));',

            params=(id_sensor, last_id, temperature, hum, hum_ground))

    def get_values(self, id_sensor):
        data = self.connect("SELECT * FROM sensor_values WHERE id_sensor=?", params=(id_sensor,), off=False,
                            fetchall=True)

        return data

# d = Database_API('database.db')
# d.create_tables()
# for i in range(1, 6):
#     print(d.get_values(i))
# d.connect("SELECT * FROM sensor_values", off=False, fetchall=True)
# d.create_recort(1, 27.3)
