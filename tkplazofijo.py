#!/usr/bin/python

# Creado por: noxonsoftwares

from tkinter import *
from tkinter import ttk



class Gui:
    def __init__(self, ventana):

        self.ventana = ventana
        #ventana.geometry('350x150')

        # Titulo
        ventana.title('Ganancias Plazo Fijo')

        self.lb1 = Label(ventana,text='Monto a depositar').grid(row=0, column=0)
        self.var1 = DoubleVar()
        self.tx1 = Entry(ventana,textvariable=self.var1).grid(row=0, column=1, sticky=W+E)

        self.lb2 = Label(ventana, text='Valor TNA').grid(row=1, column=0)
        self.var2 = DoubleVar()
        self.tx2 = Entry(ventana, textvariable=self.var2).grid(row=1, column=1, sticky=W+E)

        self.lb3 = Label(ventana, text='Dias de plazo').grid(row=3, column=0)
        self.var3 = IntVar()
        self.tx3 = Entry(ventana, textvariable=self.var3).grid(row=3, column=1, sticky=W+E)

        self.bt1 = Button(ventana,text='CALCULAR', command=self.calculo).grid(row=4, column=1, sticky=W)

        self.lb4 = Label(ventana, text='Ganancias: ').grid(row=5, column=0)
        self.var4 = StringVar()
        self.lb5 = Label(ventana, text='0', textvariable=self.var4, font=('Arial Bold','14')).grid(row=5, column=1, )

        self.lb5 = Label(ventana, text='Total: ').grid(row=6, column=0)
        self.var5 = StringVar()
        self.lb6 = Label(ventana, text='0', textvariable=self.var5, font=('Arial Bold', '14')).grid(row=6, column=1)

    def calculo(self):
        monto = self.var1.get()
        tna = self.var2.get()
        dias = self.var3.get()
        calc = tna * dias / 365
        ganan = monto * calc
        total = monto + ganan
        self.var4.set(ganan)
        self.var5.set(total)

if __name__=='__main__':
    app = Tk()
    application = Gui(app)
    app.mainloop()
