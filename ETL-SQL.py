import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
    )

    try:
        yield conexao
    finally:
        print('Conexão Fechada!')
        conexao.close()

# INSERIR UM REGISTRO
#with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s,%s)'
#        cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#        conexao.commit()

# INSERIR VÁRIOS REGISTROS
# with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s,%s)'
#        dados = [
#            ('Bruno', 'Bento', 26, 90),
#            ('Rose', 'Figueiredo', 26, 90),
#             ('Jose', 'Figueiredo', 26, 90),
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()

# DELETAR UM REGISTRO
# with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'DELETE FROM clientes WHERE id = %s'
#        cursor.execute(sql, (6,))
#        conexao.commit()

#DELETAR UMA LISTA DE REGISTROS (ENTRE)
# with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#        cursor.execute(sql, (2, 5))
#        conexao.commit()

# ATUALIZA UM REGISTRO
# with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#        cursor.execute(sql, ('Carlos', 10))
#        conexao.commit()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)

