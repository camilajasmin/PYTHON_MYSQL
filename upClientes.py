import mysql.connector as mc 
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="1234.abcd",
    database="BANCO"
    )


cursor = cx.cursor()
cursor.execute("Select * from CLIENTES")
for i in cursor:
    print(i)

print("O que você deseja atualizar no cadastro?")
print("1 - para nome")
print("2 - para email") 
print("3 - para telefone") 

option  = input("Digite a opção desejada: ")
ID      = input("Agora digite o id do cliente:")
dado    = input("Digite a nova informação: ")

if(option == "1"):
    cursor.execute("update CLIENTES set NOMEcliente='"+dado+"' where CLIENTESid="+ID)
elif(option == "2"):
    cursor.execute("update CLIENTES set EMAILcliente='"+dado+"' where CLIENTESid="+ID)
elif(option == "3"):
    cursor.execute("update CLIENTES set TELEFONEcliente='"+dado+"' where CLIENTESid="+ID)
else:
    print("Opção inválida.")

cx.commit()