import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo) #fazer a conexão com o arquivo
        self.cursor = self.conn.cursor()     #vai adicionar a função cursor na conexão e colocar em uma variável

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome,telefone) VALUES (?, ?)' #inserir na agenda
        self.cursor.execute(consulta, (nome, telefone))  #executar o comando, com nome e tel fixos
        self.conn.commit() #atualizar o arquivo

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?' #atualiza a agenda o campos de nome e telefone de acordo com o id
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?' #deleta da agenda de acordo com o id
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda') #selecionar tudo da agenda

        for linha in self.cursor.fetchall(): # o fetchall vai trazer todos os valores para linha
            print(linha) #a variável linha estará alimentada com todos os valores do arquivo

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?' # selecionar tudo da agenda
        self.cursor.execute(consulta, (f'%{valor}%', ))

        for linha in self.cursor.fetchall(): # o fetchall vai trazer todos os valores para linha
            print(linha) # a variável linha estará alimentada com todos os valores do arquivo

    def fechar(self):
        self.cursor.close()
        self.conn.close()




if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.inserir('Luiz Otávio', 123456)
    agenda.inserir('Luiz 22', 123457)
    agenda.inserir('Luiz carlin', 123458)
    agenda.inserir('R. Luiz kkkkkdaso', 123454)
    agenda.buscar('luiz')