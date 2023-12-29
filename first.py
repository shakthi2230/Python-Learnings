import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shakthi/22z4",
  database="sakthivel"
)

mycursor=mydb.cursor()

# mycursor.execute("SHOW DATABASES ")
# mycursor.execute("CREATE TABLE CUSTOMERS (name VARCHAR(255),address VARCHAR(255))")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")
# mycursor.execute("CREATE TABLE customerss (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("")


#_________________________________
#ifff alreade exiist the table 
# mycursor.execute("alter table customers add column id int auto_increment primary key")
# sql="insert into customers (name,address) values(%s,%s)"
# val=("jhon","india")
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql,val)

# mydb.commit()
# # print(mycursor.rowcount, "record inserted.")
# print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.execute("select * from customers")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)
