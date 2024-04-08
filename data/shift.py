from data.abstract.service import Service
from data.interface.shift_req import SHIFT_REQ
from lib.database import connect_to_database


class ShiftService(Service):
    def __init__(self):
        pass

    def __repr__(self):
        return "".format()

    def open_connection(self):
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection, cursor

    def create(self, data: SHIFT_REQ):
        conn, cur = self.open_connection()
        cur.execute('INSERT INTO shift (date_shift, start_shift, end_shift) VALUES (%s, %s, %s)', (data['date_shift'],
                                                                                                   data['start_shift'],
                                                                                                   data['end_shift']))
        conn.commit()
        cur.close()
        conn.close()

    def get(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM shift')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_by_id(self, id: str):
        conn, cur = self.open_connection()
        cur.execute("SELECT * FROM shift WHERE id=%s", (id,))
        rows = cur.fetchone()
        cur.close()
        conn.close()
        return {
            "id": rows[0],
            "date_shift": rows[1],
            "start_shift": rows[2],
            "end_shift": rows[3]
        }

    def update(self, data: SHIFT_REQ):
        conn, cur = self.open_connection()
        cur.execute("UPDATE shift SET date_shift=%s, start_shift=%s, end_shift=%s WHERE id=%s", (data['date_shift'],
                                                                                                 data['start_shift'],
                                                                                                 data['end_shift'],
                                                                                                 data['id']))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, id: str):
        conn, cur = self.open_connection()
        cur.execute("DELETE FROM shift WHERE id=%s", (id,))
        conn.commit()
        cur.close()
        conn.close()
