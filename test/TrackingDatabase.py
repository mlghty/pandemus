import sqlite3

conn = sqlite3.connect("tracking-database.db")
# conn = sqlite3.connect(":memory:")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE national (
        date integer,

        positive integer,
        negative integer,
        recovered integer,
        death integer,

        positiveIncrease integer,
        negativeIncrease integer,
        recoveredIncrease integer,
        deathIncrease integer
    )""")

cursor.execute("SELECT * FROM national WHERE date='20201125'")

conn.commit()
conn.close()