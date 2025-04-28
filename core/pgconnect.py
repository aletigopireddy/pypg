import psycopg2

conn = psycopg2.connect(database="companydb", user = "postgres", password = "", host = "127.0.0.1", port = "5433")

print ("Opened database successfully")

cur=conn.cursor()
cur.execute('''CREATE TABLE python_code(id serial primary key,name text);''')
print("table created successfully")

conn.commit()
conn.close()