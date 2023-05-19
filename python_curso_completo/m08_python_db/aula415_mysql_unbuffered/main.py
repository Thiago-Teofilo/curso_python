# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os

import pymysql
import pymysql.cursors
import dotenv

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.SSDictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    # Inserindo dados
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%s, %s) '
        )
        data = ('Thiago', 20)
        result = cursor.execute(sql, data)

        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES '
            '(%(nome)s, %(idade)s) '
        )
        data2 = (
            {"nome": "Leococito", "idade": 28, },
            {"nome": "Lambda", "idade": 25, },
            {"nome": "Marcio", "idade": 37, },
        )
        result = cursor.executemany(sql, data2)

        # print(result)
    connection.commit()

    # Lendo os dados
    with connection.cursor() as cursor:
        id_query = 2
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        cursor.execute(sql, id_query)

        data_table = cursor.fetchone()

        # print(data_table)

    # Atualizando os dados
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ('Leococitus', 30, 2))

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        print("\nFor 1:")
        for row in cursor.fetchall_unbuffered():
            print(row)

            if row['id'] >= 3:
                break

        print("\nLinha pausada:", cursor.rownumber)

        print("\nFor 2:")
        [print(row) for row in cursor.fetchall_unbuffered()]

    connection.commit()
