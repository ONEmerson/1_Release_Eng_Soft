## -------------------------------------------------- inicialização -------------------------------------

# Terminal >> 1_ pip install mysql-connector-python <<<<<< para usar o MySQLl
# Terminal >> 1_ pip install requests <<<< para fazer interface
import mysql.connector              #<<<<<< para usar o MySQL
from datetime import datetime
from tkinter import *               #<<<<<< para usar o TKinter (interface)
import customtkinter
from tkinter import ttk             #<<<<<< para usar comboBox, (janela com escolhas clicáveis)



usuario = 'Emerson'
passe = 'one'
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0001',            ##  <<<<< informações de log in do Banco de Dados
    database = 'cine_bd',
)
cursor = conexao.cursor()

print("Conexão com o Banco de Dados realizada com sucesso")

#+++++++++++++++++++++++++++++++++++++++++ instanciação de objetos ++++++++++++++++++++++++++++++++++++++++++
#Cadastrar novo Cinema
#Exemplo: ->> cinema = Cinema('Cineplex', 'Rua A, 123')

#Criar uma nova sala no cinema
#Exemplo: ->> sala1 = Sala(1, 50)
#Exemplo: ->> sala2 = Sala(2, 100)

#Criar um novo Filme
#Exemplo: ->> filme = Filme('Matrix', 'Um hacker descobre a verdadeira natureza da realidade', 120)

#Vender um ingresso
#Exemplo: ->> ingresso = Ingresso('A1', 20, sala1, filme)

#Registrar uma nova venda
#Exemplo: ->> venda = Venda('2022-01-01', '20:00', 20, [ingresso])
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#++++++++++++++++++++++++++++++++++++++++++++ instancias ++++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##--------------------------------------------------- funções -------------------------------------------
opcaoModificar = ["Assento", "Código", "Nome", "Sala"]
##--------------------------------------------------- CREATE -------------------------------------------
def create():
    fazTipo()
    fazData()

    comando = f'INSERT INTO ingresso( nome_cliente,' \
              f' sala,' \
              f' assento,' \
              f' valor,' \
              f' tipo_entrada,' \
              f' data,' \
              f' hora)' \
              f' VALUES("{nome.get()}",' \
              f' {sala.get()},' \
              f' "{assento.get()}",' \
              f' {valor.get()},' \
              f' "{tipo}",' \
              f'"{dataIda}",' \
              f' "{hora}")'

    cursor.execute(comando)
    conexao.commit()  ## <<<< quando se edita o banco de dados
    novaReservaMsgmLabel.configure(text=f'\n_______________________________' \
                                  f'\nReserva realizada com sucesso' \
                                  f'\n_______________________________' \
                                  f'\n{"Assento:"} {assento.get():>40}' \
                                  f'\n{"Valor:"}{"R$: "+valor.get():>40}' \
                                  f'\n{"Nome:"}{nome.get():>40}' \
                                  f'\n{"Sala:"}{sala.get():>40}' \
                                  f'\n{"Tipo:"}{tipo:>40}' \
                                  f'\n' \
                                  f'\n=========Adcionado=========' \
                                  f'\n Data:__________ {dataEscrita:<7}' \
                                  f'\nHora:_________ {hora:<7}' \
                                  f'\n===========================')

##--------------------------------------------------- CREATE FIM-------------------------------------------

                                                     #READ
##--------------------------------------------------- READ -------------------------------------------
def read():
    comando = f'SELECT * FROM ingresso;'
    cursor.execute(comando)
    resultado = cursor.fetchall() ## <<<< ler o banco de dados
    exibir(resultado)

#    print("Numero de linhas retornadas: ", cursor.rowcount)
#    for resultados in resultado:
#        print("cod:", resultados[0])
#        print("nome:", resultados[1])
#        print("sala:", resultados[2])
#        print("assento:", resultados[3])
#        print("valor:", resultados[4])
#        print("tipo: ", resultados[5])
#        print("data:", resultados[6])
#        print("hora:", resultados[7])


##--------------------------------------------------- READ FIM -------------------------------------------

                                                     #UPDATE
