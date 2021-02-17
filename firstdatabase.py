import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="",database="firstpy")

cursor=db.cursor()

#cursor.execute("CREATE DATABASE firstpy")
cursor.execute("CREATE TABLE student (s_id INT NULL AUTO_INCREMENT,PRIMARY KEY (s_id),email VARCHAR(255),UNIQUE KEY(email),name VARCHAR(225))")
#.cursor.execute("DROP TABLE student")
