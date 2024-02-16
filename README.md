# Conexão do Python com o MySQL

!["Imagem da Conexao Python com MySQL"](https://www.learntek.org/blog/wp-content/uploads/2019/06/Mysql-python.png)

## Drive de comunicação com o MySQL
Para estabelecer a comunicação entre o pyhton e o banco de dados mysql, iremos usar o seguinte drive: 
<a href="https://pypi.org/project/mysql-connector-python/#history">https://pypi.org/project/mysql-connector-python/#history</a>

### Comando para Instalar o drive
```python
    python -m pip install mysql-connector-python
```

### Configuração do Banco de Dados MySQL
O nosso banco de dados está em um container de docker. Para acessá-lo será necessário criar o container, então faremos os seguintes comandos em um servidor fedora com o docker instalado.

#### Criação do volume
```shell
mkdir dadosClientes
```
#### Criação do container

<center>
    <img src="https://storage.googleapis.com/eti-academy/courses/curso-de-docker.png" height="200" width="200">
</center>

```shell
docker run --name srvmysql -v ~/dadosClientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD=1234.abcd -d mysql
```
#### Criação do banco de dados e da tabela de clientes

```sql
    create database BANCO;
    use BANCO;

create table CLIENTES(
		CLIENTESid int auto_increment primary key,
        NOMEcliente varchar(50) not null,
        EMAILcliente varchar(100) not null unique,
        TELEFONEcliente varchar(20) not null
        );
```

#### Arquivo de clientes.py
```python
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
```

#### Arquivo de cadstro de clientes: cadClientes.py
```python
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

# Criação de variáveis para o usuário passar os dados do cliente  para o cadastro
nome        = input("Digite o nome do cliente:")
email       = input("Digite o email do cliente:")
telefone    = input("Digite o telefone do cliente:")

cursor = cx.cursor()
cursor.execute("insert into CLIENTES(NOMEcliente, EMAILcliente, TELEFONEcliente)values('"+nome+"','"+email+"','"+telefone+"')")
# Confirmar a insersão dos dados na tabela
print(cx.commit())
```

#### Arquivo de atualização: upClientes.py 
```python 
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
```