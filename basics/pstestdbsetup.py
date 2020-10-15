import sqlite3


connection = sqlite3.connect('store.db')
cursor = connection.cursor()


query = 'select sqlite_version()'
cursor.execute(query)
print(cursor.fetchone())

connection.close()
