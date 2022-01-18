import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="db_demos",
    user="postgres",
    password="1123QwER")

cursor = connection.cursor()
cursor.execute('''
SELECT CONCAT(e.name, ' (', e.job_title, ')'),
       CONCAT(m.name, ' (', m.job_title, ')')
FROM employees e
JOIN employees m
    ON e.manager_id = m.id;
''')


class Employee:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

    def __str__(self):
        return f'{self.name}, {self.manager}'


employees = [Employee(*row) for row in cursor.fetchall()]
print(employees)

connection.close()

# ORM - Object-Relational Mapping
