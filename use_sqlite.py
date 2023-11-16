from Darkoob_sqlite import DarkoobSQLIT
orm = DarkoobSQLIT()

orm.create_table(table_name='users', id='INTEGER PRIMARY KEY', name='TEXT', age='INTEGER')
orm.insert('users', name='John', age=25)
print(orm.select('users', name='John'))
orm.update('users', {'age': 30}, name='John')
orm.delete('users', name='John')
orm.close_connection()

