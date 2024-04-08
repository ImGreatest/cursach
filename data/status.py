from data.abstract.service import Service
from lib.database import connect_to_database


class StatusService(Service):
    def __init__(self):
        pass

    def __repr__(self):
        return "".format()

    def open_connection(self):
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection, cursor

    def create(self, name: str):
        conn, cur = self.open_connection()
        cur.execute("INSERT INTO status (name) VALUES (%s)", (name,))
        conn.commit()
        cur.close()
        conn.close()

    def get(self):
        conn, cur = self.open_connection()
        cur.execute("SELECT * FROM status")
        rows = {row[0]: row[1] for row in cur.fetchall()}
        cur.close()
        conn.close()
        return {
            "id": list(rows.keys()),
            "name": list(rows.values()),
        }

    def get_by_name(self, name: str):
        conn, cur = self.open_connection()
        cur.execute("SELECT * FROM status WHERE name=%s", (name,))
        rows = cur.fetchone()
        cur.close()
        conn.close()
        return {
            "id": rows[0],
            "name": rows[1],
        }

    def update(self, name: str):
        conn, cur = self.open_connection()
        cur.execute("UPDATE status SET name=%s WHERE id=%s", (name, id))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, name: str):
        conn, cur = self.open_connection()
        cur.execute("DELETE FROM status WHERE name=%s", (name,))
        conn.commit()
        cur.close()
        conn.close()