##--------------------------------------------------- UPDATE -------------------------------------------
def update():

        match txt:
            case "Código": # Código

                fazTipo()
                fazData()
                comando = f'UPDATE ingresso SET' \
                          f' cod = "{codigo.get()}",' \
                          f' nome_cliente = "{nome.get()}",'\
                          f' sala = "{sala.get()}",' \
                          f' valor = "{valor.get()}",' \
                          f'tipo_entrada = "{tipo}",' \
                          f' assento = "{assento.get()}",'\
                          f' data = "{dataIda}",' \
                          f' hora = "{hora}"' \
                          f' WHERE cod = "{int(Descricao.get())}"'
                cursor.execute(comando)
                conexao.commit()  ##  <<<< editar o banco de dados

                novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                              f'\n\nAssento: {assento.get()}' \
                                              f'\nValor: R${valor.get()}' \
                                              f'\nNome: {nome.get()}' \
                                              f'\nSala: {sala.get()}' \
                                              f'\nTipo: {tipo}' \
                                              f'\n\n=======Adcionado=======' \
                                              f'\nData:{dataEscrita}' \
                                              f'\nHora:{hora}' \
                                              f'\n=======================')
                return 0

            case "Nome": # Nome

                fazTipo()
                fazData()

                comando = f'UPDATE ingresso SET' \
                          f' cod = "{codigo.get()}",' \
                          f' nome_cliente = "{nome.get()}",'\
                          f' sala = "{sala.get()}",' \
                          f' valor = "{valor.get()}",' \
                          f'tipo_entrada = "{tipo}",' \
                          f' assento = "{assento.get()}",' \
                          f' data = "{dataIda}",' \
                          f' hora = "{hora}"' \
                          f' WHERE nome_cliente = "{Descricao.get()}" AND assento = "{DescricaoParaSala.get()}" AND sala = "{DescricaoParaAssento.get()}"'
                print(comando)
                cursor.execute(comando)
                conexao.commit()  ##  <<<< editar o banco de dados

                novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                               f'\n\nAssento: {assento.get()}' \
                                               f'\nValor: R${valor.get()}' \
                                               f'\nNome: {nome.get()}' \
                                               f'\nSala: {sala.get()}' \
                                               f'\nTipo: {tipo}' \
                                               f'\n\n=======Adcionado=======' \
                                               f'\nData:{dataEscrita}' \
                                               f'\nHora:{hora}' \
                                               f'\n=======================')
                return 0

            case "Sala": # Sala

                fazTipo()
                fazData()

                comando = f'UPDATE ingresso SET' \
                          f' cod = "{codigo.get()}",' \
                          f' nome_cliente = "{nome.get()}",' \
                          f' sala = "{sala.get()}",' \
                          f' valor = "{valor.get()}",' \
                          f' tipo_entrada = "{tipo}",' \
                          f' assento = "{assento.get()}",' \
                          f' data = "{dataIda}",' \
                          f' hora = "{hora}"' \
                          f' WHERE sala = "{Descricao.get()}" AND assento = "{DescricaoParaAssento.get()}"'
                print(comando)
                cursor.execute(comando)
                conexao.commit()  ##  <<<< editar o banco de dados

                novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                                    f'\n\nAssento: {assento.get()}' \
                                                    f'\nValor: R${valor.get()}' \
                                                    f'\nNome: {nome.get()}' \
                                                    f'\nSala: {sala.get()}' \
                                                    f'\nTipo: {tipo}' \
                                                    f'\n\n=======Adcionado=======' \
                                                    f'\nData:{dataEscrita}' \
                                                    f'\nHora:{hora}' \
                                                    f'\n=======================')
                return 0

            case "Assento": #Assento

                fazTipo()
                fazData()

                comando = f'UPDATE ingresso SET' \
                          f' cod = "{codigo.get()}",' \
                          f' nome_cliente = "{nome.get()}",' \
                          f' sala = "{sala.get()}",' \
                          f' valor = "{valor.get()}",' \
                          f'tipo_entrada = "{tipo}",' \
                          f' assento = "{assento.get()}",' \
                          f' data = "{dataIda}",' \
                          f' hora = "{hora}"' \
                          f' WHERE assento = "{Descricao.get()}" AND sala = "{DescricaoParaSala.get()}"'
                cursor.execute(comando)
                conexao.commit()  ##  <<<< editar o banco de dados

                novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                              f'\n\nAssento: {assento.get()}' \
                                              f'\nValor: R${valor.get()}' \
                                              f'\nNome: {nome.get()}' \
                                              f'\nSala: {sala.get()}' \
                                              f'\nTipo: {tipo}' \
                                              f'\n\n=======Adcionado=======' \
                                              f'\nData:{dataEscrita}' \
                                              f'\nHora:{hora}' \
                                              f'\n=======================')
                return 0

            case _:
                novaReservaMsgmLabel.configure(text=f'Opção {txt}: --> {Descricao.get()} <--\nnão é válida.\nPor favor confira a escolha \ne \ntente novamente.')
                return 0

