import psycopg2
from config import *

try:
    #коннект
    connection = psycopg2.connect(
        port=port,
        dbname=db_name,
        password=password,
        user=user,
        host=host
    )

    connection.autocommit = True

    print('СОЕДИНЕНИЕ ОТКРЫТО!')

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f'Server verison: {cursor.fetchone()}') #fetchone вернет кортэж или None

        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """CREATE TABLE users(
        #             id SERIAL PRIMARY KEY,
        #             first_name VARCHAR(50) NOT NULL,
        #             nick_name VARCHAR(50) NOT NULL);"""
        #     )   

        # print('Table created!')

        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """INSERT INTO users (first_name, nick_name) VALUES
        #         ('OleG', 'KenZO');"""
        #     )   

        # print('[INFO] User was created')

        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """SELECT nick_name FROM users WHERE first_name = 'OleG';"""
        #     )

        #     print(cursor.fetchone()[0])

        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE users;")

        print('[INFO] Table was dropped')

except Exception as _ex:
    print('[INFO] Error', _ex)
finally:
    if connection:
        connection.close()
        print('СОЕДИНЕНИЕ ЗАКРЫТО!')