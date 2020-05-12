import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabase"
)

mycursor = mydb.cursor()


mycursor.execute("select * from pegawai")

result = mycursor.fetchall()
nama = [item[1] for item in result]
# # alamat = [item[id] for item in result]
print(nama)
alamat = [item[2] for item in result]
print(alamat)
# for i in result:
    # print(i[1], i[2])
