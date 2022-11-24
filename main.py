
from tkinter import *

mdf_cru = float(0.00187)
mdf_branco = float(0.00225)
acrilico = float(0.03)

class Calculadora:
    def __init__(self, toplevel):

        # Janela
        toplevel.title('Calculadora de Orçamentos')
        toplevel.geometry("300x200")

        # Espaçamento
        self.frame1 = Frame(toplevel)
        self.frame1.pack()

        # Box 1
        self.frame2 = Frame(toplevel)
        self.frame2.pack()

        # Box 2
        self.frame3 = Frame(toplevel)
        self.frame3.pack()

        # Operações
        self.frame4 = Frame(toplevel, pady=12)
        self.frame4.pack()

        # Resultado
        self.frame5 = Frame(toplevel)
        self.frame5.pack()

        # Botões
        self.frame6 = Frame(toplevel, pady=12)
        self.frame6.pack()

        # Cor e tamanho das letras
        Label(self.frame1, text='', fg='black',
              font=('Verdana', '10'), height=1).pack()
        fonte1 = ('Verdana', '10')

        # Botão MDF Cru
        mdf_c = Button(self.frame4, font=fonte1, text='MDF Cru', command=self.mdf_c)
        mdf_c.pack(side=LEFT)

        # Botão MDF Branco
        mdf_b = Button(self.frame4, font=fonte1, text='MDF Branco', command=self.mdf_b)
        mdf_b.pack(side=LEFT)

        # Botão Acrílico
        acr = Button(self.frame4, font=fonte1, text='Acrílico', command=self.acr)
        acr.pack(side=LEFT)

        # Botão Sair
        sair = Button(self.frame6, font=fonte1, text='Sair', command=self.sair)
        sair.pack(side=LEFT)

        # Box 1 para entrada de número
        Label(self.frame2, text='Altura: ', font=fonte1, width=8).pack(side=LEFT)
        self.valor1 = Entry(self.frame2, width=10, font=fonte1)
        self.valor1.focus_force()
        self.valor1.pack(side=LEFT)

        # Box 2 para entrada de número
        Label(self.frame3, text='Largura:', font=fonte1, width=8).pack(side=LEFT)
        self.valor2 = Entry(self.frame3, width=10, font=fonte1)
        self.valor2.pack(side=LEFT)

        # Resultado
        Label(self.frame5, text='O valor da peça é   R$', font=fonte1, width=18).pack(side=LEFT)
        self.msg = Label(self.frame5, width=6, font=fonte1)
        self.msg.pack(side=LEFT)

    def mdf_c(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 * valor2 * mdf_cru
        c = float(c)
        self.msg['text'] = '%.2f' % (c)

    def mdf_b(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 * valor2 * mdf_branco
        c = float(c)
        self.msg['text'] = '%.2f' % (c)

    def acr(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 * valor2 * acrilico
        c = float(c)
        self.msg['text'] = '%.2f' % (c)

    def sair(self):
        app.destroy()


app = Tk()
Calculadora(app)
app.mainloop()