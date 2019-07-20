import sqlite3
def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("create table IF NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)")
    cur.execute("insert into store values('wine glass',8,10.5)")
    conn.commit()
    conn.close()
def insert_data(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("insert into store values(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()
insert_data("water glass",8,98)
def delete_data(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("delete from store where item=?",(item,))
    conn.commit()
    conn.close()
delete_data("water glass")
def update_data(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("update store set quantity=?,price=? where item=?",(quantity,price,item))
    conn.commit()
    conn.close()
update_data(11,6,"wine glass")
def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("select * from store")
    rows=cur.fetchall()
    conn.close()
    return rows
print(view())
