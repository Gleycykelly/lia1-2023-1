
#Nome: Gleycykelly Syssy Indymayer Carnot Amaro
#Matrícula: 201808731

import pandas as pd

import psycopg2 as pg
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:123456@localhost/livraria')
print(engine)

query = "SELECT * FROM venda"

df = pd.read_sql_query(query, con=engine)
print(df)

conn = pg.connect(user = 'postgres',
                  password = '123456',
                  host = 'localhost',
                  port = '5432',
                  database = 'livraria')


print(conn.info)


print(conn.status)

cursor = conn.cursor()


# Insere um novo cliente
nomeCliente = input("Digite o nome do cliente: ")
endereco = input("Digite o endereço do cliente: ")
cursor.execute("insert into cliente (cli_nome, cli_endereco) values ('{nomeCliente}', '{endereco}')".format(nomeCliente = nomeCliente, endereco = endereco))
conn.commit()

query = "SELECT * FROM cliente"

df = pd.read_sql_query(query, con=engine)
print(df)

# Insere um novo livro
livro = input("Digite o nome do livro: ")
isbn = input("Digite o isbn do livro: ")
cursor.execute("insert into livro (liv_titulo, liv_isbn) values ('{liv_titulo}', '{liv_isbn}')".format(liv_titulo = livro, liv_isbn = isbn))
conn.commit()

query = "SELECT * FROM livro"

df = pd.read_sql_query(query, con=engine)
print(df)

# Insere uma nova venda
valor = input("Digite o valor da venda: ")
frete = input("Digite o valor do frete: ")
idLivro = input("Digite o id do livro: ")
idCliente = input("Digite o id do cliente: ")
cursor.execute("insert into venda (ven_valor, ven_frete, liv_id, cli_id) values ('{ven_valor}', '{ven_frete}', '{liv_id}', '{cli_id}')"
               .format(ven_valor = valor, ven_frete = frete, liv_id = idLivro, cli_id = idCliente))
conn.commit()

query = "SELECT * FROM venda"

df = pd.read_sql_query(query, con=engine)
print(df)
