from lib.database import connect_to_database


class TeacherService:
    def __init__(self):
        pass

    def __repr__(self):
        return "".format()

    def open_connection(self):
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection, cursor

    def create(self, full_name, academic_degree, department_id, discipline_id):
        teacher_number = self.count() + 1
        conn, cur = self.open_connection()
        cur.execute(
            'INSERT INTO "teacher" (teacher_number, full_name, academic_degree, department_id, discipline_id) VALUES (%s, %s, %s, %s, %s)',
            (teacher_number, full_name, academic_degree, department_id, discipline_id)
        )
        conn.commit()
        cur.close()
        conn.close()

    def get(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "teacher"')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in rows:
            data = {
                "teacher_number": row[0],
                "full_name": row[1],
                "academic_degree": row[2],
                "department_id": row[3],
                "discipline_id": row[4],
            }
            result.append(data)
        try:
            return result
        except:
            return None

    def get_by_id(self, id):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "teacher" WHERE id=%s', (id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        try:
            return {
                "teacher_number": row[0],
                "full_name": row[1],
                "academic_degree": row[2],
                "department_id": row[3],
                "discipline_id": row[4],
            }
        except:
            return None

    def update(self, name: str, degree, depart, discipline) -> None:
        conn, cur = self.open_connection()
        cur.execute('UPDATE "teacher" SET full_name=%s, academic_degree=%s, department_id=%s, descipline_id WHERE id=%s',
                    (name, degree, depart, discipline, id))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, id) -> None:
        conn, cur = self.open_connection()
        cur.execute('DELETE FROM "teacher" WHERE teacher_number=%s', (id,))
        conn.commit()
        cur.close()
        conn.close()

    def count(self):
        conn, cur = self.open_connection()
        cur.execute(f'SELECT COUNT(teacher_number) FROM "teacher"')
        data = cur.fetchone()
        cur.close()
        conn.close()
        for i, v in enumerate(data):
            data = v
            break
        if data is None:
            return 0

        return data
