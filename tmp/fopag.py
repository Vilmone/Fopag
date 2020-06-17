#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import Tkinter as tk
from Tkinter import *


janela = tk.Tk()
m = []
m2 = []

imgFundo =tk.PhotoImage(file="C:/tmp/img.gif")
fundo = tk.Label(janela, width = 500, height = 600, image=imgFundo)
fundo.imgFundo=imgFundo
fundo.pack()
fundo.place(x=0, y=0)

pg = Label(janela, text="FoPag", width=6, height=2, font="Arial, 24")
pg.place(x=200, y=10) 
pg.pack()

'''def limpar_cadastro()'''
    

def cadastrar(event):
    cadastro = Tk()
    cadastro.title("Cadastro") 
    cadastro.geometry("580x250+250+250")
    
    codigo = Label(cadastro, text="     Código  ", font="Arial, 11")
    Entry_codigo = Entry(cadastro)
   

    nome = Label(cadastro, text="   Nome  ", font="Arial, 11")
    Entry_nome = Entry(cadastro)

    cpf = Label(cadastro, text=" CPF  ", font="Arial, 11")
    Entry_cpf = Entry(cadastro)

    endereco = Label(cadastro, text="         Endereço  ", font="Arial, 11")
    Entry_endereco = Entry(cadastro)

    cidade = Label(cadastro, text="     Cidade  ", font="Arial, 11")
    Entry_cidade = Entry(cadastro)

    cep = Label(cadastro, text="CEP  ", font="Arial, 11")
    Entry_cep = Entry(cadastro)

    telefone = Label(cadastro, text="        Telefone  ", font="Arial, 11")
    Entry_telefone = Entry(cadastro)

    email = Label(cadastro, text="     E-mail  ", font="Arial, 11")
    Entry_email= Entry(cadastro)

    cargo = Label(cadastro, text="    Cargo  ", font="Arial, 11")
    Entry_cargo = Entry(cadastro)

    salario = Label(cadastro, text="     Salário  ", font="Arial, 11")
    Entry_salario = Entry(cadastro)

    admissao = Label(cadastro, text="           Admissão  ", font="Arial, 11")
    Entry_admissao = Entry(cadastro)

    data_nascimento = Label (cadastro, text="                  Data de Nasc.  ", font="Arial, 11")
    Entry_data = Entry(cadastro)

    rg = Label (cadastro, text="RG  ", font="Arial, 11") 
    Entry_rg = Entry(cadastro)

    bairro = Label(cadastro, text="     Bairro  ", font="Arial, 11")
    Entry_bairro = Entry(cadastro)

    estado = Label(cadastro, text="       Estado  ", font="Arial, 11")
    Entry_estado = Entry(cadastro)
    


    codigo.grid(row = 0)
    nome.grid(row=1)
    cpf.grid(row=2)
    endereco.grid(row=3)
    cidade.grid(row=4)
    cep.grid(row=5)
    telefone.grid(row=6)
    email.grid(row=7)
    cargo.grid(row=8)
    salario.grid(row=9)
    admissao.grid(row=0, column= 15)
    data_nascimento.grid(row=1, column=15)
    rg.grid(row=2, column=15)
    bairro.grid(row=3, column=15)
    estado.grid(row=4, column=15)

    Entry_codigo.grid(row=0, column=1)
    Entry_nome.grid(row=1, column=1)
    Entry_cpf.grid(row=2, column=1)
    Entry_endereco.grid(row=3, column=1)
    Entry_cidade.grid(row=4, column=1)
    Entry_cep.grid(row=5, column=1)
    Entry_telefone.grid(row=6, column=1)
    Entry_email.grid(row=7, column=1)
    Entry_cargo.grid(row=8, column=1)
    Entry_salario.grid(row=9, column=1)
    Entry_admissao.grid(row=0, column=16)
    Entry_data.grid(row=1, column= 16)
    Entry_rg.grid(row=2, column=16)
    Entry_bairro.grid(row=3, column=16)
    Entry_estado.grid(row=4, column=16)

    def gravar(event):
        dado=[]
        
        dado.append (Entry_codigo.get())
        dado.append (Entry_nome.get())
        dado.append (Entry_cpf.get())
        dado.append (Entry_endereco.get())
        dado.append (Entry_cidade.get())
        dado.append (Entry_cep.get())
        dado.append (Entry_telefone.get())
        dado.append (Entry_email.get())
        dado.append (Entry_cargo.get())
        dado.append (Entry_salario.get())
        dado.append (Entry_admissao.get())
        dado.append (Entry_data.get())
        dado.append (Entry_rg.get())
        dado.append (Entry_bairro.get())
        dado.append (Entry_estado.get())
        m.append (dado)
        dado = []
        for i in range(len(m)):
            print(m[i])

        cadastro.destroy()

        

        
    def cancelar(event):
        cadastro.destroy()
    
    bot_gravar = Button(cadastro, text="  Gravar  ", font="Arial, 9")
    bot_gravar.grid(row=9, column= 16)
    bot_gravar.bind("<Button-1>", gravar)
 
    bot_cancelar = Button(cadastro, text="  Cancelar  ", font="Arial, 9")
    bot_cancelar.grid(row=9, column= 15)
    bot_cancelar.bind("<Button-1>", cancelar)

    cadastro.mainloop()

