from tkinter import *
import tkinter.messagebox

#cores-------------------
cor0 = '#444466'  # preto
cor1 = '#feffff'  # branco
cor2 = '#004338'

#--criando a janela -------------------

janela = Tk()
janela.geometry('530x205')
janela.configure(bg=cor1)

# -- configurando a janela ---------------

tela = Label(janela, bg=cor0, width=40, height=10, bd=1)
tela.grid(row=0, column=0)

frame_direita = Frame(janela, bg=cor1)
frame_direita.grid(row=0, column=1)

frame_baixo = Frame(janela, bg='red', width=100)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=20)


janela.mainloop()