##--------------------------------------------------- UPDATE FIM -------------------------------------------


                                                     #DELETE
##--------------------------------------------------- DELETE -------------------------------------------

def delete():
        match txt:
            case 'Código': # Código
                cod = int(Descricao.get())
                comando = f'DELETE FROM ingresso WHERE cod = {cod}'
                cursor.execute(comando)
                conexao.commit()  # <<< editar o banco de dados
                msgmConfirm.configure(text=f'Reservas de {txt}: ({cod})\n apagada com sucesso!')
                return 0
            case "Nome": # Nome
                comando = f'DELETE FROM ingresso WHERE nome_cliente = "{Descricao.get()}" AND sala="{DescricaoParaSala.get()}" AND assento="{DescricaoParaAssento.get()}"'
                cursor.execute(comando)
                conexao.commit()  # <<< editar o banco de dados
                msgmConfirm.configure(text=f'Reservas de: ( Nome {Descricao.get()}, Sala {DescricaoParaSala.get()}, Assento {DescricaoParaAssento.get()})\n apagada com sucesso!')
                return 0
            case "Assento": # Assento
                comando = f'DELETE FROM ingresso WHERE assento = "{Descricao.get()}" AND sala = "{DescricaoParaSala.get()}"'
                cursor.execute(comando)
                conexao.commit()  # <<< editar o banco de dados
                msgmConfirm.configure(text=f'Reservas de {txt} {Descricao.get()}: ( Sala {DescricaoParaSala.get()} )\n apagada com sucesso!')
                return 0
            case "Sala": # Sala
                comando = f'DELETE FROM ingresso WHERE sala = "{Descricao.get()}" AND assento = "{DescricaoParaAssento.get()}"'
                cursor.execute(comando)
                conexao.commit()  # <<< editar o banco de dados
                msgmConfirm.configure(text=f'Reserva de {txt} {Descricao.get()}: ( Assento {DescricaoParaAssento.get()} ) apagada com sucesso!')
            case _:
                msgmConfirm["text"] = f'Opção ({txt}) não é válida.\nPor favor confira a escolha e tente novamente.'
                return 0

##--------------------------------------------------- DELETE FIM -------------------------------------------

def fazTipo():
    global tipo
    v = int(valor.get())
    if ( v > 10):
        tipo = "Inteira"
    elif (v == 10):
        tipo = "Meia"
    elif (v < 10 and v > 0):
        tipo = "Promocional"
    else:
        tipo = "Cortesia"


def fazData():
    global dataCrua
    global dataIda
    global dataEscrita
    global hora
    dataCrua = datetime.now()
    dataIda = f'{dataCrua:%y/%m/%d}'
    dataEscrita = f'{dataCrua:%d/%m/%y}'
    hora = f'{dataCrua:%H:%M:%S}'

##--------------------------------------------------- TELA LOG IN ------------------------------------------

def logIn():
    global janelaLogIn
    janelaLogIn = customtkinter.CTkToplevel()
    janelaLogIn.title("Janela Log In")
    fontePadrao = ("Comic Sans MS", 18)
    janelaLogIn.geometry("350x300")
    janelaLogIn.resizable()


    titulo = customtkinter.CTkLabel(janelaLogIn, text="Dados do Administrador",font=("Roboto", 20))
    titulo.pack()

    global nomeLog
    nomeLog = customtkinter.CTkEntry(janelaLogIn, placeholder_text="Usuário", font=("",15))
    nomeLog.pack(pady=12, padx=10)


    global senha
    senha = customtkinter.CTkEntry(janelaLogIn, placeholder_text="Senha", show="*", font=("",15))
    senha.pack(pady=12, padx=10)


    BotaoAutenticar = customtkinter.CTkButton(janelaLogIn, text="Autenticar",font=("Arial", 15), command=verificaSenha)
    BotaoAutenticar.pack(pady=12)
    lembrar = customtkinter.CTkCheckBox(janelaLogIn, text="Lembrar nessa sessão")
    lembrar.pack(pady=8)

    global mensagem
    mensagem = customtkinter.CTkLabel(janelaLogIn, text="", font=fontePadrao)
    mensagem.pack(pady=15)

