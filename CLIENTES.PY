# importanto a biblioteca de conexão com o banco de dados mysql

# vamos adicionar um alias a biblioteca
import mysql.connector as mc 

# vamos estabelecer a cenexão com o banco de dados e para tal
# iremos passr os seguintes dados
# servidor, porta, usuário, senha, banco
conexao = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="1234.abcd",
    database="BANCO"
    )

# Estamos testando utilizando o "print" para a exibição do id da conexao. 
# Caso exiba uma pilha de erros, então você temum erro na linha de conexão.
print(conexao)

# Para se movimentar dentro da estrutura de banco 
# de dados e retornar dos dados necessários
# iremos criar um cursor.
cursor = conexao.cursor()

# vamos executar um comando usando o cursor
# cursor.execute("Create database Ola")

# cursor.execute("insert into CLIENTES(NOMEcliente, EMAILcliente, TELEFONEcliente)value('Veronica Chauca','veronica@uol.com.br','(11)9997-6665')")

# Vamos selecionar todos os dados da tabela CLIENTES
cursor.execute("Select * from BANCO.CLIENTES")
print(cursor)

for c in cursor:
    print (f"ID do cliente: {c[0]}")
    print (f"NOME do cliente: {c[1]}")
    print (f"E-MAIL do cliente: {c[2]}")
    print (f"TELEFONE do cliente: {c[3]}")