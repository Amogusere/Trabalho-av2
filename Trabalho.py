# Import required modules
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
import sqlite3
from msilib.schema import Directory
import os.path
from pathlib import Path
from datetime import datetime
import time
import csv
conteudo = []
conteudo2 = []
filename = ''
filename1 = ''

# Connecting to the geeks database
connection = sqlite3.connect('trabalho.db')
  
# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()
  
# Definições da Tabela Pessoas
pessoa = '''CREATE TABLE IF NOT EXISTS pessoas(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                cpf TEXT NOT NULL UNIQUE,
                primeiro_nome TEXT NOT NULL,
                nome_do_meio TEXT NOT NULL,
                sobrenome TEXT NOT NULL,
                idade INTEGER NOT NULL);
                '''
  
# Criando a tabela pessoas dentro do seu banco de dados 
cursor.execute(pessoa)

# Definições da Tabela Contas
conta = '''CREATE TABLE IF NOT EXISTS contas(
                agencia TEXT NOT NULL,
                numero TEXT NOT NULL,
                saldo TEXT NOT NULL,
                gerente TEXT NOT NULL,
                id_titular INTEGER NOT NULL,
                renda TEXT NULL);
                '''
  
# Criando a tabela contas dentro do seu banco de dados 
cursor.execute(conta)

# Definições da Tabela Contatos
contato = '''CREATE TABLE IF NOT EXISTS contatos(
                telefone TEXT NULL,
                e_mail TEXT NULL,
                id_titular INTEGER NULL);
                '''
  
# Criando a tabela contas dentro do seu banco de dados 
cursor.execute(contato)

