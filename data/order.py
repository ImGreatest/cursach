from data.abstract.service import Service
from data.interface.user_req import USER_REQ
from lib.database import connect_to_database


class OrderService(Service):
    def __init__(self):
        pass

    def __repr__(self):
        return "".format()

    def open_connection(self):
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection, cursor

    def create(self, status_id, start_order, end_order):
        conn, cur = self.open_connection()
        cur.execute('INSERT INTO "order" (status, start_order, end_order) VALUES (%s, %s, %s)',
                    (status_id, start_order, end_order))
        conn.commit()
        cur.close()
        conn.close()

    def get(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "order"')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in rows:
            user_data = {
                "id": row[0],
                "status_id": row[1],
                "start_order": row[2],
                "end_order": row[3],
                "createdAt": row[4],
                "updateAt": row[5],
                "deletedAt": row[6],
            }
            result.append(user_data)
        try:
            return result
        except:
            return None

    def get_by_id(self, id: str):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "order" WHERE id=%s', (id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        try:
            return {
                "id": row[0],
                "status_id": row[1],
                "start_order": row[2],
                "end_order": row[3],
                "createdAt": row[4],
                "updateAt": row[5],
                "deletedAt": row[6],
            }
        except:
            return None

    def get_by_status(self, status_id: str):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "order" WHERE status=%s', (status_id))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in rows:
            user_data = {
                "id": row[0],
                "status_id": row[1],
                "createdAt": row[2],
                "updateAt": row[3],
                "deletedAt": row[4],
            }
            result.append(user_data)
        try:
            return result
        except:
            return None

    def update(self, status_id, start_order, end_order, id:str) -> None:
        conn, cur = self.open_connection()
        cur.execute('UPDATE "order" SET status=%s, start_order=%s, end_order=%s WHERE id=%s',
                    (status_id, start_order, end_order, id))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, id: str) -> None:
        conn, cur = self.open_connection()
        cur.execute('DELETE FROM "order" WHERE id=%s', (id,))
        conn.commit()
        cur.close()
        conn.close()

    def count_orders(self):
        conn, cur = self.open_connection()
        cur.execute(f'SELECT COUNT(id) FROM "order"')
        data = cur.fetchone()
        cur.close()
        conn.close()
        for i, v in enumerate(data):
            data = v
            break
        if data is None:
            return 0

        return data

    def accept_orders(self):
        conn, cur = self.open_connection()
        status = 'b86e7fc4-ddb6-4e0f-915c-2553814933cc'
        cur.execute(f'SELECT * FROM "order" where "status"=status', (status,))
        data = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in data:
            user_data = {
                "id": row[0],
                "status_id": row[1],
                "createdAt": row[2],
                "updateAt": row[3],
                "deletedAt": row[4],
            }
            result.append(user_data)
        try:
            return result
        except:
            return None

    def count_accept_orders(self):
        conn, cur = self.open_connection()
        status = 'b86e7fc4-ddb6-4e0f-915c-2553814933cc'
        cur.execute(f'SELECT COUNT(id) FROM "order" where status=%s', (status,))
        data = cur.fetchone()
        cur.close()
        conn.close()
        for i, v in enumerate(data):
            data = v
            break
        if data is None:
            return 0

        return data
