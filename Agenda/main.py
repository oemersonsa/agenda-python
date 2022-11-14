import sqlite3, time

conectar = sqlite3.connect('agenda.db')
c = conectar.cursor()


def criar_db():
    c.execute('CREATE TABLE cadastro (nome text, telefone varchar, email text, data text)')


'''try:
    criar_db()
except:
    print('Erro ao criar banco de dados!')
else:
    print('Banco de dados criado com sucesso!')'''


def inserir(n, t, e):
    d = time.strftime('%d/%m/%y')
    c.execute('INSERT INTO cadastro VALUES(?,?,?,?)', (n, t, e, d))
    conectar.commit()


def listar(p):
    sql = 'SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql, (p, )):
        print(row)


while True:
    time.sleep(1.5)
    fc = int(input('1 - Cadastrar\n2 - Pesquisar\n3 - Sair\nO que deseja fazer?: '))

    if fc == 1:
        try:
            print('Cadastro Agenda')
            time.sleep(1.5)
            n = str(input('Digite o nome: '))
            t = int(input('Digite o telefone: '))
            e = str(input('Digite o e-mail: '))

            inserir(n, t, e)
        except:
            print('Erro ao cadastrar!')
        else:
            print('Cadastro feito com sucesso!')
    elif fc == 2:
        try:
            print('Pesquisa Agenda')
            time.sleep(1.5)
            p = str(input('Digite o nome: '))
            listar(p)
        except:
            print('Erro ao pesquisar!')
    elif fc == 3:
        time.sleep(1)
        print('Saindo do programa...')
        break
    else:
        print('...')