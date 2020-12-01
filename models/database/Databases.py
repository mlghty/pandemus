import sqlite3

class GlobalDataBase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS global (id INTEGER PRIMARY KEY, date integer, total integer)')
        self.conn.commit()

    def fetch(self):
        self.cursor.execute('SELECT * from global')
        return self.cursor.fetchall()

    def insert(self, date, total):
        self.cursor.execute('INSERT INTO global VALUES (NULL, ?, ?)', (date, total))
        self.conn.commit()
    
    def remove(self, id):
        self.cursor.execute('DELETE FROM global WHERE id=?', (id))
        self.conn.commit()
    
    def update(self, id, date, total):
        self.cursor.execute('UPDATE global SET date=?, total=? WHERE id=?', (date, total, id))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()

