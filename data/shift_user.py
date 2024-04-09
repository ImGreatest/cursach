from data.abstract.service import Service
from lib.database import connect_to_database


class ShiftUserService(Service):
    def __init__(self):
        pass

    def __repr__(self):
        return "".format()

    def open_connection(self):
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection, cursor

    def create(self, shift, user):
        conn, cur = self.open_connection()
        cur.execute('INSERT INTO "shift_user" (id_shift, id_user) VALUES (%s, %s)', (shift, user))
        conn.commit()
        cur.close()
        conn.close()

    def get(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "shift_user"')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in rows:
            user_data = {
                "id_shift": row[0],
                "id_user": row[1],
            }
            result.append(user_data)
        try:
            return result
        except:
            return None

    def get_by_id(self, id: str):
        conn, cur = self.open_connection()
        cur.execute("SELECT * FROM shift_user WHERE id_shift=%s", (id,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in rows:
            user_data = {
                "id_shift": row[0],
                "id_user": row[1],
            }
            result.append(user_data)
        try:
            return result
        except:
            return None

    def count(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT COUNT(id_shift) FROM "shift_user"')
        rows = cur.fetchone()
        cur.close()
        conn.close()
        try:
            return rows
        except:
            return None
