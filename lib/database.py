from decouple import config
from psycopg2 import connect

# config = dotenv_values(".env")

# def connect_to_database():
#     return connect(
#         host=config.get('DATABASE_HOST'),
#         database=config.get('DATABASE_NAME'),
#         user=config.get('DATABASE_USER'),
#         password=config.get('DATABASE_PASSWORD')
#     )

config = {
    'DATABASE_HOST': config('DATABASE_HOST'),
    'DATABASE_NAME': config('DATABASE_NAME'),
    'DATABASE_USER': config('DATABASE_USER'),
    'DATABASE_PASSWORD': config('DATABASE_PASSWORD'),
}


def connect_to_database():
    return connect(
        host=config['DATABASE_HOST'],
        database=config['DATABASE_NAME'],
        user=config['DATABASE_USER'],
        password=config['DATABASE_PASSWORD']
    )
