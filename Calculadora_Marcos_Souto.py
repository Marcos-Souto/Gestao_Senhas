# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:16:37 2018

@author: marcos.souto
"""

import tkinter as tk
from tkinter import *
import math

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.place()
        self.grid()
        
        # Cria o label do primeiro valor
        self.lb1 = Label()
        self.lb1.configure(text="Qual o 1º valor?", font="Verdana,15", bg="white")
        self.lb1.place(x=5,y=30)
        
        #Cria a caixa de texto de input do primeiro valor
        self.txt1=Entry()  # Cria e nomeioa o objeto
        self.txt1.configure(width=10) # Configura dimenções objeto
        self.txt1.place(x=125,y=30) # configura o local do objeto
        
        # Cria o label do segundo valor
        self.lb2 = Label()  # Cria e nomeioa o objeto
        self.lb2.configure(text="Qual o 2º valor?", font="Verdana,15", bg="white") # Configura dimenções tipo de texto e cor do fundo do  objeto
        self.lb2.place(x=5,y=60) # configura o local do objeto
        
        # Cria a caixa de texto do segundo valor
        self.txt2=Entry()
        self.txt2.configure(width=10)
        self.txt2.place(x=125,y=60)
        
        # Cria o botão de soma
        self.btSoma=Button()
        self.btSoma.configure(width=7, text="Somar", font="Verdana,15",command=lambda:self.func_Soma())
        self.btSoma.place(x=305,y=30)
        
        # Cria o Botão de subtração
        self.btSubtrair=Button()
        self.btSubtrair.configure(width=7, text="Subtrair", font="Verdana,15",command=lambda:self.func_Subtrai())
        self.btSubtrair.place(x=305,y=65)
        
        # Cria o botão de multiplicação
        self.btMultiplicar=Button()
        self.btMultiplicar.configure(width=7, text="Multiplicar", font="Verdana,15",command=lambda:self.func_Multiplica())
        self.btMultiplicar.place(x=305,y=100)
        
        # cria o botão de divisão
        self.btDividir=Button()
        self.btDividir.configure(width=7, text="Dividir", font="Verdana,15",command=lambda:self.func_Divide())
        self.btDividir.place(x=305,y=135)
        
        # cria o botão de Raiz Quadrada
        self.btRaiz=Button()
        self.btRaiz.configure(width=7, text="Raiz", font="Verdana,15",command=lambda:self.func_Raiz())
        self.btRaiz.place(x=305,y=170)
        
        # cria o label de resultado
        self.lbResult = Label()
        self.lbResult.configure(text="Resultado", font="Verdana,15", bg="white")
        self.lbResult.place(x=5,y=90)
        
        #Cria label de observação
        self.lbObs = Label()
        self.lbObs.configure(text="Para calculo da Raiz será consideradoa apenas o 1º valor", font="Verdana,8", bg="white")
        self.lbObs.place(x=5,y=220)
        
#Cria as funções das operações        
    def func_Soma (self):
        try:
            soma = float(self.txt1.get()) + float(self.txt2.get())
            self.lbResult.configure(text="Resultado = " + str(soma))
        except Exception:
            self.lbResult.configure(text="Os valores digitados devem ser numericos")
            
    def func_Subtrai (self):
        try:
            subtrai = float(self.txt1.get()) - float(self.txt2.get())
            self.lbResult.configure(text="Resultado = " + str(subtrai))
        except Exception:
            self.lbResult.configure(text="Os valores digitados devem ser numericos")            

            
    def func_Multiplica (self):
        try:
            multiplica = float(self.txt1.get()) * float(self.txt2.get())
            self.lbResult.configure(text="Resultado = " + str(multiplica))
        except Exception:
            self.lbResult.configure(text="Os valores digitados devem ser numericos")
        
    def func_Divide (self):
        try:
            divide = float(self.txt1.get()) / float(self.txt2.get())
            self.lbResult.configure(text="Resultado = " + str(divide))
        except Exception:
            self.lbResult.configure(text="Os valores digitados devem ser numericos \n Não é possivel dividir por 0")

    def func_Raiz (self):
        try:
            raiz = math.sqrt(float(self.txt1.get()))  #float(self.txt2.get())
            self.lbResult.configure(text="Resultado = " + str(raiz))
        except Exception:
            self.lbResult.configure(text="Os valores digitados devem ser numericos \n ")
        
root = tk.Tk()
#Display(root)
root.title("Calculador - Marcos Souto") # titulo do frame
root.resizable(height=FALSE,width=FALSE) # não deixa maximizar e nem alterar o frame
root.geometry("420x250+200+150") # dimenciona o Frame
root.configure(background="white") # cor do fundo
# Chama o frame
app=Application(master=root)
app.mainloop()