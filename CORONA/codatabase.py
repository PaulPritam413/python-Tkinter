#22.10.22
import mysql.connector
import credential as cr

#creating database object
mydb=mysql.connector.connect(host=cr.host,user=cr.user,passwd=cr.pas,database=cr.data)
#creating cursor object
mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE register(name varchar(50),username varchar(50),contact varchar(12),email varchar(50),age varchar(3),gender varchar(10),password varchar(50))")

mycursor.execute("CREATE TABLE data(id integer NOT NULL,name varchar(50),age varchar(10),gender varchar(20),blood varchar(5),DOA varchar(10),address varchar(100),PHno varchar(50),PRIMARY KEY(id))")

mydb.commit()

mydb.close()