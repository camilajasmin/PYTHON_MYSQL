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