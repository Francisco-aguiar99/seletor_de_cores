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
frame_direita.grid(row=0, column=1, padx=5)

frame_baixo = Frame(janela, bg='red')
frame_baixo.grid(row=1, column=0, columnspan=2, pady=20)

# -- configurando  o frame direita ---------------

l_red = Label(frame_direita, text='Red', width=7, bg=cor1, fg='red', anchor='nw', font=('Time New Roman', 12, 'bold'))
l_red.grid(row=0, column=0)
s_red = Scale(frame_direita, from_=0, to=255, length=150, bg=cor1, fg='red', orient=HORIZONTAL)
s_red.grid(row=0, column=1)

l_green = Label(frame_direita, text='Green', width=7, bg=cor1, fg='green', anchor='nw', font=('Time New Roman', 12, 'bold'))
l_green.grid(row=1, column=0)
s_green = Scale(frame_direita, from_=0, to=255, length=150, bg=cor1, fg='green', orient=HORIZONTAL)
s_green.grid(row=1, column=1)

l_blue = Label(frame_direita, text='Blue', width=7, bg=cor1, fg='blue', anchor='nw', font=('Time New Roman', 12, 'bold'))
l_blue.grid(row=2, column=0)
s_blue = Scale(frame_direita, from_=0, to=255, length=150, bg=cor1, fg='blue', orient=HORIZONTAL)
s_blue.grid(row=2, column=1)


janela.mainloop()
