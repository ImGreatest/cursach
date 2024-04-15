from lib.database import connect_to_database


class StudentService:
    def __init__(self):
        pass

    def __repr__(self):
        return "".format()

    def open_connection(self):
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection, cursor

    def create(self, id, number_of_student_book, full_name, group_name, city):
        conn, cur = self.open_connection()
        cur.execute(
            'INSERT INTO "student" (id, number_of_student_book, full_name, group_name, city) VALUES (%s, %s, %s, %s, %s)',
            (id, number_of_student_book, full_name, group_name, city))
        conn.commit()
        cur.close()
        conn.close()

    def get(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "student"')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in rows:
            data = {
                "id": row[0],
                "number_book": row[1],
                "full_name": row[2],
                "group_name": row[3],
                "city": row[4],
            }
            result.append(data)
        try:
            return result
        except:
            return None

    def get_by_id(self, id):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "student" WHERE id=%s', (id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        try:
            return {
                "id": row[0],
                "number_book": row[1],
                "full_name": row[2],
                "group_name": row[3],
                "city": row[4],
            }
        except:
            return None

    def update(self, id, number_of_student_book, full_name, group_name, city) -> None:
        conn, cur = self.open_connection()
        cur.execute(
            'UPDATE "student" SET full_name=%s, academic_degree=%s, department_id=%s, descipline_id WHERE id=%s',
            (number_of_student_book, full_name, group_name, city, id))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, id) -> None:
        conn, cur = self.open_connection()
        cur.execute('DELETE FROM "student" WHERE id=%s', (id,))
        conn.commit()
        cur.close()
        conn.close()

    def count(self):
        conn, cur = self.open_connection()
        cur.execute(f'SELECT MAX(id) FROM "student"')
        data = cur.fetchone()
        cur.close()
        conn.close()
        for i, v in enumerate(data):
            data = v
            break
        if data is None:
            return 0

        return data
