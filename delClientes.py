import mysql.connector as mc

con = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="1234.abcd",
    database="BANCO"
    )

cursor =con.cursor()
cursor.execute("Select * from CLIENTES")
for c in cursor:
    print(c)

id = input("Digite o id do cliente o qual deseja apagar: ")
rs = input("Você realmente deseja deletar o cadstro deste cliente?: ")

if(rs == "s" or rs=="S"):
    cursor.execute("delete from CLIENTES where CLIENTESid="+id)
    con.commit()
else:
    print("Okay, nada foi feito!")