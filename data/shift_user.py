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

    def create(self):
        pass

    def get(self):
        pass

    def get_by_id(self, service_item_id: str):
        pass

    def update(self):
        pass

    def delete(self):
        pass
