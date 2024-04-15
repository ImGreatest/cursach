from lib.database import connect_to_database


class DepartmentService:
    def __init__(self):
        pass

    def __repr__(self):
        return "".format()

    def open_connection(self):
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection, cursor

    def create(self, id, name, phone):
        print(id)
        conn, cur = self.open_connection()
        cur.execute(
            'INSERT INTO "department" (id, name, phone) VALUES (%s, %s, %s)',
            (id, name, phone))
        conn.commit()
        cur.close()
        conn.close()

    def get(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "department"')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in rows:
            data = {
                "id": row[0],
                "name": row[1],
                "phone": row[2]
            }
            result.append(data)
        try:
            return result
        except:
            return None

    def get_by_id(self, id):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "department" WHERE id=%s', (id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        try:
            return {
                "id": row[0],
                "name": row[1],
                "phone": row[2]
            }
        except:
            return None

    def update(self, id, name, phone) -> None:
        conn, cur = self.open_connection()
        cur.execute(
            'UPDATE "department" SET "name"=%s, "phone"=%s, WHERE id=%s',
            (name, phone, id))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, id) -> None:
        conn, cur = self.open_connection()
        cur.execute('DELETE FROM "department" WHERE id=%s', (id,))
        conn.commit()
        cur.close()
        conn.close()

    def count(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT MAX("id") FROM "department"')
        data = cur.fetchone()
        cur.close()
        conn.close()
        for i, v in enumerate(data):
            data = v
            break
        if data is None:
            return 0

        return data