#Método verificar senha
def verificaSenha():
    if (nomeLog.get() != usuario):
        mensagem.configure(text="Usuário inválido",text_color='red')

    elif(senha.get() != passe):
        mensagem.configure(text="Senha incorreta",text_color='red')
    else:
        if (log == "Apagar"):
            apagando()
        elif (log == "Editar"):
            editando()
        mensagem.configure(text="Autenticado",text_color='green')
        janelaLogIn.destroy

##--------------------------------------------------- TELA LOG IN FIM --------------------------------------
##--------------------------------------------------- JANELA NOVA RESERVA -------------------------------------------

def novaReserva():
    janelaEnstradaDados = customtkinter.CTkToplevel()
    janelaEnstradaDados.title("Nova Reserva")
    fontePadrao = ("Comic Sans MS", "10")
    janelaEnstradaDados.geometry("250x505")
    # --------------------------------- CONTAINERS ENTRADA DE DADOS --------------------------------

    titulo = customtkinter.CTkLabel(janelaEnstradaDados, text="NOVA RESERVA",font=("Agency FB", 15, "bold"))
    titulo.pack()

    global nome
    nome = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Nome")
    nome.pack(pady=12, padx=10)

    global sala
    sala = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Sala")
    sala.pack(pady=12, padx=10)

    global assento
    assento = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Assento")
    assento.pack(pady=12, padx=10)

    global valor
    valor = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Valor")
    valor.pack(pady=12, padx=10)

    botaoOkEntradaDados = customtkinter.CTkButton(janelaEnstradaDados, text="Ok", font=("Comics Sans MS", 10, "bold"),
                                                  command=create)
    botaoOkEntradaDados.pack(pady=12)

    global novaReservaMsgmLabel
    novaReservaMsgmLabel = customtkinter.CTkLabel(janelaEnstradaDados, text="Campo de confirmação:")
    novaReservaMsgmLabel.pack(pady=2)

##--------------------------------------------------- JANELA NOVA RESERVA FIM -------------------------------------------

def duasFuncApagar():
    msgm2Del()
    confirmDelet()

def duasFuncEdit():
    msgm2Del()
    confirmEdit()

def confirmEdit():
    global msgmConfirm
    msgmConfirm = customtkinter.CTkLabel(janelaApagarReserva, text="")
    msgmConfirm.place(x=20,y=180)
    update()

def confirmDelet():
    global log
    log = "Apagar"
    global msgmConfirm
    msgmConfirm = customtkinter.CTkLabel(janelaApagarReserva, text=" Obrigatório preencher todos os campos ")
    msgmConfirm.place(x=20,y=180)
    delete()


def msgm2Edit():
    global txt
    global Descricao
    global DescricaoParaAssento
    global DescricaoParaSala
    txt = comboOpcao.get()

    Descricao = customtkinter.CTkEntry(janelaApagarReserva, placeholder_text=txt, font=("Arial", 16))
    Descricao.place(x=170, y=50)

    if(txt == "Sala"):
        DescricaoParaAssento = customtkinter.CTkEntry(janelaApagarReserva, placeholder_text="Assento", font=("Arial", 16))
        DescricaoParaAssento.place(x=170, y=80)

    elif (txt == "Assento"):
        DescricaoParaSala = customtkinter.CTkEntry(janelaApagarReserva, placeholder_text="Sala", font=("Arial", 16))
        DescricaoParaSala.place(x=170, y=80)

    elif(txt == "Nome"):
        DescricaoParaSala = customtkinter.CTkEntry(janelaApagarReserva, placeholder_text="Assento", font=("Arial", 16))
        DescricaoParaSala.place(x=170, y=80)
        DescricaoParaAssento = customtkinter.CTkEntry(janelaApagarReserva, placeholder_text="Sala", font=("Arial", 16))
        DescricaoParaAssento.place(x=170, y=110)

    botao.destroy()
    botao2 = customtkinter.CTkButton(janelaApagarReserva, text="EDITAR", command=reservaEdit)
    botao2.place(x=100, y=220)