# interface
def jan_principal():
    def titulo(x):
        lb = Label(x, text='Seja bem-vindo ao Sistema de Cadastro de Pessoas')
        lb.place(x=210, y=50)
        lb['bg'] = 'bisque'

    def tipotitulo(x, a):
        lb = Label(x, text=a)
        lb.place(x=280, y=80)
        lb['bg'] = 'bisque'

    def jan_importar():
        def ok():
            erro.destroy()
            FileRead = open("nomes.txt","r")
            texto = ''
            for line in FileRead:
                texto += line.replace(" ",",")
            FileRead.close()
            FileWrite = open("nomes.txt","w")
            FileWrite.write(texto)
            FileWrite.close()

            FileRead = open("contas.txt","r")
            texto = ''
            for line in FileRead:
                texto += line.replace(" ",",")
            FileRead.close()
            FileWrite = open("contas.txt","w")
            FileWrite.write(texto)
            FileWrite.close()
        try:
            # Abrindo o arquivo nomes.txt
            file = open('nomes.txt')

            # Lendo o conteúdo do arquivo nomes.txt
            contents = csv.reader(file)

            # SQL query para inserir dados dentro da tabela pessoas
            insert_records = "INSERT INTO pessoas (cpf, primeiro_nome, nome_do_meio, sobrenome, idade, id) VALUES(?, ?, ?, ?, ?, ?)"

            # Importando o conteúdo do arquivo txt para sua tabela pessoas
            cursor.executemany(insert_records, contents)

            # Abrindo o arquivo contas.txt
            file = open('contas.txt')

            # Lendo o conteúdo do arquivo contas.txt
            contents = csv.reader(file)

            # SQL query para inserir dados dentro da tabela contas
            insert_records = "INSERT INTO contas (agencia, numero, saldo, gerente, id_titular) VALUES(?, ?, ?, ?, ?)"

            # Importando o conteúdo do arquivo txt para sua tabela contas
            cursor.executemany(insert_records, contents)

            connection.commit()
            #connection.close() 
            erro = Tk()
            erro.title('Erro')
            erro.geometry('180x150+620+280')
            
            lb = Label(erro, text='Arquivos importados!')
            lb.place(x=45, y=50)
                    
            bt = Button(erro, text='OK', command=ok, )
            bt.place(x=75, y=85) 
        except:
            erro = Tk()
            erro.title('Erro')
            erro.geometry('180x150+620+280')

            lb = Label(erro, text='Base já atualizada!')
            lb.place(x=45, y=50)
                    
            bt = Button(erro, text='OK', command=ok, )
            bt.place(x=75, y=85)   

    def jan_pessoas():
        # interface
        def jan_cadastropessoas():
            def bd_cadpessoas():
                def Ok():
                    erro.destroy()
                    cpf.delete(0, END)
                    primeiro_nome.delete(0, END)
                    nome_do_meio.delete(0,END)
                    sobrenome.delete(0,END)
                    idade.delete(0,END)
                try:
                    cpfa = str(cpf.get())
                    primeiro_nomea = str(primeiro_nome.get())
                    nome_do_meioa = str(nome_do_meio.get())
                    sobrenomea = str(sobrenome.get())
                    idadea = int(idade.get())
                    cursor.execute('''
                    INSERT INTO pessoas (cpf, primeiro_nome, nome_do_meio, sobrenome, idade)
                    VALUES('%s','%s','%s','%s','%d')
                    ''' % (cpfa, primeiro_nomea, nome_do_meioa, sobrenomea, idadea))
                    connection.commit()

                    lb = Label(c_pessoas, text='Cliente cadastrado!')
                    lb.place(x=350, y=400)
                    cpf.delete(0, END)
                    primeiro_nome.delete(0, END)
                    nome_do_meio.delete(0,END)
                    sobrenome.delete(0,END)
                    idade.delete(0,END)
                except:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    lb = Label(erro, text='Cliente já cadastrado!')
                    lb.place(x=45, y=50)
                    
                    bt = Button(erro, text='OK', command=Ok, )
                    bt.place(x=75, y=85)

            def voltar1():
                c_pessoas.destroy()
                jan_principal()

            # janela cadastro pessoas
            c_pessoas = Tk()
            c_pessoas.title('Cadastrando Pessoa')
            c_pessoas['bg'] = 'bisque'
            c_pessoas.geometry('700x450+350+100')
            pessoas.destroy()

            # titulos
            titulo(c_pessoas)
            a = 'CADASTRO PESSOAS'
            tipotitulo(c_pessoas, a)

            # CPF
            lb_cpf = Label(c_pessoas, text='cpf :')
            lb_cpf.place(x=170, y=150)
            lb_cpf['bg'] = 'bisque'

            # Entrada do CPF
            cpf = Entry(c_pessoas, width=45)
            cpf.place(x=280, y=153)

            # primeiro_nome
            lb_primeiro_nome = Label(c_pessoas, text='Primeiro Nome :')
            lb_primeiro_nome.place(x=170, y=180)
            lb_primeiro_nome['bg'] = 'bisque'

            # Entrada do primeiro_nome
            primeiro_nome = Entry(c_pessoas, width=45)
            primeiro_nome.place(x=280, y=183)

            # nome_do_meio
            lb_nome_do_meio = Label(c_pessoas, text='Nome do Meio :')
            lb_nome_do_meio.place(x=170, y=210)
            lb_nome_do_meio['bg'] = 'bisque'

            # Entrada do nome_do_meio
            nome_do_meio = Entry(c_pessoas, width=45)
            nome_do_meio.place(x=280, y=213)

            # sobrenome
            lb_sobrenome = Label(c_pessoas, text='Sobrenome :')
            lb_sobrenome.place(x=170, y=240)
            lb_sobrenome['bg'] = 'bisque'

            # Entrada do sobrenome
            sobrenome = Entry(c_pessoas, width=45)
            sobrenome.place(x=280, y=243)

            # idade
            lb_idade = Label(c_pessoas, text='Idade :')
            lb_idade.place(x=170, y=270)
            lb_idade['bg'] = 'bisque'

            # Entrada do sobrenome
            idade = Entry(c_pessoas, width=45)
            idade.place(x=280, y=273)

            # BUTTON cadastrar pessoas
            b_cadastrar = Button(c_pessoas, width=20, text='Cadastrar',
                                 command=bd_cadpessoas,
                                 activebackground='gray28',
                                 activeforeground='gray99',
                                 bg='gray99', bd=0.5)
            b_cadastrar.place(x=200, y=350)
            # BUTTON voltar
            b_voltar = Button(c_pessoas, width=20, text='Voltar',
                              command=voltar1,
                              activebackground='gray28',
                              activeforeground='gray99',
                              bg='gray99', bd=0.5)
            b_voltar.place(x=350, y=350)
        def jan_alterarpessoas():
            # janela alterar pessoas
            a_pessoas = Tk()
            a_pessoas.title('Alterando Cadastro do Pessoa')
            a_pessoas['bg'] = 'bisque'
            a_pessoas.geometry('700x450+350+100')
            pessoas.destroy()

            def voltar():
                a_pessoas.destroy()
                jan_principal()

            # titulos
            titulo(a_pessoas)
            a = 'ALTERAR CADASTRO DO PESSOA'
            tipotitulo(a_pessoas, a)

            # LABEL : ID CPF primeiro_nome nome_do_meio sobrenome idade
            lb_id = Label(a_pessoas, text='ID   CPF          PRIMEIRO_NOME        NOME_DO_MEIO     SOBRENOME     IDADE')
            lb_id.place(x=175, y=240)
            lb_id['bg'] = 'bisque'

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(a_pessoas, width=40)
            e_cpf.place(x=295, y=180)

            # nome : cpf para pesquisa
            lb = Label(a_pessoas, text='Digite o CPF:')
            lb.place(x=170, y=178)
            lb['bg'] = 'bisque'

            # tela de informações
            C = Listbox(a_pessoas, width=40, height=3, bg='snow', bd=0.6, relief='raise')
            C.place(x=175, y=260)

            def entradadenovasinf():
                def bd_alterar():
                    cpf = (nv_cpf.get())
                    primeiro_nome = (nv_primeiro_nome.get())
                    nome_do_meio = (nv_nome_do_meio.get())
                    sobrenome = (nv_sobrenome.get())
                    idade = (nv_idade.get())
                    c = connection.cursor()
                    c.execute("""
                        UPDATE pessoas
                        SET cpf = '%s', primeiro_nome = '%s', nome_do_meio = '%s', sobrenome = '%s', idade = '%s' WHERE cpf = '%s'
                        """ % (cpf, primeiro_nome, nome_do_meio, sobrenome, idade, cpfa))
                    connection.commit()
                    nv_cpf.delete(0, END)
                    nv_primeiro_nome.delete(0, END)
                    nv_nome_do_meio.delete(0, END)
                    nv_sobrenome.delete(0, END)
                    nv_idade.delete(0, END)
                    if len(cpfa) == 0:
                        lb = Label(at_inf, text='Pessoa não selecionada!')
                    else:
                        lb = Label(at_inf, text='Cliente alterado!')
                    lb.place(x=200, y=380)
                    lb['bg'] = 'bisque'

                c = connection.cursor()
                cpfa = str(e_cpf.get())
                c.execute('''SELECT * FROM pessoas WHERE cpf = '%s';''' % cpfa)
                at_inf = Tk()
                at_inf.title('Atualizando Cadastro do Cliente')
                at_inf['bg'] = 'bisque'
                at_inf.geometry('700x450+350+100')
                a_pessoas.destroy()

                def voltar_():
                    at_inf.destroy()
                    jan_principal()

                # titulos
                titulo(at_inf)
                a = 'ALTERAR CADASTRO DO PESSOA'
                tipotitulo(at_inf, a)

                # Entrada de novo cpf
                nv_cpf = Entry(at_inf, width=40)
                nv_cpf.place(x=295, y=140)

                # Entrada de novo primeiro_nome
                nv_primeiro_nome = Entry(at_inf, width=40)
                nv_primeiro_nome.place(x=295, y=180)

                # Entrada de novo nome_do_meio
                nv_nome_do_meio = Entry(at_inf, width=40)
                nv_nome_do_meio.place(x=295, y=220)

                # Entrada de novo sobrenome
                nv_sobrenome = Entry(at_inf, width=40)
                nv_sobrenome.place(x=295, y=260)

                # Entrada de nova idade
                nv_idade = Entry(at_inf, width=40)
                nv_idade.place(x=295, y=300)

                # Texto - Novo cpf
                lb_n = Label(at_inf, text='Novo cpf:')
                lb_n.place(x=170, y=136)
                lb_n['bg'] = 'bisque'

                # Texto - Novo primeiro_nome
                lb_c = Label(at_inf, text='Novo Primeiro Nome:')
                lb_c.place(x=170, y=176)
                lb_c['bg'] = 'bisque'

                # Texto - Novo nome_do_meio
                lb_c = Label(at_inf, text='Novo Nome do Meio:')
                lb_c.place(x=170, y=216)
                lb_c['bg'] = 'bisque'

                # Texto - Novo sobrenome
                lb_c = Label(at_inf, text='Novo Sobrenome:')
                lb_c.place(x=170, y=256)
                lb_c['bg'] = 'bisque'

                # Texto - Nova idade
                lb_c = Label(at_inf, text='Nova Idade:')
                lb_c.place(x=170, y=296)
                lb_c['bg'] = 'bisque'

                # button: Alterar
                butt_a = Button(at_inf, width=20,
                                command=bd_alterar,
                                text='Alterar',
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_a.place(x=220, y=350)

                # button : voltar
                butt_v = Button(at_inf, width=20,
                                text='Voltar',
                                command=voltar_,
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_v.place(x=380, y=350)

                #Buscar informações do bando de dados
                c = connection.cursor()
                c.execute('''SELECT * FROM pessoas WHERE cpf = '%s';''' % cpfa)
                List_pesq = c.fetchall()
                if len(List_pesq) != 0:
                    cpfa = List_pesq[0][1]
                    primeiro_nomea = List_pesq[0][2]
                    nome_do_meioa = List_pesq[0][3]
                    sobrenomea = List_pesq[0][4]
                    idadea = List_pesq[0][5]
                    nv_cpf.insert(0, cpfa)
                    nv_primeiro_nome.insert(0, primeiro_nomea)
                    nv_nome_do_meio.insert(0,nome_do_meioa)
                    nv_sobrenome.insert(0,sobrenomea)
                    nv_idade.insert(0,idadea)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_cpf.delete(0, END)

                cpfa = e_cpf.get()
                c = connection.cursor()
                c.execute('''SELECT * FROM pessoas WHERE cpf = '%s';''' % cpfa)
                a = c.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='CPF não encontrado!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    C.delete(0, END)
                else:
                    C.insert(0, a)

            # button : alterar cadastro
            butt_a = Button(a_pessoas, width=20,
                            command=entradadenovasinf,
                            text='Alterar cadastro',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_a.place(x=220, y=350)
            # Button pesquisar
            btp = Button(a_pessoas, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=200)

            # button : voltar
            butt_v = Button(a_pessoas, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=380, y=350)

        def jan_consultarpessoas():
        # janela consultar pessoas
            co_pessoas = Tk()
            co_pessoas.title('Consultando Pessoa')
            co_pessoas['bg'] = 'bisque'
            co_pessoas.geometry('700x450+350+100')
            pessoas.destroy()

            def bd_txtpessoas():
                # SQL query para selecionar dados dentro da tabela pessoas
                cpfa = str(e_cpf.get())
                c = connection.cursor()
                Select_records1 = "SELECT * FROM pessoas WHERE cpf = '"+cpfa+"'" 
 
                # Selecionar dados na tabela pessoas 
                Nome1 = c.execute(Select_records1)
                Nome1 = ''.join([str(item) for item in Nome1])
                b = "(')"
                for i in range(0,len(b)):
                    Nome1 =Nome1.replace(b[i],"")
                print(Nome1)
                # Criar pasta 
                pasta = "Consulta cpf/"
                if os.path.isdir(pasta): # vemos de este diretorio ja existe
                    lb = Label(co_pessoas, text='Ja existe uma pasta com esse nome!')
                else:
                    os.mkdir(pasta) # aqui criamos a pasta caso nao exista
                    lb = Label(co_pessoas, text='Pasta criada com sucesso!')
                lb.place(x=350, y=430)

                # Criar arquivo txt e inserir dados da consulta
                timestr = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
                NomeArq = 'cpf-'+timestr+'.txt'
                Directory = Path(pasta)
                file = Directory / NomeArq
                for row in Nome1:
                    conteudo.append(row)
                arquivo = open(file,'w')
                arquivo.writelines(conteudo)
                arquivo.close()

                connection.commit() 

            def voltar():
                co_pessoas.destroy()
                jan_principal()

            # titulos
            titulo(co_pessoas)
            a = 'CONSULTAR PESSOAS'
            tipotitulo(co_pessoas, a)

            # LABEL : ID CPF primeiro_nome nome_do_meio sobrenome idade
            lb_id = Label(co_pessoas, text='ID   CPF          PRIMEIRO_NOME        NOME_DO_MEIO     SOBRENOME     IDADE')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(co_pessoas, width=40, height=7, bg='snow', bd=0.6, relief='raise')
            C.place(x=175, y=240)
            cursor.execute('''SELECT * FROM pessoas''')
            x = 1
            for i in cursor.fetchall():
                C.insert(x + 1, i)

            def pesquisa():
                cpfa = str(e_cpf.get())
                c = connection.cursor()
                try:
                    c.execute('''SELECT * FROM pessoas WHERE cpf = '%s';''' % cpfa)
                    C = Listbox(co_pessoas, width=40, height=7, bg='snow', bd=0.6, relief='raise')
                    C.place(x=175, y=240)
                    for i in c.fetchall():
                        C.insert(0, i)
                except:
                    print('erro')

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(co_pessoas, width=40)
            e_cpf.place(x=295, y=160)

            # Button pesquisar
            btp = Button(co_pessoas, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : cpf para pesquisa
            lb = Label(co_pessoas, text='CPF para pesquisa:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # BUTTON Gerar TXT contas
            butt_txt = Button(co_pessoas, width=20, text='Gerar TXT',
                                 command=bd_txtpessoas,
                                 activebackground='gray28',
                                 activeforeground='gray99',
                                 bg='gray99', bd=0.5)
            butt_txt.place(x=200, y=400)

            # button : voltar
            butt_v = Button(co_pessoas, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=490, y=400)

        def jan_removerpessoas():
            # janela remover pessoas
            r_pessoas = Tk()
            r_pessoas.title('Removendo Pessoa')
            r_pessoas['bg'] = 'bisque'
            r_pessoas.geometry('700x450+350+100')
            pessoas.destroy()

            def voltar():
                r_pessoas.destroy()
                jan_principal()

            # titulos
            titulo(r_pessoas)
            a = 'REMOVER PESSOA'
            tipotitulo(r_pessoas, a)

            # LABEL : ID CPF primeiro_nome nome_do_meio sobrenome idade
            lb_id = Label(r_pessoas, text='ID   CPF          PRIMEIRO_NOME        NOME_DO_MEIO     SOBRENOME     IDADE')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(r_pessoas, width=40, height=6, bg='snow', bd=0.6, relief='raise')
            C.place(x=175, y=240)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_cpf.delete(0, END)

                cpfa = e_cpf.get()
                c = connection.cursor()
                c.execute('''SELECT * FROM pessoas WHERE cpf = '%s';''' % cpfa)
                a = c.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='CPF não encontrado!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    C.delete(0, END)
                else:
                    C.insert(0, a)

            def remover():
                cpfa = e_cpf.get()
                c = connection.cursor()
                c.execute('''SELECT * FROM pessoas WHERE cpf = '%s';''' % cpfa)
                a = c.fetchall()
                id_d = a[0][0]
                c.execute('''SELECT id_titular FROM contas WHERE id_titular = '%s';''' % id_d)
                id_titular = c.fetchall()
                id_titular_r = id_titular[0][0]
                id_d = id_titular_r
                c.execute("""DELETE FROM pessoas WHERE cpf = '%s'; """ % (cpfa))
                c.execute("""DELETE FROM contas WHERE id_titular = '%s'; """ % (id_d))
                connection.commit()
                e_cpf.delete(0, END)
                lb_id = Label(r_pessoas, text='Pessoa removida')
                lb_id.place(x=320, y=360)
                lb_id['bg'] = 'bisque'
                C.delete(0, END)

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(r_pessoas, width=40)
            e_cpf.place(x=295, y=160)

            # Button pesquisar
            btp = Button(r_pessoas, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : cpf para pesquisa
            lb = Label(r_pessoas, text='Digite o cpf:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # button : remover cadastro
            butt_a = Button(r_pessoas, width=20,
                            command=remover,
                            text='Remover cadastro',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_a.place(x=320, y=400)

            # button : voltar
            butt_v = Button(r_pessoas, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=490, y=400)

        def voltar_a():
            pessoas.destroy()
            jan_principal()

        # janela pessoas
        pessoas = Tk()
        pessoas.title('Pessoas')
        pessoas['bg'] = 'bisque'
        pessoas.geometry('700x450+350+100')
        janela.destroy()
        # titulos
        titulo(pessoas)
        a = 'PESSOAS'
        tipotitulo(pessoas, a)
        # button cadastrar pessoa
        btac = Button(pessoas, width=40,
                      command=jan_cadastropessoas,
                      text='Cadastrar Pessoa',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btac.place(x=200, y=150)

        # button alterar pessoa
        btaa = Button(pessoas, width=40,
                      command=jan_alterarpessoas,
                      text='Alterar Pessoa',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btaa.place(x=200, y=200)

        # button Consultar Pessoa
        btaco = Button(pessoas, width=40,
                       command=jan_consultarpessoas,
                       text='Consultar Pessoa',
                       activebackground='gray28',
                       activeforeground='gray99',
                       bg='gray99', bd=0.5)
        btaco.place(x=200, y=250)

        # button Remover pessoa
        btar = Button(pessoas, width=40,
                      command=jan_removerpessoas,
                      text='Remover Pessoa',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btar.place(x=200, y=300)

        # button Voltar
        v = Button(pessoas, width=40,
                   command=voltar_a,
                   text='Voltar',
                   activebackground='gray28',
                   activeforeground='gray99',
                   bg='gray99', bd=0.5)
        v.place(x=200, y=350)

    def jan_contas():
        # interface
        def jan_cadastrocontas():
            def bd_cadcontas():
                def Ok():
                    erro.destroy()
                    agencia.delete(0, END)
                    numero.delete(0, END)
                    saldo.delete(0,END)
                    gerente.delete(0,END)
                    renda.delete(0,END)
                try:
                    agenciaa = str(agencia.get())
                    numeroa = str(numero.get())
                    saldoa = str(saldo.get())
                    gerentea = str(gerente.get())
                    rendaa = str(renda.get())
                    cpfa = str(e_cpf.get())
                    c = connection.cursor()
                    id_titulara = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                    id_titularastr = ''.join([str(item) for item in id_titulara])
                    b = "(,)"
                    for i in range(0,len(b)):
                        id_titularastr =id_titularastr.replace(b[i],"")
                    c.execute('''SELECT * FROM contas WHERE id_titular = '%s';''' % id_titularastr)
                    agenciaco = c.fetchall()
                    if len(agenciaco) == 0:
                        cursor.execute('''
                        INSERT INTO contas (agencia, numero, saldo, gerente, id_titular, renda)
                        VALUES('%s','%s','%s','%s','%s','%s')
                        ''' % (agenciaa, numeroa, saldoa, gerentea, id_titularastr, rendaa))
                        connection.commit()
                        lb = Label(c_contas, text='Conta cadastrada!')
                        lb.place(x=350, y=400)
                        agencia.delete(0, END)
                        numero.delete(0, END)
                        saldo.delete(0,END)
                        gerente.delete(0,END)
                        renda.delete(0,END)
                except:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    if len(id_titularastr) == 0:
                        lb = Label(erro, text='Pessoa não cadastrada!')
                        lb.place(x=45, y=50)
                    else:
                        lb = Label(erro, text='Conta já cadastrada!')
                        lb.place(x=45, y=50)
                    
                    bt = Button(erro, text='OK', command=Ok, )
                    bt.place(x=75, y=85)

            def voltar1():
                c_contas.destroy()
                jan_principal()

            # janela cadastro contas
            c_contas = Tk()
            c_contas.title('Cadastrando Conta')
            c_contas['bg'] = 'bisque'
            c_contas.geometry('700x450+350+100')
            contas.destroy()

            # titulos
            titulo(c_contas)
            a = 'CADASTRO CONTA'
            tipotitulo(c_contas, a)

            def pesquisa():
                cpfa = str(e_cpf.get())
                c = connection.cursor()
                d = connection.cursor()
                try:
                    id_titular = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                    id_titularstr = ''.join([str(item) for item in id_titular])
                    b = "(,)"
                    for i in range(0,len(b)):
                        id_titularstr =id_titularstr.replace(b[i],"")
                    d.execute('''SELECT * FROM contas WHERE id_titular = '%s';''' % id_titularstr)
                    List_pesq = d.fetchall()
                    if len(id_titularstr) == 0:
                        agencia.delete(0, END)
                        numero.delete(0, END)
                        saldo.delete(0,END)
                        gerente.delete(0,END)
                        renda.delete(0,END)
                        lb = Label(c_contas, text='Pessoa não cadastrada!')
                    else:
                        if len(List_pesq) == 0:
                            agencia.delete(0, END)
                            numero.delete(0, END)
                            saldo.delete(0,END)
                            gerente.delete(0,END)
                            renda.delete(0,END)
                            lb = Label(c_contas, text='Preencher os dados da conta!')
                        else:
                            print(List_pesq)
                            agenciaa = List_pesq[0][0]
                            numeroa = List_pesq[0][1]
                            saldoa = List_pesq[0][2]
                            gerentea = List_pesq[0][3]
                            rendaa = List_pesq[0][5]
                            agencia.insert(0, agenciaa)
                            numero.insert(0, numeroa)
                            saldo.insert(0,saldoa)
                            gerente.insert(0,gerentea)
                            renda.insert(0,rendaa)
                            lb = Label(c_contas, text='Conta já cadastrada!')
                    lb.place(x=350, y=400)
                except:
                    print('erro')

            # Entrada do CPF pra pesquisar
            e_cpf = Entry(c_contas, width=40)
            e_cpf.place(x=295, y=118)

            # Button pesquisar
            btp = Button(c_contas, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=143)

            # nome : cpf para pesquisa
            lb = Label(c_contas, text='Digite o CPF:')
            lb.place(x=170, y=116)
            lb['bg'] = 'bisque'

            # AGÊNCIA
            lb_agencia = Label(c_contas, text='Agência :')
            lb_agencia.place(x=170, y=180)
            lb_agencia['bg'] = 'bisque'

            # Entrada da agência
            agencia = Entry(c_contas, width=45)
            agencia.place(x=230, y=183)

            # numero
            lb_numero = Label(c_contas, text='Número :')
            lb_numero.place(x=170, y=210)
            lb_numero['bg'] = 'bisque'

            # Entrada do número
            numero = Entry(c_contas, width=45)
            numero.place(x=230, y=213)

            # saldo
            lb_saldo = Label(c_contas, text='Saldo :')
            lb_saldo.place(x=170, y=240)
            lb_saldo['bg'] = 'bisque'

            # Entrada do saldo
            saldo = Entry(c_contas, width=45)
            saldo.place(x=230, y=243)

            # gerente
            lb_gerente = Label(c_contas, text='Gerente :')
            lb_gerente.place(x=170, y=270)
            lb_gerente['bg'] = 'bisque'

            # Entrada do gerente
            gerente = Entry(c_contas, width=45)
            gerente.place(x=230, y=273)

            # renda
            lb_renda = Label(c_contas, text='Renda :')
            lb_renda.place(x=170, y=300)
            lb_saldo['bg'] = 'bisque'

            # Entrada da renda
            renda = Entry(c_contas, width=45)
            renda.place(x=230, y=303)

            # BUTTON cadastrar contas
            b_cadastrar = Button(c_contas, width=20, text='Cadastrar',
                                 command=bd_cadcontas,
                                 activebackground='gray28',
                                 activeforeground='gray99',
                                 bg='gray99', bd=0.5)
            b_cadastrar.place(x=200, y=350)
            # BUTTON voltar
            b_voltar = Button(c_contas, width=20, text='Voltar',
                              command=voltar1,
                              activebackground='gray28',
                              activeforeground='gray99',
                              bg='gray99', bd=0.5)
            b_voltar.place(x=350, y=350)
            
        def jan_alterarcontas():
            # janela alterar contas
            a_contas = Tk()
            a_contas.title('Alterando Cadastro da Conta')
            a_contas['bg'] = 'bisque'
            a_contas.geometry('700x450+350+100')
            contas.destroy()

            def voltar():
                a_contas.destroy()
                jan_principal()

            # titulos
            titulo(a_contas)
            a = 'ALTERAR CADASTRO DA CONTA'
            tipotitulo(a_contas, a)

            # LABEL : AGÊNCIA NÚMERO SALDO GERENTE ID_TITULAR
            lb_id = Label(a_contas, text='AGÊNCIA NÚMERO SALDO GERENTE ID_TITULAR RENDA')
            lb_id.place(x=175, y=240)
            lb_id['bg'] = 'bisque'
 
            # Entrada do CPF pra pesquisar
            e_cpf = Entry(a_contas, width=40)
            e_cpf.place(x=295, y=180)

            # nome : cpf para pesquisa
            lb = Label(a_contas, text='Digite o CPF:')
            lb.place(x=170, y=178)
            lb['bg'] = 'bisque'

            # tela de informações
            C = Listbox(a_contas, width=40, height=3, bg='snow', bd=0.6, relief='raise')
            C.place(x=175, y=260)

            def entradadenovasinf():
                def bd_alterar():
                    agencia = str(nv_agencia.get())
                    numero = str(nv_numero.get())
                    saldo = str(nv_saldo.get())
                    gerente = str(nv_gerente.get())
                    renda = str(nv_renda.get())
                    c = connection.cursor()
                    d = connection.cursor()
                    id_titular = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                    id_titularstr = ''.join([str(item) for item in id_titular])
                    b = "(,)"
                    for i in range(0,len(b)):
                        id_titularstr =id_titularstr.replace(b[i],"")
                    d.execute("""UPDATE contas
                        SET agencia = '%s', numero = '%s', saldo = '%s', gerente = '%s', id_titular = '%s', renda = '%s' WHERE id_titular = '%s'
                        """ % (agencia, numero, saldo, gerente, id_titularstr, renda, id_titularstr))
                    connection.commit()
                    nv_agencia.delete(0, END)
                    nv_numero.delete(0, END)
                    nv_saldo.delete(0, END)
                    nv_gerente.delete(0, END)
                    nv_renda.delete(0, END)
                    if len(id_titularstr) == 0:
                        lb = Label(at_inf, text='Pessoa não selecionada!', font='12')
                    else:
                        lb = Label(at_inf, text='Conta atualizada!', font='12')
                    lb.place(x=200, y=380)
                    lb['bg'] = 'bisque'

                c = connection.cursor()
                cpfa = str(e_cpf.get())
                c.execute('''SELECT contas.* FROM contas INNER JOIN pessoas ON id = id_titular WHERE cpf = '%s';''' % cpfa)
                at_inf = Tk()
                at_inf.title('Atualizando Cadastro da Conta')
                at_inf['bg'] = 'bisque'
                at_inf.geometry('700x450+350+100')
                a_contas.destroy()

                def voltar_():
                    at_inf.destroy()
                    jan_principal()

                # titulos
                titulo(at_inf)
                a = 'ALTERAR CADASTRO DA CONTA'
                tipotitulo(at_inf, a)

                # Entrada de nova agência
                nv_agencia = Entry(at_inf, width=40)
                nv_agencia.place(x=295, y=180)

                # Entrada de novo número
                nv_numero = Entry(at_inf, width=40)
                nv_numero.place(x=295, y=220)

                # Entrada de novo saldo
                nv_saldo = Entry(at_inf, width=40)
                nv_saldo.place(x=295, y=260)

                # Entrada de novo gerente
                nv_gerente = Entry(at_inf, width=40)
                nv_gerente.place(x=295, y=290)

                # Entrada de nova renda
                nv_renda = Entry(at_inf, width=40)
                nv_renda.place(x=295, y=330)
                
                # Texto - Nova Agência
                lb_n = Label(at_inf, text='Nova Agência:')
                lb_n.place(x=170, y=176)
                lb_n['bg'] = 'bisque'

                # Texto - Novo número
                lb_c = Label(at_inf, text='Novo Número:')
                lb_c.place(x=170, y=216)
                lb_c['bg'] = 'bisque'

                # Texto - Novo Saldo
                lb_c = Label(at_inf, text='Novo Saldo:')
                lb_c.place(x=170, y=256)
                lb_c['bg'] = 'bisque'

                # Texto - Novo gerente
                lb_c = Label(at_inf, text='Novo Gerente:')
                lb_c.place(x=170, y=296)
                lb_c['bg'] = 'bisque'

                # Texto - Nova Renda
                lb_c = Label(at_inf, text='Nova Renda:')
                lb_c.place(x=170, y=336)
                lb_c['bg'] = 'bisque'

                # button: Alterar
                butt_a = Button(at_inf, width=20,
                                command=bd_alterar,
                                text='Alterar',
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_a.place(x=220, y=360)

                # button : voltar
                butt_v = Button(at_inf, width=20,
                                text='Voltar',
                                command=voltar_,
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_v.place(x=380, y=360)

                #Buscar informações do bando de dados
                c = connection.cursor()
                id_titular = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                id_titularstr = ''.join([str(item) for item in id_titular])
                b = "(,)"
                for i in range(0,len(b)):
                    id_titularstr =id_titularstr.replace(b[i],"")
                c.execute('''SELECT * FROM contas WHERE id_titular = '%s';''' % id_titularstr)
                List_pesq = c.fetchall()
                if len(List_pesq) != 0:
                    agenciaa = List_pesq[0][0]
                    numeroa = List_pesq[0][1]
                    saldoa = List_pesq[0][2]
                    gerentea = List_pesq[0][3]
                    rendaa = List_pesq[0][5]
                    nv_agencia.insert(0, agenciaa)
                    nv_numero.insert(0, numeroa)
                    nv_saldo.insert(0,saldoa)
                    nv_gerente.insert(0,gerentea)
                    if str(rendaa) == 'None':
                        nv_renda.insert(0,"")
                    else:
                        nv_renda.insert(0,rendaa)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_cpf.delete(0, END)

                cpfa = e_cpf.get()
                c = connection.cursor()
                c.execute('''SELECT contas.* FROM contas INNER JOIN pessoas ON id = id_titular WHERE cpf = '%s';''' % cpfa)
                a = c.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='CPF não encontrado!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    C.delete(0, END)
                else:
                    C.insert(0, a)

            # button : alterar cadastro
            butt_a = Button(a_contas, width=20,
                            command=entradadenovasinf,
                            text='Alterar cadastro',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_a.place(x=220, y=350)
            # Button pesquisar
            btp = Button(a_contas, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=200)

            # button : voltar
            butt_v = Button(a_contas, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=380, y=350)

        def jan_consultarcontas():
        # janela consultar contas
            co_contas = Tk()
            co_contas.title('Consultando Conta')
            co_contas['bg'] = 'bisque'
            co_contas.geometry('700x450+350+100')
            contas.destroy()

            def bd_txtcontas():
                # SQL query para selecionar dados dentro da tabela pessoas
                cpfa = str(e_cpf.get())
                c = connection.cursor()
                id_titulara = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                id_titularastr = ''.join([str(item) for item in id_titulara])
                b = "(,)"
                for i in range(0,len(b)):
                    id_titularastr =id_titularastr.replace(b[i],"")
                # SQL query para selecionar dados dentro da tabela contas
                Select_records2 = "SELECT * FROM CONTAS WHERE id_titular = '"+id_titularastr+"'" 
 
                # Selecionar dados na tabela pessoas 
                Nome2 = c.execute(Select_records2)
                Nome2 = ''.join([str(item) for item in Nome2])
                b = "(')"
                for i in range(0,len(b)):
                    Nome2 = Nome2.replace(b[i],"")
                Nome2 = cpfa + ', ' + Nome2

                # Criar pasta 
                pasta2 = "Consulta conta/"
                if os.path.isdir(pasta2): # vemos de este diretorio ja existe
                    lb = Label(co_contas, text='Ja existe uma pasta com esse nome!')
                else:
                    os.mkdir(pasta2) # aqui criamos a pasta caso nao exista
                    lb = Label(co_contas, text='Pasta criada com sucesso!')
                lb.place(x=350, y=430)

                # Criar arquivo txt e inserir dados da consulta
                timestr2 = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
                NomeArq2 = 'conta-'+timestr2+'.txt'
                Directory2 = Path(pasta2)
                file2 = Directory2 / NomeArq2
                for row2 in Nome2:
                    conteudo2.append(row2)
                arquivo2 = open(file2,'w')
                arquivo2.writelines(conteudo2)
                arquivo2.close()

                connection.commit() 

            def voltar():
                co_contas.destroy()
                jan_principal()

            # titulos
            titulo(co_contas)
            a = 'CONSULTAR contas'
            tipotitulo(co_contas, a)

            # LABEL : AGÊNCIA NÚMERO SALDO GERENTE ID_TITULAR RENDA
            lb_id = Label(co_contas, text='AGÊNCIA NÚMERO SALDO GERENTE ID_TITULAR RENDA')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(co_contas, width=40, height=7, bg='snow', bd=0.6, relief='raise')
            C.place(x=175, y=240)
            cursor.execute('''SELECT * FROM contas''')
            x = 1
            for i in cursor.fetchall():
                C.insert(x + 1, i)

            def pesquisa():
                cpfa = str(e_cpf.get())
                c = connection.cursor()
                try:
                    id_titulara = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                    id_titularastr = ''.join([str(item) for item in id_titulara])
                    b = "(,)"
                    for i in range(0,len(b)):
                        id_titularastr =id_titularastr.replace(b[i],"")
                    c.execute('''SELECT * FROM contas WHERE id_titular = '%s';''' % id_titularastr)
                    C = Listbox(co_contas, width=40, height=7, bg='snow', bd=0.6, relief='raise')
                    C.place(x=175, y=240)
                    for i in c.fetchall():
                        C.insert(0, i)
                except:
                    print('erro')

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(co_contas, width=40)
            e_cpf.place(x=295, y=160)

            # Button pesquisar
            btp = Button(co_contas, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : cpf para pesquisa
            lb = Label(co_contas, text='CPF para pesquisa:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # BUTTON Gerar TXT contas
            butt_txt = Button(co_contas, width=20, text='Gerar TXT',
                                 command=bd_txtcontas,
                                 activebackground='gray28',
                                 activeforeground='gray99',
                                 bg='gray99', bd=0.5)
            butt_txt.place(x=200, y=400)

            # button : voltar
            butt_v = Button(co_contas, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=490, y=400)

        def jan_removercontas():
            # janela remover contas
            r_contas = Tk()
            r_contas.title('Removendo Conta')
            r_contas['bg'] = 'bisque'
            r_contas.geometry('700x450+350+100')
            contas.destroy()

            def voltar():
                r_contas.destroy()
                jan_principal()

            # titulos
            titulo(r_contas)
            a = 'REMOVER CONTA'
            tipotitulo(r_contas, a)

            # LABEL : AGÊNCIA NÚMERO SALDO GERENTE ID_TITULAR
            lb_id = Label(r_contas, text='AGÊNCIA NÚMERO SALDO GERENTE ID_TITULAR RENDA')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(r_contas, width=40, height=6, bg='snow', bd=0.6, relief='raise')
            C.place(x=175, y=240)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_cpf.delete(0, END)

                cpfa = e_cpf.get()
                d = connection.cursor()
                id_titular = d.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                id_titularstr = ''.join([str(item) for item in id_titular])
                b = "(,)"
                for i in range(0,len(b)):
                    id_titularstr =id_titularstr.replace(b[i],"")
                d.execute('''SELECT * FROM contas WHERE id_titular = '%s';''' % id_titularstr)
                a = d.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='CPF não encontrado!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    C.delete(0, END)
                else:
                    C.insert(0, a)

            def remover():
                cpfa = e_cpf.get()
                c = connection.cursor()
                id_titulara = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                id_titularastr = ''.join([str(item) for item in id_titulara])
                b = "(,)"
                for i in range(0,len(b)):
                    id_titularastr =id_titularastr.replace(b[i],"")
                c.execute("""DELETE FROM contas WHERE id_titular = '%s'; """ % id_titularastr)
                connection.commit()
                e_cpf.delete(0, END)
                lb_id = Label(r_contas, text='Conta removida')
                lb_id.place(x=320, y=360)
                lb_id['bg'] = 'bisque'
                C.delete(0, END)

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(r_contas, width=40)
            e_cpf.place(x=295, y=160)

            # Button pesquisar
            btp = Button(r_contas, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : cpf para pesquisa
            lb = Label(r_contas, text='Digite o cpf:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # button : remover cadastro
            butt_a = Button(r_contas, width=20,
                            command=remover,
                            text='Remover conta',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_a.place(x=320, y=400)

            # button : voltar
            butt_v = Button(r_contas, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=490, y=400)

        def voltar_a():
            contas.destroy()
            jan_principal()

        # janela contas
        contas = Tk()
        contas.title('contas')
        contas['bg'] = 'bisque'
        contas.geometry('700x450+350+100')
        janela.destroy()
        # titulos
        titulo(contas)
        a = 'contas'
        tipotitulo(contas, a)
        # button cadastrar pessoa
        btac = Button(contas, width=40,
                      command=jan_cadastrocontas,
                      text='Cadastrar Conta',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btac.place(x=200, y=150)

        # button alterar conta
        btaa = Button(contas, width=40,
                      command=jan_alterarcontas,
                      text='Alterar Conta',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btaa.place(x=200, y=200)

        # button Consultar Conta
        btaco = Button(contas, width=40,
                       command=jan_consultarcontas,
                       text='Consultar Conta',
                       activebackground='gray28',
                       activeforeground='gray99',
                       bg='gray99', bd=0.5)
        btaco.place(x=200, y=250)

        # button Remover conta
        btar = Button(contas, width=40,
                      command=jan_removercontas,
                      text='Remover Conta',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btar.place(x=200, y=300)

        # button Voltar
        v = Button(contas, width=40,
                   command=voltar_a,
                   text='Voltar',
                   activebackground='gray28',
                   activeforeground='gray99',
                   bg='gray99', bd=0.5)
        v.place(x=200, y=350)

    def jan_contatos():
        # interface
        def jan_cadastrocontatos():
            def bd_cadcontatos():
                def Ok():
                    erro.destroy()
                    telefone.delete(0, END)
                    e_mail.delete(0, END)
                try:
                    telefonea = str(telefone.get())
                    e_maila = str(e_mail.get())
                    cpfa = str(e_cpf.get())
                    c = connection.cursor()
                    id_titulara = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                    id_titularastr = ''.join([str(item) for item in id_titulara])
                    b = "(,)"
                    for i in range(0,len(b)):
                        id_titularastr =id_titularastr.replace(b[i],"")
                    c.execute('''SELECT * FROM contatos WHERE id_titular = '%s';''' % id_titularastr)
                    telefoneco = c.fetchall()
                    if len(telefoneco) == 0:
                        cursor.execute('''
                        INSERT INTO contatos (telefone, e_mail, id_titular)
                        VALUES('%s','%s','%s')
                        ''' % (telefonea, e_maila, id_titularastr))
                        connection.commit()
                        lb = Label(c_contatos, text='contato cadastrado!')
                        lb.place(x=350, y=400)
                        telefone.delete(0, END)
                        e_mail.delete(0, END)
                except:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')

                    if len(id_titularastr) == 0:
                        lb = Label(erro, text='Pessoa não cadastrada!')
                        lb.place(x=45, y=50)
                    else:
                        lb = Label(erro, text='contato já cadastrado!')
                        lb.place(x=45, y=50)
                    
                    bt = Button(erro, text='OK', command=Ok, )
                    bt.place(x=75, y=85)

            def voltar1():
                c_contatos.destroy()
                jan_principal()

            # janela cadastro contatos
            c_contatos = Tk()
            c_contatos.title('Cadastrando contato')
            c_contatos['bg'] = 'bisque'
            c_contatos.geometry('700x450+350+100')
            contatos.destroy()

            # titulos
            titulo(c_contatos)
            a = 'CADASTRO contato'
            tipotitulo(c_contatos, a)

            def pesquisa():
                cpfa = str(e_cpf.get())
                c = connection.cursor()
                d = connection.cursor()
                try:
                    id_titular = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                    id_titularstr = ''.join([str(item) for item in id_titular])
                    b = "(,)"
                    for i in range(0,len(b)):
                        id_titularstr =id_titularstr.replace(b[i],"")
                    d.execute('''SELECT * FROM contatos WHERE id_titular = '%s';''' % id_titularstr)
                    List_pesq = d.fetchall()
                    if len(id_titularstr) == 0:
                        telefone.delete(0, END)
                        e_mail.delete(0, END)
                        lb = Label(c_contatos, text='Pessoa não cadastrada!')
                    else:
                        if len(List_pesq) == 0:
                            telefone.delete(0, END)
                            e_mail.delete(0, END)
                            lb = Label(c_contatos, text='Preencher os dados de contato!')
                        else:
                            telefonea = List_pesq[0][0]
                            e_maila = List_pesq[0][1]
                            telefone.insert(0, telefonea)
                            e_mail.insert(0, e_maila)
                            lb = Label(c_contatos, text='contato já cadastrado!')
                    lb.place(x=350, y=400)
                except:
                    print('erro')

            # Entrada do CPF pra pesquisar
            e_cpf = Entry(c_contatos, width=40)
            e_cpf.place(x=295, y=118)

            # Button pesquisar
            btp = Button(c_contatos, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=143)

            # nome : cpf para pesquisa
            lb = Label(c_contatos, text='Digite o CPF:')
            lb.place(x=170, y=116)
            lb['bg'] = 'bisque'

            # TELEFONE
            lb_telefone = Label(c_contatos, text='Telefone :')
            lb_telefone.place(x=170, y=180)
            lb_telefone['bg'] = 'bisque'

            # Entrada do telefone
            telefone = Entry(c_contatos, width=45)
            telefone.place(x=230, y=183)

            # e-mail
            lb_e_mail = Label(c_contatos, text='E-mail :')
            lb_e_mail.place(x=170, y=210)
            lb_e_mail['bg'] = 'bisque'

            # Entrada do e-mail
            e_mail = Entry(c_contatos, width=45)
            e_mail.place(x=230, y=213)

            # BUTTON cadastrar contatos
            b_cadastrar = Button(c_contatos, width=20, text='Cadastrar',
                                 command=bd_cadcontatos,
                                 activebackground='gray28',
                                 activeforeground='gray99',
                                 bg='gray99', bd=0.5)
            b_cadastrar.place(x=200, y=350)

            # BUTTON voltar
            b_voltar = Button(c_contatos, width=20, text='Voltar',
                              command=voltar1,
                              activebackground='gray28',
                              activeforeground='gray99',
                              bg='gray99', bd=0.5)
            b_voltar.place(x=350, y=350)
            
        def jan_alterarcontatos():
            # janela alterar contatos
            a_contatos = Tk()
            a_contatos.title('Alterando Cadastro da contato')
            a_contatos['bg'] = 'bisque'
            a_contatos.geometry('700x450+350+100')
            contatos.destroy()

            def voltar():
                a_contatos.destroy()
                jan_principal()

            # titulos
            titulo(a_contatos)
            a = 'ALTERAR CADASTRO DO contato'
            tipotitulo(a_contatos, a)

            # LABEL : TELEFONE E-MAIL ID_TITULAR
            lb_id = Label(a_contatos, text='TELEFONE E-MAIL ID_TITULAR')
            lb_id.place(x=175, y=240)
            lb_id['bg'] = 'bisque'

            # Entrada do CPF pra pesquisar
            e_cpf = Entry(a_contatos, width=40)
            e_cpf.place(x=295, y=180)

            # nome : cpf para pesquisa
            lb = Label(a_contatos, text='Digite o CPF:')
            lb.place(x=170, y=178)
            lb['bg'] = 'bisque'

            # tela de informações
            C = Listbox(a_contatos, width=40, height=3, bg='snow', bd=0.6, relief='raise')
            C.place(x=175, y=260)

            def entradadenovasinf():
                def bd_alterar():
                    telefone = str(nv_telefone.get())
                    e_mail = str(nv_e_mail.get())
                    c = connection.cursor()
                    d = connection.cursor()
                    id_titular = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                    id_titularstr = ''.join([str(item) for item in id_titular])
                    b = "(,)"
                    for i in range(0,len(b)):
                        id_titularstr =id_titularstr.replace(b[i],"")
                    d.execute("""UPDATE contatos
                        SET telefone = '%s', e_mail = '%s' WHERE id_titular = '%s'
                        """ % (telefone, e_mail, id_titularstr))
                    connection.commit()
                    nv_telefone.delete(0, END)
                    nv_e_mail.delete(0, END)
                    if len(id_titularstr) == 0:
                        lb = Label(at_inf, text='Pessoa não selecionada!', font='12')
                    else:
                        lb = Label(at_inf, text='contato atualizado!', font='12')
                    lb.place(x=200, y=380)
                    lb['bg'] = 'bisque'

                c = connection.cursor()
                cpfa = str(e_cpf.get())
                c.execute('''SELECT contatos.* FROM contatos INNER JOIN pessoas ON id = id_titular WHERE cpf = '%s';''' % cpfa)
                at_inf = Tk()
                at_inf.title('Atualizando Cadastro do contato')
                at_inf['bg'] = 'bisque'
                at_inf.geometry('700x450+350+100')
                a_contatos.destroy()

                def voltar_():
                    at_inf.destroy()
                    jan_principal()

                # titulos
                titulo(at_inf)
                a = 'ALTERAR CADASTRO DO contato'
                tipotitulo(at_inf, a)

                # Entrada de novo telefone
                nv_telefone = Entry(at_inf, width=40)
                nv_telefone.place(x=295, y=180)

                # Entrada de novo e-mail
                nv_e_mail = Entry(at_inf, width=40)
                nv_e_mail.place(x=295, y=220)
                
                # Texto - Novo Telefone
                lb_n = Label(at_inf, text='Novo Telefone:')
                lb_n.place(x=170, y=176)
                lb_n['bg'] = 'bisque'

                # Texto - Novo e-mail
                lb_c = Label(at_inf, text='Novo e-mail:')
                lb_c.place(x=170, y=216)
                lb_c['bg'] = 'bisque'

                # button: Alterar
                butt_a = Button(at_inf, width=20,
                                command=bd_alterar,
                                text='Alterar',
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_a.place(x=220, y=350)

                # button : voltar
                butt_v = Button(at_inf, width=20,
                                text='Voltar',
                                command=voltar_,
                                activebackground='gray28',
                                activeforeground='gray99',
                                bg='gray99', bd=0.5)
                butt_v.place(x=380, y=350)

                #Buscar informações do bando de dados
                c = connection.cursor()
                id_titular = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                id_titularstr = ''.join([str(item) for item in id_titular])
                b = "(,)"
                for i in range(0,len(b)):
                    id_titularstr =id_titularstr.replace(b[i],"")
                c.execute('''SELECT * FROM contatos WHERE id_titular = '%s';''' % id_titularstr)
                List_pesq = c.fetchall()
                if len(List_pesq) != 0:
                    telefonea = List_pesq[0][0]
                    e_maila = List_pesq[0][1]
                    nv_telefone.insert(0, telefonea)
                    nv_e_mail.insert(0, e_maila)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_cpf.delete(0, END)

                cpfa = e_cpf.get()
                c = connection.cursor()
                c.execute('''SELECT contatos.* FROM contatos INNER JOIN pessoas ON id = id_titular WHERE cpf = '%s';''' % cpfa)
                a = c.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='CPF não encontrado!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    C.delete(0, END)
                else:
                    C.insert(0, a)

            # button : alterar cadastro
            butt_a = Button(a_contatos, width=20,
                            command=entradadenovasinf,
                            text='Alterar cadastro',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_a.place(x=220, y=350)
            # Button pesquisar
            btp = Button(a_contatos, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=200)

            # button : voltar
            butt_v = Button(a_contatos, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=380, y=350)

        def jan_consultarcontatos():
        # janela consultar contatos
            co_contatos = Tk()
            co_contatos.title('Consultando contato')
            co_contatos['bg'] = 'bisque'
            co_contatos.geometry('700x450+350+100')
            contatos.destroy()

            def bd_txtcontatos():
                # SQL query para selecionar dados dentro da tabela pessoas
                cpfa = str(e_cpf.get())
                c = connection.cursor()
                id_titulara = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                id_titularastr = ''.join([str(item) for item in id_titulara])
                b = "(,)"
                for i in range(0,len(b)):
                    id_titularastr =id_titularastr.replace(b[i],"")
                # SQL query para selecionar dados dentro da tabela contatos
                Select_records2 = "SELECT * FROM contatoS WHERE id_titular = '"+id_titularastr+"'" 
 
                # Selecionar dados na tabela pessoas 
                Nome2 = c.execute(Select_records2)
                Nome2 = ''.join([str(item) for item in Nome2])
                b = "(')"
                for i in range(0,len(b)):
                    Nome2 = Nome2.replace(b[i],"")
                Nome2 = cpfa + ', ' + Nome2

                # Criar pasta 
                pasta2 = "Consulta contato/"
                if os.path.isdir(pasta2): # vemos de este diretorio ja existe
                    lb = Label(co_contatos, text='Ja existe uma pasta com esse nome!')
                else:
                    os.mkdir(pasta2) # aqui criamos a pasta caso nao exista
                    lb = Label(co_contatos, text='Pasta criada com sucesso!')
                lb.place(x=350, y=430)

                # Criar arquivo txt e inserir dados da consulta
                timestr2 = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
                NomeArq2 = 'contato-'+timestr2+'.txt'
                Directory2 = Path(pasta2)
                file2 = Directory2 / NomeArq2
                for row2 in Nome2:
                    conteudo2.append(row2)
                arquivo2 = open(file2,'w')
                arquivo2.writelines(conteudo2)
                arquivo2.close()

                connection.commit() 

            def voltar():
                co_contatos.destroy()
                jan_principal()

            # titulos
            titulo(co_contatos)
            a = 'CONSULTAR contatos'
            tipotitulo(co_contatos, a)

            # LABEL : TELEFONE E-MAIL ID_TITULAR
            lb_id = Label(co_contatos, text='TELEFONE E-MAIL ID_TITULAR')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(co_contatos, width=40, height=7, bg='snow', bd=0.6, relief='raise')
            C.place(x=175, y=240)
            cursor.execute('''SELECT * FROM contatos''')
            x = 1
            for i in cursor.fetchall():
                C.insert(x + 1, i)

            def pesquisa():
                cpfa = str(e_cpf.get())
                c = connection.cursor()
                try:
                    id_titulara = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                    id_titularastr = ''.join([str(item) for item in id_titulara])
                    b = "(,)"
                    for i in range(0,len(b)):
                        id_titularastr =id_titularastr.replace(b[i],"")
                    c.execute('''SELECT * FROM contatos WHERE id_titular = '%s';''' % id_titularastr)
                    C = Listbox(co_contatos, width=40, height=7, bg='snow', bd=0.6, relief='raise')
                    C.place(x=175, y=240)
                    for i in c.fetchall():
                        C.insert(0, i)
                except:
                    print('erro')

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(co_contatos, width=40)
            e_cpf.place(x=295, y=160)

            # Button pesquisar
            btp = Button(co_contatos, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : cpf para pesquisa
            lb = Label(co_contatos, text='CPF para pesquisa:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # BUTTON Gerar TXT contatos
            butt_txt = Button(co_contatos, width=20, text='Gerar TXT',
                                 command=bd_txtcontatos,
                                 activebackground='gray28',
                                 activeforeground='gray99',
                                 bg='gray99', bd=0.5)
            butt_txt.place(x=200, y=400)

            # button : voltar
            butt_v = Button(co_contatos, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=490, y=400)

        def jan_removercontatos():
            # janela remover contatos
            r_contatos = Tk()
            r_contatos.title('Removendo contato')
            r_contatos['bg'] = 'bisque'
            r_contatos.geometry('700x450+350+100')
            contatos.destroy()

            def voltar():
                r_contatos.destroy()
                jan_principal()

            # titulos
            titulo(r_contatos)
            a = 'REMOVER contato'
            tipotitulo(r_contatos, a)

            # LABEL : TELEFONE E-MAIL ID_TITULAR
            lb_id = Label(r_contatos, text='TELEFONE E-MAIL ID_TITULAR')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(r_contatos, width=40, height=6, bg='snow', bd=0.6, relief='raise')
            C.place(x=175, y=240)

            def pesquisa():
                def Ok():
                    erro.destroy()
                    e_cpf.delete(0, END)

                cpfa = e_cpf.get()
                d = connection.cursor()
                id_titular = d.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                id_titularstr = ''.join([str(item) for item in id_titular])
                b = "(,)"
                for i in range(0,len(b)):
                    id_titularstr =id_titularstr.replace(b[i],"")
                d.execute('''SELECT * FROM contatos WHERE id_titular = '%s';''' % id_titularstr)
                a = d.fetchall()
                if len(a) == 0:
                    erro = Tk()
                    erro.title('Erro')
                    erro.geometry('180x150+620+280')
                    lb = Label(erro, text='CPF não encontrado!')
                    lb.place(x=45, y=50)
                    bt = Button(erro, text='OK', command=Ok)
                    bt.place(x=75, y=85)
                    C.delete(0, END)
                else:
                    C.insert(0, a)

            def remover():
                cpfa = e_cpf.get()
                c = connection.cursor()
                id_titulara = c.execute('''SELECT id FROM pessoas WHERE cpf = '%s';''' % cpfa)
                id_titularastr = ''.join([str(item) for item in id_titulara])
                b = "(,)"
                for i in range(0,len(b)):
                    id_titularastr =id_titularastr.replace(b[i],"")
                c.execute("""DELETE FROM contatos WHERE id_titular = '%s'; """ % id_titularastr)
                connection.commit()
                e_cpf.delete(0, END)
                lb_id = Label(r_contatos, text='contato removido')
                lb_id.place(x=320, y=360)
                lb_id['bg'] = 'bisque'
                C.delete(0, END)

            # Entrada do cpf pra pesquisar
            e_cpf = Entry(r_contatos, width=40)
            e_cpf.place(x=295, y=160)

            # Button pesquisar
            btp = Button(r_contatos, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
            btp.place(x=455, y=185)

            # nome : cpf para pesquisa
            lb = Label(r_contatos, text='Digite o cpf:')
            lb.place(x=170, y=158)
            lb['bg'] = 'bisque'

            # button : remover cadastro
            butt_a = Button(r_contatos, width=20,
                            command=remover,
                            text='Remover contato',
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_a.place(x=320, y=400)

            # button : voltar
            butt_v = Button(r_contatos, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
            butt_v.place(x=490, y=400)

        def voltar_a():
            contatos.destroy()
            jan_principal()

        # janela contatos
        contatos = Tk()
        contatos.title('contatos')
        contatos['bg'] = 'bisque'
        contatos.geometry('700x450+350+100')
        janela.destroy()
        # titulos
        titulo(contatos)
        a = 'contatos'
        tipotitulo(contatos, a)
        # button cadastrar contato
        btac = Button(contatos, width=40,
                      command=jan_cadastrocontatos,
                      text='Cadastrar contato',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btac.place(x=200, y=150)

        # button alterar contato
        btaa = Button(contatos, width=40,
                      command=jan_alterarcontatos,
                      text='Alterar contato',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btaa.place(x=200, y=200)

        # button Consultar contato
        btaco = Button(contatos, width=40,
                       command=jan_consultarcontatos,
                       text='Consultar contato',
                       activebackground='gray28',
                       activeforeground='gray99',
                       bg='gray99', bd=0.5)
        btaco.place(x=200, y=250)

        # button Remover contato
        btar = Button(contatos, width=40,
                      command=jan_removercontatos,
                      text='Remover contato',
                      activebackground='gray28',
                      activeforeground='gray99',
                      bg='gray99', bd=0.5)
        btar.place(x=200, y=300)

        # button Voltar
        v = Button(contatos, width=40,
                   command=voltar_a,
                   text='Voltar',
                   activebackground='gray28',
                   activeforeground='gray99',
                   bg='gray99', bd=0.5)
        v.place(x=200, y=350)

    def jan_consTXT():
        # janela consultar contas
        co_consTXT = Tk()
        co_consTXT.title('Consultando Arquivo TXT')
        co_consTXT['bg'] = 'bisque'
        co_consTXT.geometry('700x450+350+100')
        janela.destroy()
        
        def voltar():
            co_consTXT.destroy()
            jan_principal()

        # titulos
        titulo(co_consTXT)
        a = 'CONSULTAR arquivo TXT'
        tipotitulo(co_consTXT, a)
        

        def pesquisa():
            Tk().withdraw() # Isto torna oculto a janela principal
            filename = askopenfilename() # Isto te permite selecionar um arquivo
            filename1 = filename
            filename = filename[filename.rfind('/') + 1:]

            # Entrada do cpf pra pesquisar
            e_consTXT = Entry(co_consTXT, width=40)
            e_consTXT.place(x=295, y=185)
            e_consTXT.insert(0,filename)

            # LABEL : CONSULTAR DADOS DO TXT
            lb_id = Label(co_consTXT, text='DADOS DO ARQUIVO TXT')
            lb_id.place(x=175, y=220)
            lb_id['bg'] = 'bisque'

            # tela
            C = Listbox(co_consTXT, width=40, height=7, bg='snow', bd=0.6, relief='raise')
            C.place(x=175, y=240)    
            test_str = filename1
            spl_char = filename
            res = test_str.rsplit(spl_char, 1)[0] 
            pasta = res
            Directory = Path(pasta)
            file = Directory / filename
            arq= open(file, 'r') 
            conteudo3 = arq.read() 
            C.insert(0,conteudo3)           

        # Button pesquisar
        btp = Button(co_consTXT, width=10, text='Pesquisar',
                         command=pesquisa,
                         activebackground='gray28',
                         activeforeground='gray99',
                         bg='gray99', bd=0.5)
        btp.place(x=170, y=185)

        # nome : arquivo para pesquisa
        lb = Label(co_consTXT, text='Clique para pesquisa:')
        lb.place(x=170, y=158)
        lb['bg'] = 'bisque'

        # button : voltar
        butt_v = Button(co_consTXT, width=20,
                            text='Voltar',
                            command=voltar,
                            activebackground='gray28',
                            activeforeground='gray99',
                            bg='gray99', bd=0.5)
        butt_v.place(x=490, y=400)

    janela = Tk()
    janela.title('Sistema de Cadastro de Pessoas')
    janela['bg'] = 'bisque'
    janela.geometry('700x450+350+100')

    titulo(janela)

    bta = Button(janela, width=30, text='Pessoas',
                command=jan_pessoas,
                activebackground='gray28',
                activeforeground='gray99',
                bg='gray99', bd=0.5)
    bta.place(x=15, y=150)

    bta1 = Button(janela, width=30, text='Contas',
                command=jan_contas,
                activebackground='gray28',
                activeforeground='gray99',
                bg='gray99', bd=0.5)
    bta1.place(x=240, y=150)

    bta4 = Button(janela, width=30, text='Contatos',
                command=jan_contatos,
                activebackground='gray28',
                activeforeground='gray99',
                bg='gray99', bd=0.5)
    bta4.place(x=465, y=150)

    bta2 = Button(janela, width=30, text='Importar TXT',
                command=jan_importar,
                activebackground='gray28',
                activeforeground='gray99',
                bg='gray99', bd=0.5)
    bta2.place(x=100, y=190)

    bta3 = Button(janela, width=30, text='Consultar TXT',
                command=jan_consTXT,
                activebackground='gray28',
                activeforeground='gray99',
                bg='gray99', bd=0.5)
    bta3.place(x=400, y=190)

    janela.mainloop()

jan_principal()
