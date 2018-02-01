import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS grades (name TEXT, grade INTEGER)")


def populate():
    c.execute("INSERT INTO grades VALUES('Bill Murray', 77)")
    c.execute("INSERT INTO grades VALUES ('John Smith', 89)")
    conn.commit()
    c.close()
    conn.close


def dynamic_populate():
    name = input("enter name")
    grade = input("enter an integer grade")
    c.execute("INSERT INTO grades VALUES(?,?)", (name, grade))
    conn.commit()


def showall():
    c.execute("SELECT * FROM grades")
    for row in c.fetchall():
        print(row)


def delete_error():
    c.execute("DELETE FROM grades WHERE name='Error'")
    conn.commit()


def avg_grade():
    c.execute("SELECT AVG(grade) FROM grades")
    return c.fetchall()

create_table()
#dynamic_populate()
showall()
delete_error()
print(avg_grade())
conn.close()