def msgm2Del():
    global txt
    global Descricao
    global DescricaoParaAssento
    global DescricaoParaSala
    txt = comboOpcao.get()

    Descricao = customtkinter.CTkEntry(janelaApagarReserva, placeholder_text=txt, font=("Arial", 16))
    Descricao.place(x=170, y=50)


    if(txt == "Sala"):
        DescricaoParaAssento = customtkinter.CTkEntry(janelaApagarReserva, placeholder_text="Assento", font=("Arial", 16))
        DescricaoParaAssento.place(x=170, y=80)

    elif (txt == "Assento"):
        DescricaoParaSala = customtkinter.CTkEntry(janelaApagarReserva, placeholder_text="Sala", font=("Arial", 16))
        DescricaoParaSala.place(x=170, y=80)

    elif(txt == "Nome"):
        DescricaoParaSala = customtkinter.CTkEntry(janelaApagarReserva, placeholder_text="Sala", font=("Arial", 16))
        DescricaoParaSala.place(x=170, y=80)
        DescricaoParaAssento = customtkinter.CTkEntry(janelaApagarReserva, placeholder_text="Assento", font=("Arial", 16))
        DescricaoParaAssento.place(x=170, y=110)

    botao.destroy()
    botao2 = customtkinter.CTkButton(janelaApagarReserva, text="APAGAR", command=confirmDelet)
    botao2.place(x=100, y=220)


##--------------------------------------------------- APAGAR RESERVA ---------------------------------------
def apagarReserva():
    global log
    log = "Apagar"
    logIn()

def editarReserva():
    global log
    log = "Editar"
    logIn()

def editando():
    global janelaApagarReserva
    janelaApagarReserva = customtkinter.CTkToplevel()
    janelaApagarReserva.geometry("350x280")
    janelaApagarReserva.resizable(True, True)
    janelaApagarReserva.title("Editor de RESERVAS")

    comboLabel = customtkinter.CTkLabel(janelaApagarReserva, text=" Editar a partir de: ", font=("Arial", 16))
    comboLabel.place(x=30, y=20)

    global txt
    global comboOpcao
    comboOpcao = customtkinter.CTkComboBox(janelaApagarReserva, values=opcaoModificar, font=("", 15))
    comboOpcao.place(x=170, y=20)

    txt = comboOpcao.get()

    global botao
    botao = customtkinter.CTkButton(janelaApagarReserva, text="Confirmar escolha", font=("", 15), command=msgm2Edit)
    botao.place(x=100, y=220)

def apagando():
    global janelaApagarReserva
    janelaApagarReserva = customtkinter.CTkToplevel()
    janelaApagarReserva.geometry("350x280")
    janelaApagarReserva.resizable(True, True)
    janelaApagarReserva.title("Apagar reserva")

    comboLabel = customtkinter.CTkLabel(janelaApagarReserva, text=" Apagar a partir de: ", font=("Arial", 16))
    comboLabel.place(x=30, y=20)

    global comboOpcao
    comboOpcao = customtkinter.CTkComboBox(janelaApagarReserva, values=opcaoModificar, font=("", 15))
    comboOpcao.place(x=170, y=20)

    txt=comboOpcao.get()

    global botao
    botao = customtkinter.CTkButton(janelaApagarReserva, text="Confirmar escolha", font=("", 15), command=msgm2Del)
    botao.place(x=100, y=220)

##--------------------------------------------------- APAGAR RESERVA FIM ---------------------------------------

def reservaEdit():
    janelaEnstradaDados = customtkinter.CTkToplevel()
    janelaEnstradaDados.title("Editor de Reservas")
    janelaEnstradaDados.geometry("250x545")

    titulo = customtkinter.CTkLabel(janelaEnstradaDados, text="EDITOR DE RESERVA", font=("Agency FB", 20, "bold"))
    titulo.pack(pady=5)

    global codigo
    codigo = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Novo CÓDIGO")
    codigo.pack(pady=12, padx=10)

    global nome
    nome = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Novo NOME")
    nome.pack(pady=12, padx=10)

    global sala
    sala = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Novo SALA")
    sala.pack(pady=12, padx=10)

    global assento
    assento = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Novo ASSENTO")
    assento.pack(pady=12, padx=10)

    global valor
    valor = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Valor")
    valor.pack(pady=12, padx=10)


    botaoOkEntradaDados = customtkinter.CTkButton(janelaEnstradaDados, text="Ok",command=confirmEdit)
    botaoOkEntradaDados.pack(pady=10)

    global novaReservaMsgmLabel
    novaReservaMsgmLabel = customtkinter.CTkLabel(janelaEnstradaDados, text="Campo de confirmação:")
    novaReservaMsgmLabel.pack()

