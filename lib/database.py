from dotenv import dotenv_values
from psycopg2 import connect

config = dotenv_values(".env")


def connect_to_database():
    return connect(
        host=config.get('DATABASE_HOST'),
        database=config.get('DATABASE_NAME'),
        user=config.get('DATABASE_USER'),
        password=config.get('DATABASE_PASSWORD')
    )

#
# # connect to database postgresql
# # Для коннекта к определенной бд меняй строки внутри -> conn = psycopg2.connect
# def connection():
#     conn = connect(host='localhost', database='gameshop', user='postgres', password='889988')
#
#     return conn
#
#
# # ---------------------------------------------------------------------------
# # SQL Запрос к бд чтобы вытащить данные из неё
# # table -> название таблицы (string)
# # specify -> уточнение к запросу, указывается столбец (string)
# # если нужно вытащить всё -> specify=None
# def SelectReq(table, specify):
#     if specify is None: specify = '*'
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute(f'SELECT {specify} FROM {table}')
#     data = cur.fetchall()
#     cur.close()
#     conn.close()
#
#     return data
#
#
# # ---------------------------------------------------------------------------
# # SQL Запрос к бд добавление элементов
# # парамент table -> название таблицы (string)
# # id -> индификация записи в таблицы (int) ↓
# # nomenation -> название продукта (string(max(50) ↓
# # description -> описание продукта (string(max(200) ↓
# # cost -> цена продукта (int(max 2 147 483 647) ↓
# # data_start -> дата выпуска (data) example -> data_start='01-01-2000' (day-month-year)
# # publisher -> название издателя (string(max(50)
# # developer -> название разработчика (string(max(50)
# # key -> ключ продукта как steam (буквы и числа) (string(max(20)
# def InsertIntoReq(table, id, nomenation, description, cost, data_start, publisher, developer, key, genre):
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute(f'INSERT INTO {table}(id, nomenation, description, cost, data_start, publisher, developer, key_good, genre)' 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, nomenation, description, cost, data_start, publisher, developer, key, genre))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# #----------------------------------------------------------------------------
# # удаление записи из бд (удаление по id)
# # table -> название таблицы (string)
# # id -> значение id
# def DeleteReq(table=str, id=int):
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute(f'DELETE FROM {table} WHERE id={id}')
#     conn.commit()
#     cur.close()
#     conn.close()
#
# def DeleteUserReq(table=str, id=int):
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute(f'DELETE FROM {table} WHERE id={id}')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# # ---------------------------------------------------------------------------
# # запрос sql макс. значение id
# # table -> название таблицы (string)
# def CountIdReq(table=str):
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute(f'SELECT max(id) FROM {table}')
#     data = cur.fetchone()
#     cur.close()
#     conn.close()
#     for i, v in enumerate(data):
#         data = v
#         break
#     if data is None: data = 0
#
#     return data
#
#
# def InsertSingle(table=str, id=str):
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute(f'INSERT INTO {table}(id)' 'VALUES(%s)', (id))
#     conn.commit()
#     cur.close()
#     conn.close()
#
# def InsertSingleCustomer(table=str, id=str, name=str):
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute(f'INSERT INTO {table}(id, nomenation)' 'VALUES (%s, %s)', (id, name))
#     conn.commit()
#     cur.close()
#     conn.close()
#
# def DeleteFrom(table=str):
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute(f'DELETE FROM {table}')
#     conn.commit()
#     cur.close()
#     conn.close()
#
# def SelectWhereReq(table=str, specify=str):
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute(f'SELECT * FROM {table} where id={specify}')
#     data = cur.fetchall()
#     cur.close()
#     conn.close()
#
#     return data
#
# def SelectWhereGenreReq(table=str, specify=str):
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute(f'SELECT * FROM {table} where genre={specify}')
#     data = cur.fetchall()
#     cur.close()
#     conn.close()
#
#     return data
#
