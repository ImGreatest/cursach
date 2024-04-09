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