import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="01777tsr"
  database = "foundation" 
) 

my_cursor = mydb.cursor()

data = my_cursor.execute("select * from users_info")
data = data.fetchall()
print(mydb)