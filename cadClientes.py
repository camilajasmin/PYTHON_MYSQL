import mysql.connector as mc
# Estabelecar a conexao com o banco
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="1234.abcd",
    database="BANCO"
    )

#verificar se a conexao foi estabelecida
print(cx)

# Criação de variáveis para o usuário passar os dados do cliente  para o cadastroca
nome        = input("Digite o nome do cliente:")
email       = input("Digite o email do cliente:")
telefone    = input("Digite o telefone do cliente:")

cursor = cx.cursor()
cursor.execute("insert into CLIENTES(NOMEcliente, EMAILcliente, TELEFONEcliente)values('"+nome+"','"+email+"','"+telefone+"')")
# Confirmar a insersão dos dados na tabela
print(cx.commit())