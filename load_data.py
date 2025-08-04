import sqlite3
import pandas as pd
users_df = pd.read_csv("users.csv")
orders_df = pd.read_csv("orders.csv")
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()
cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS users(
                user_id integer primary key,
                first_name text,
                last_name text,
                email text unique,
                gender text,
                age integer,
                city text,
                state text,
                postal_code text,
                street text,
                country text,
                latitude real,
                longitude real,
                sigup_date text);
                """)
              
cursor.execute("""
              CREATE TABLE IF NOT EXISTS orders(
                order_id integer primary key,
                user_id integer,             
                status text,
                gender text,
                create_at text,
                returned_at text,
                shipped_at text,
                delivered_at text,                          
                num_of_item integer,
                foreign key(user_id)references users(user_id));
                             """ )
users_df.to_sql("users",conn, if_exists="replace",index=False)
orders_df.to_sql("orders",conn, if_exists="replace",index=False)
print("\n sample users:")
for row in cursor.execute("select*from users limit 5;"):
    print(row)
print("\n sample users:")
for row in cursor.execute("select*from orders limit 5;"):
    print(row)
conn.commit()
conn.close()