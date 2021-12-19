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

frame_baixo = Frame(janela, bg=cor1)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=20)

# funções scale


def escala(valor):
    r = s_red.get()
    g = s_green.get()
    b = s_blue.get()

    rgb = f'{r}, {g}, {b}'

    hexadecimal = "#%02x%02x%02x" % (r, g, b)

    #alterando a cor do fundo da tela
    tela['bg'] = hexadecimal

    # alterando a entry
    e_cor.delete(0, END)
    e_cor.insert(0, hexadecimal)



# função clicar

def onClick():
    # informar
    tkinter.messagebox.showinfo('Cor', "a cor foi copiada")

    #serve para criar botão copiar
    clip = Tk()
    clip.withdraw()
    clip.clipboard_append(e_cor.get())
    clip.destroy()
    print('copiando o cógico hex')

#  -- configurando  o frame direita ---------------

l_red = Label(frame_direita, text='Red', width=7, bg=cor1, fg='red', anchor='nw', font=('Time New Roman', 12, 'bold'))
l_red.grid(row=0, column=0)
s_red = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='red', orient=HORIZONTAL)
s_red.grid(row=0, column=1)

l_green = Label(frame_direita,  text='Green', width=7, bg=cor1, fg='green', anchor='nw', font=('Time New Roman', 12, 'bold'))
l_green.grid(row=1, column=0)
s_green = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='green', orient=HORIZONTAL)
s_green.grid(row=1, column=1)

l_blue = Label(frame_direita, text='Blue', width=7, bg=cor1, fg='blue', anchor='nw', font=('Time New Roman', 12, 'bold'))
l_blue.grid(row=2, column=0)
s_blue = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='blue', orient=HORIZONTAL)
s_blue.grid(row=2, column=1)

# -- configurando  o frame Baixo ---------------
l_rgb = Label(frame_baixo, text='CÒDIGO HEX:', bg=cor1, font=('Ivy', 10, 'bold'))
l_rgb.grid(row=0, column=0, padx=5)

#Entry
e_cor = Entry(frame_baixo, width=15, font=("Ivy", 10, "bold"), justify=CENTER)
e_cor.grid(row=0, column=1, padx=10)

# Button copy
b_copy = Button(frame_baixo, command=onClick, text='copy', bg=cor1, font=('Ivy', 10, 'bold'), relief=RAISED, overrelief=RIDGE)
b_copy.grid(row=0, column=2, padx=5)

#app name
l_app_nome = Label(frame_baixo, text='<Seletor de Cores', bg=cor1, font=('Ivy', 13, 'bold'))
l_app_nome.grid(row=0, column=3, padx=50)



janela.mainloop()