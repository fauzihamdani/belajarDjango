import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO pegawai (nama, alamat) VALUES (%s, %s)"
val = ("fauzi", "kedunganyar 7 no.33")
mycursor.execute(sql,val)

mydb.commit()
print("1 record inserted, ID:", mycursor.rowcount)
