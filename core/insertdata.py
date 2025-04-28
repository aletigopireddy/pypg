import psycopg2

conn = psycopg2.connect(database="companydb", user = "postgres", password = "zapcom1234", host = "127.0.0.1", port = "5433")

print ("Opened database successfully")

cur=conn.cursor()
table_name='python_code'
cur.execute('''INSERT INTO '''+table_name+'''(name) SELECT 'stundent-'||n FROM  generate_series(1,100)n;''')
print("data into table:",table_name,"inserted successfully")

conn.commit()
conn.close()