#----------------------------------------------------------------------------------------------------------


##--------------------------------------------------- TREEVIEW INICIO-------------------------------------------
def exibir(resultado):
    janelaTREEVIEW = customtkinter.CTkToplevel()
    janelaTREEVIEW.title("Tabela")

    tree = ttk.Treeview(janelaTREEVIEW, columns=("column1","column2", "column3","column4",
                                                 "column5", "column6", "column7", "column8"), # <<< ATRIBUTO RETIRADO [, "column9" ]
                                                show='headings')

    tree.column("column1", width=90, minwidth=14, stretch=YES)
    tree.heading("#1", text='Código')

    tree.column("column2", width=160, minwidth=40, stretch=YES)
    tree.heading("#2", text='Nome')

    tree.column("column3", width=75, minwidth=12, stretch=YES)
    tree.heading("#3", text='Sala')

    tree.column("column4", width=100, minwidth=18, stretch=YES)
    tree.heading("#4", text='Assento')

    tree.column("column5", width=70, minwidth=14, stretch=YES)
    tree.heading("#5", text='Valor')

    tree.column("column6", width=90, minwidth=15, stretch=YES)
    tree.heading("#6", text='Tipo')

    tree.column("column7", width=100, minwidth=11, stretch=YES)
    tree.heading("#7", text='Data')

    tree.column("column8", width=55, minwidth=12, stretch=YES)
    tree.heading("#8", text='Hora')

    '''tree.column("column9", width=95, minwidth=12, stretch=YES)
    tree.heading("#9", text='cliente_cod')'''

    print(resultado)
    tree.grid(row=0, column=0)
    for (c,n,s,a,v,t,d,h) in resultado:
        tree.insert("", END, values= (f'{c:^20}',f'{n:^40}',f'{s:^20}',
                                      f'{a:^30}',f'{v:^20}',f'{t:^20}',
                                      f'{d:        %d/%m/%y}',f'{h:}',
                                      ))#f'{cc:^20}'))


##--------------------------------------------------- TREEVIEW FIM -------------------------------------------

##--------------------------------------------------- JANELA PRINCIPAL -------------------------------------------


# ***********************************************************************************************************************
# ************************************************       TK INTER        ************************************************
# ***********************************************************************************************************************
def setMode():
    if(mode.get()== 0):
        customtkinter.set_appearance_mode("light")
    else:
        customtkinter.set_appearance_mode("dark")

def setColor():
    if(color.get()== 0):
        customtkinter.set_default_color_theme("green")
        color.configure(text='Cor Azul')
    else:
        customtkinter.set_default_color_theme("blue")
        color.configure(text='implementação futura')


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")
# ------------------------------------------------------------ TEMA ------------------------------------------------------

root = customtkinter.CTk()
root.geometry("550x400")
fontePadrao = ("Arial", "10")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady="20", padx=60, fill="both", expand=True)

root.title("CInema")

label = customtkinter.CTkLabel(master=frame, text="Cinema dus Film", font=("Roboto", 20))
label.pack(pady=12, padx=10)


texto_espaco = customtkinter.CTkLabel(master=frame, text="", width=14, height=2)
texto_espaco.pack()

botao1 = customtkinter.CTkButton(master=frame, text="Nova RESERVA ", command=novaReserva)
botao1.pack(pady=12, padx=10)

botao2 = customtkinter.CTkButton(master=frame, text="Apagar RESERVA", command=apagarReserva)
botao2.pack(pady=12, padx=10)

botao3 = customtkinter.CTkButton(master=frame, text="Editar RESERVA", command=editarReserva)
botao3.pack(pady=12, padx=10)

botao4 = customtkinter.CTkButton(master=frame, text="ExibirRESERVAS", command=read)
botao4.pack(pady=12, padx=10)

mode = customtkinter.CTkCheckBox(master=frame, text="Dark Mode", command=setMode)
mode.pack(side=LEFT,pady=12, padx=10)

color = customtkinter.CTkSwitch(master=frame, text="Cor Azul", text_color="blue", command=setColor)

color.pack(side=LEFT,pady=12, padx=10)

root.mainloop()

##------------------------------------------- Janela principal FIM -----------------------------------------------------

##--------------------------------------------------- Encerrar conexão -------------------------------------------
cursor.close()
conexao.close()
##--------------------------------------------------- Encerrado -------------------------------------------
