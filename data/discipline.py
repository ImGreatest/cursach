from lib.database import connect_to_database


class DisciplineService:
    def __init__(self):
        pass

    def __repr__(self):
        return "".format()

    def open_connection(self):
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection, cursor

    def create(self, subject_code, subject_name, hours, student_id):
        conn, cur = self.open_connection()
        cur.execute(
            'INSERT INTO "discipline" (subject_code, subject_name, hours, student_id) VALUES (%s, %s, %s, %s)',
            (subject_code, subject_name, hours, student_id))
        conn.commit()
        cur.close()
        conn.close()

    def get(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "discipline"')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in rows:
            data = {
                "subject_code": row[0],
                "subject_name": row[1],
                "hours": row[2],
                "student_id": row[3]
            }
            result.append(data)
        try:
            return result
        except:
            return None

    def get_by_id(self, id):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "discipline" WHERE subject_code=%s', (id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        try:
            return {
                "subject_code": row[0],
                "subject_name": row[1],
                "hours": row[2],
                "student_id": row[3]
            }
        except:
            return None

    def update(self, id, subject_name, hours, student_id) -> None:
        conn, cur = self.open_connection()
        cur.execute(
            'UPDATE "discipline" SET subject_name=%s, hours=%s, student_id=%s WHERE id=%s',
            (subject_name, hours, student_id, id))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, id) -> None:
        conn, cur = self.open_connection()
        cur.execute('DELETE FROM "discipline" WHERE subject_code=%s', (id,))
        conn.commit()
        cur.close()
        conn.close()

    def count(self):
        conn, cur = self.open_connection()
        cur.execute(f'SELECT MAX(subject_code) FROM "discipline"')
        data = cur.fetchone()
        cur.close()
        conn.close()
        for i, v in enumerate(data):
            data = v
            break
        if data is None:
            return 0

        return data
