import sqlite3
from pprint import pprint as pp


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
            create table if not exists parts(id INTEGER PRIMARY KEY AUTOINCREMENT, 
            part text,
            customer text, 
            retailer text, 
            price text)
            """
        )
        self.conn.commit()

    def insert(self, part, customer, retailer, price):
        query = 'insert into parts (part, customer, retailer, price) values (?, ?, ?, ?)'
        self.cur.execute(query, (part, customer, retailer, price))
        self.conn.commit()

    def fetch(self):
        query = 'select * from parts'
        self.cur.execute(query)
        rows = [[column_info[0] for column_info in self.cur.description]]
        rows.extend(self.cur.fetchall())
        return rows

    def remove(self, part_id):
        query = 'delete from parts where id = ?'
        self.cur.execute(query, (part_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    db = Database('store.db')

    # rows = [("4db DDR4 Ram", 'John Doe', 'Microcenter', '160'),
    #         ('Asus Mobo', 'Mike Harry', 'Microcenter', '360'),
    #         ('500W PSU', 'Larry Johnson', "Newengg", '70')]
    #
    # for row in rows:
    #     db.insert(*row)
    pp(db.fetch())
