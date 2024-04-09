from data.abstract.service import Service
from data.interface.user_req import USER_REQ
from lib.database import connect_to_database


class UserService(Service):
    def __init__(self):
        pass

    def __repr__(self):
        return "".format()

    def open_connection(self):
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection, cursor

    def create(self, data: dict):
        conn, cur = self.open_connection()
        cur.execute('INSERT INTO "user" ("name", "role", "password", "status") VALUES (%s, %s, %s, %s)',
                    (data['name'], data['role'], data['password'], data['status']))
        conn.commit()
        cur.close()
        conn.close()

    def get(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "user"')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in rows:
            user_data = {
                "id": row[0],
                "role": row[1],
                "createdAt": row[2],
                "updateAt": row[3],
                "deletedAt": row[4],
                "password": row[5],
                "status": row[6],
                "name": row[7],
            }
            result.append(user_data)
        try:
            return result
        except:
            return None

    def count(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT COUNT(id) FROM "user"')
        rows = cur.fetchone()
        cur.close()
        conn.close()
        try:
            return rows
        except:
            return None

    def get_by_id(self, id: str):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "user" WHERE id=%s', (id,))
        rows = cur.fetchone()
        cur.close()
        conn.close()
        try:
            return {
                "id": rows[0],
                "name": rows[7],
                "role": rows[1],
                "createdAt": rows[2],
                "updateAt": rows[3],
                "deletedAt": rows[4],
                "password": rows[5],
                "status": rows[6],
            }
        except:
            return None

    def get_by_name(self, name: str, password: str):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "user" WHERE "name"=%s AND "password"=%s', (name, password))
        rows = cur.fetchone()
        print('sss', rows)
        cur.close()
        conn.close()
        try:
            return {
                "id": rows[0],
                "name": rows[-1],
                "role": rows[1],
                "createdAt": rows[2],
                "updateAt": rows[3],
                "deletedAt": rows[4],
                "password": rows[5],
                "status": rows[6],
            }
        except:
            return None

    def update(self, data: USER_REQ, id:str) -> None:
        conn, cur = self.open_connection()
        cur.execute('UPDATE "user" SET name=%s, role=%s, status=%s WHERE id=%s',
                    (data['name'], data['role'], data['status'], id))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, id: str) -> None:
        conn, cur = self.open_connection()
        cur.execute('DELETE FROM "user" WHERE id=%s', (id,))
        conn.commit()
        cur.close()
        conn.close()