bot_Cadastrar = Button(janela, text="   Cadastrar   ", width=8, height=2, font="Arial, 9") 
bot_Cadastrar.place(x=400, y=550)

bot_Cadastrar.bind("<Button-1>", cadastrar)

def consultar(event):
    consulta = Tk()
    consulta.title("Consulta") 
    #consulta.geometry("300x250+500+150")
    dado2 = []
    lista = Listbox(consulta)
    #lista.place(x=133, y=23)
    lista.pack()

    '''pesquisa = Label(consulta, text="  Pesquisar nome:  ", font="Arial, 11")
    Entry_pesquisa = Entry(consulta)
    pesquisa.grid(row=0)
    Entry_pesquisa.grid(row=0, column=1)
    lista.delete(1, lista.size())'''
    
    for i in range(len(m)):
        dado2.append(m[i][0])
        dado2.append(m[i][1])
        name = dado2[1]

        lista.insert(END, name)
        dado2=[] 
    
    def duplo_clique(event):
        ficha = Tk()
        ficha.title("ficha") 
        ficha.geometry("700x250+250+250")
 
        print(lista.index(ACTIVE))
        j= lista.index(ACTIVE)

        text_codigo = m[j][0]
        text_nome = m[j][1]
        text_cpf = m[j][2]
        text_endereco = m[j][3]
        text_cidade = m[j][4]
        text_cep = m[j][5]
        text_telefone = m[j][6]
        text_email = m[j][7]
        text_cargo = m[j][8]
        text_salario = m[j][9]
        text_admissao = m[j][10]
        text_data_nascimento = m[j][11]
        text_rg = m[j][12]
        text_bairro = m[j][13]
        text_estado = m[j][14]

        codigo_2 = Label(ficha, text="     Código  ", font="Arial, 11")
        codigo_ficha = Label(ficha, text= text_codigo , font="Arial, 11")

        nome_2 = Label(ficha, text="   Nome  ", font="Arial, 11")
        nome_ficha = Label(ficha, text= text_nome, font="Arial, 11")

        cpf_2 = Label(ficha, text=" CPF  ", font="Arial, 11")
        cpf_ficha = Label(ficha, text= text_cpf, font="Arial, 11")

        endereco_2 = Label(ficha, text="         Endereço  ", font="Arial, 11")
        endereco_ficha = Label(ficha, text= text_endereco, font="Arial, 11")
        
        cidade_2 = Label(ficha, text="     Cidade  ", font="Arial, 11")
        cidade_ficha = Label(ficha, text= text_cidade, font="Arial, 11")

        cep_2 = Label(ficha, text="CEP  ", font="Arial, 11")
        cep_ficha = Label(ficha, text= text_cep, font="Arial, 11")

        telefone_2 = Label(ficha, text="        Telefone  ", font="Arial, 11")
        telefone_ficha = Label(ficha, text= text_telefone, font="Arial, 11")

        email_2 = Label(ficha, text="     E-mail  ", font="Arial, 11")
        email_ficha = Label(ficha, text= text_email, font="Arial, 11")

        cargo_2 = Label(ficha, text="    Cargo  ", font="Arial, 11")
        cargo_ficha = Label(ficha, text= text_cargo, font="Arial, 11")

        salario_2 = Label(ficha, text="     Salário  ", font="Arial, 11")
        salario_ficha = Label(ficha, text= text_salario, font="Arial, 11")

        admissao_2 = Label(ficha, text="           Admissão  ", font="Arial, 11")
        admissao_ficha = Label(ficha, text= text_admissao, font="Arial, 11")

        data_nascimento_2 = Label (ficha, text="                  Data de Nasc.  ", font="Arial, 11")
        data_nascimento_ficha = Label(ficha, text= text_data_nascimento, font="Arial, 11")

        rg_2 = Label (ficha, text="RG  ", font="Arial, 11") 
        rg_ficha = Label(ficha, text= text_rg, font="Arial, 11")
         
        bairro_2 = Label(ficha, text="     Bairro  ", font="Arial, 11")
        bairro_ficha = Label(ficha, text= text_bairro, font="Arial, 11")

        estado_2 = Label(ficha, text="       Estado  ", font="Arial, 11")
        estado_ficha = Label(ficha, text= text_estado, font="Arial, 11")

        codigo_2.grid(row = 0)
        nome_2.grid(row=1)
        cpf_2.grid(row=2)
        endereco_2.grid(row=3)
        cidade_2.grid(row=4)
        cep_2.grid(row=5)
        telefone_2.grid(row=6)
        email_2.grid(row=7)
        cargo_2.grid(row=8)
        salario_2.grid(row=9)
        admissao_2.grid(row=0, column= 15)
        data_nascimento_2.grid(row=1, column=15)
        rg_2.grid(row=2, column=15)
        bairro_2.grid(row=3, column=15)
        estado_2.grid(row=4, column=15)
        codigo_ficha.grid(row=0, column=1)
        nome_ficha.grid(row=1, column =1)
        cpf_ficha.grid(row=2, column=1)
        endereco_ficha.grid(row=3, column=1)
        cidade_ficha.grid(row=4, column=1)
        cep_ficha.grid(row=5, column=1)
        telefone_ficha.grid(row=6, column=1)
        email_ficha.grid(row=7, column=1)
        cargo_ficha.grid(row=8, column=1)
        salario_ficha.grid(row=9, column=1)
        admissao_ficha.grid(row=0, column= 16)
        data_nascimento_ficha.grid(row=1, column=16)
        rg_ficha.grid(row=2, column=16)
        bairro_ficha.grid(row=3, column=16)
        estado_ficha.grid(row=4, column=16)

        def espelho(event):
            espelho_ponto = Tk()
            espelho_ponto.title("Espelho de Ponto")
            espelho_ponto.geometry("500x250+400+150")

            segunda = Label(espelho_ponto, text="Segunda-Feira ", font="Arial, 11")

            terca = Label(espelho_ponto, text="Terça-Feira ", font="Arial, 11")

            quarta = Label(espelho_ponto, text="Quarta-Feira ", font="Arial, 11")

            quinta = Label(espelho_ponto, text="Quinta-Feira ", font="Arial, 11")

            sexta = Label(espelho_ponto, text="Sexta-Feira ", font="Arial, 11")

            sabado = Label(espelho_ponto, text="Sábado ", font="Arial, 11")

            domingo = Label(espelho_ponto, text="Domingo ", font="Arial, 11")

            '''entrada_1 = Label(espelho_ponto, text="Entrada ", font="Arial, 11")

            saida_1 = Label(espelho_ponto, text="Saída ", font="Arial, 11")
            
            entrada_2 = Label(espelho_ponto, text="Entrada ", font="Arial, 11")
            
            saida_2 = Label(espelho_ponto, text="Saída ", font="Arial, 11")
            
            horas = Label(espelho_ponto, text="H/Trabalhadas ", font="Arial, 11")'''

            entrada_1 = Label(espelho_ponto, text="|  7:00  ", font="Arial, 11")
            saida_1 = Label(espelho_ponto, text="|  12:00 ", font="Arial, 11")
            entrada_2 = Label(espelho_ponto, text="|  13:00  ", font="Arial, 11")
            saida_2 = Label(espelho_ponto, text="|  16:78  |", font="Arial, 11")
            entrada_3 = Label(espelho_ponto, text="|  7:00  ", font="Arial, 11")
            saida_3 = Label(espelho_ponto, text="|  12:00  ", font="Arial, 11")
            entrada_4 = Label(espelho_ponto, text="|  13:00  ", font="Arial, 11")
            saida_4 = Label(espelho_ponto, text="|  16:48  |", font="Arial, 11")
            entrada_5 = Label(espelho_ponto, text="|  7:00  ", font="Arial, 11")
            saida_5  = Label(espelho_ponto, text="|  12:00  ", font="Arial, 11")
            entrada_6 = Label(espelho_ponto, text="|  13:00  ", font="Arial, 11")
            saida_6 = Label(espelho_ponto, text="|  16:48  |", font="Arial, 11")
            entrada_7 = Label(espelho_ponto, text="|  7:00  ", font="Arial, 11")
            saida_7 = Label(espelho_ponto, text="|  12:00  ", font="Arial, 11")
            entrada_8 = Label(espelho_ponto, text="|  13:00  ", font="Arial, 11")
            saida_8 = Label(espelho_ponto, text="|  16:48  |", font="Arial, 11")
            entrada_9 = Label(espelho_ponto, text="|  7:00  ", font="Arial, 11")
            saida_9 = Label(espelho_ponto, text="|  12:00  ", font="Arial, 11")
            entrada_10 = Label(espelho_ponto, text="|  13:00  ", font="Arial, 11")
            saida_10 = Label(espelho_ponto, text="|  16:48  |", font="Arial, 11")
            entrada_11 = Label(espelho_ponto, text="Compensado ", font="Arial, 11")
            '''saida_11 = Label(espelho_ponto, text="|  12:00  ", font="Arial, 11")
            entrada_12 = Label(espelho_ponto, text="|  13:00  ", font="Arial, 11")
            saida_12 = Label(espelho_ponto, text="|  16:48  |", font="Arial, 11")'''
            entrada_13 = Label(espelho_ponto, text="DSR  ", font="Arial, 11")
            '''saida_13 = Label(espelho_ponto, text="|  12:00  ", font="Arial, 11")
            entrada_14 = Label(espelho_ponto, text="|  13:00  ", font="Arial, 11")
            saida_14 = Label(espelho_ponto, text="|  16:48  |", font="Arial, 11")'''

            
            
            
            segunda.grid(row=1)          
            terca.grid(row=2)
            quarta.grid(row=3)
            quinta.grid(row=4)
            sexta.grid(row=5)
            sabado.grid(row=6)
            domingo.grid(row=7)
            '''entrada_1.grid(row=0, column=1)
            saida_1.grid(row=0, column=2)
            entrada_2.grid(row=0, column=3)
            saida_2.grid(row=0, column=4)'''
            #horas.grid(row=0, column=5)
            
            entrada_1.grid(row=1, column=1)
            saida_1.grid(row=1, column=2)
            entrada_2.grid(row=1, column=3)
            saida_2.grid(row=1, column=4)
            entrada_3.grid(row=2, column=1)
            saida_3.grid(row=2, column=2)
            entrada_4.grid(row=2, column=3)
            saida_4.grid(row=2, column=4)
            entrada_5.grid(row=3, column=1)
            saida_5.grid(row=3, column=2)
            entrada_6.grid(row=3, column=3)
            saida_6.grid(row=3, column=4)
            entrada_7.grid(row=4, column=1)
            saida_7.grid(row=4, column=2)
            entrada_8.grid(row=4, column=3)
            saida_8.grid(row=4, column=4)
            entrada_9.grid(row=5, column=1)
            saida_9.grid(row=5, column=2)
            entrada_10.grid(row=5, column=3)
            saida_10.grid(row=5, column=4)
            entrada_11.grid(row=6, column=1)
            '''saida_11.grid(row=6, column=2)
            entrada_12.grid(row=6, column=3)
            saida_12.grid(row=6, column=4)'''
            entrada_13.grid(row=7, column=1)
            '''saida_13.grid(row=7, column=2)
            entrada_14.grid(row=7, column=3)
            saida_14.grid(row=7, column=4)'''
        


            def holerite_calc(*args):
                
                holerite = Tk()
                holerite.title("Holerite")
                holerite.geometry("400x400+400+150")
                
                
                dm= Label(holerite, text="DEMONSTRATIVO DE PAGAMENTO", font="Arial, 12")
                lb_nome = Label(holerite, text="Nome: ", font="Arial, 11")
                lb_nome2= Label(holerite, text= text_nome, font="Arial, 11")
                lb_cargo = Label(holerite, text="Cargo: ", font="Arial, 11")
                lb_cargo2 = Label(holerite, text= text_cargo, font="Arial, 11")
                
                horas_normais = Label(holerite, text="Horas normais: ", font="Arial, 11")
                inss= Label(holerite, text="INSS: ", font="Arial, 11", )
                irff= Label(holerite, text="IRRF: ", font="Arial, 11")
                plano_odonto = Label(holerite, text="Plano Odontologico: ", font="Arial, 11")
                seguro_vida = Label(holerite, text="Seguro de vida: ", font="Arial, 11")
                refeicao = Label(holerite, text="Refeição: ", font= "Arial, 11")
                unimed = Label (holerite, text="Plano de Saúde: ", font="Arial, 11")
                plano_odonto2 = Label (holerite, text="11,00 ", font="Arial, 11")
                seguro_vida2 = Label (holerite, text="35,00 ", font="Arial, 11")
                refeicao2 = Label(holerite, text="4,00 ", font= "Arial, 11")
                unimed2 = Label (holerite, text="110,00 ", font="Arial, 11")

                dm.grid(row=0)
                lb_nome.grid(row=1)
                lb_nome2.grid(row=1, column=1)
                lb_cargo.grid(row=2)
                lb_cargo2.grid(row=2, column=1)
                
                
                horas_normais.grid(row=3)
                inss.grid(row=4)
                irff.grid(row=5)
                plano_odonto.grid(row=6)
                seguro_vida.grid(row=7)
                refeicao.grid(row=8)
                unimed.grid(row=9)
                plano_odonto2.grid(row=6, column=1)
                seguro_vida2.grid(row=7, column=1)
                refeicao2.grid(row=8, column=1)
                unimed2.grid(row=9, column=1)

                lb_salario= Label(holerite, text=text_salario, font="Arial, 11")

                lb_salario.grid(row=3, column=1)

                fgts = Label(holerite, text="Deposito em Conta do FGTS: ", font="Arial, 11")
                fgts_calc = Label(holerite, text="80,00 ", font="Arial, 11")
                inss_calc = Label(holerite, text="140,00 ", font="Arial, 11")
                irrf_calc = Label(holerite, text="61,00 ", font="Arial, 11")

                fgts.grid(row=10)
                fgts_calc.grid(row=10, column=1)
                inss_calc.grid(row=4, column=1)
                irrf_calc.grid(row=5, column=1)

                
                
                
                
                '''def (*args):
                
                    if(text_salario <= 1.145):
                        text_salario2= (text_salario * 0.075)+text_salario 
                        lb_salario2 = Label(holerite, text=text_salario2, font="Arial, 11")
                        lb_salario2.grid (row=1, column=1)
                    elif((text_salario > 1.145) and (text_salario <= 2.090)):
                        text_salario2= (text_salario * 0.09)+text_salario 
                        lb_salario2 = Label(holerite, text=text_salario2, font="Arial, 11")
                        lb_salario2.grid (row=1, column=1)
                    elif((text_salario>2.090) and (text_salario<=3.135)):
                        text_salario2= (text_salario * 0.12)+text_salario 
                        lb_salario2 = Label(holerite, text=text_salario2, font="Arial, 11")
                        lb_salario2.grid (row=1, column=1)
                    else:
                        text_salario2= (text_salario * 0.14)+text_salario 
                        lb_salario2 = Label(holerite, text=text_salario2, font="Arial, 11")
                        lb_salario2.grid (row=1, column=1)

                    if (text_salario < 1.904):
                        #lb_salario2 = Label(holerite, text=text_salario2, font="Arial, 11")
                        #lb_salario2.grid (row=2, column=1)

                    calc_fgts'''
                
                


                    


            bot_fechar = Button(espelho_ponto, text="Fechar  ", font="Arial, 9")
            bot_fechar.place(x= 300, y=200)

            bot_holerite = Button(espelho_ponto, text="Holerite  ", command=holerite_calc, font="Arial, 9")
            bot_holerite.place(x= 400, y=200)
            '''bot_salvar.bind("<Button-1>", holerite_calc)'''

            '''bot_salvar.bind("<Button-1>", grave)'''


        bot_espelho = Button(ficha, text="  Espelho de Ponto  ", command= espelho, font="Arial, 9")
        bot_espelho.grid(row=9, column= 16)
        bot_espelho.bind("<Button-1>", espelho)
        
    lista.bind("<Double-Button-1>", duplo_clique)
    
    consulta.mainloop()

bot_Consultar = Button(janela, text="   Consultar   ", width=8, height=2, font="Arial, 9") 
bot_Consultar.place(x=320, y=550) 
bot_Consultar.bind("<Button-1>", consultar)

janela.geometry("500x600+400+70") 

janela.title("FoPag") 

janela.resizable(True, True)

janela.overrideredirect(False)

janela.mainloop()