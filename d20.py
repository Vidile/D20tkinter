import random
from tkinter import *
# Rápida aplicação do Tkinter

raiz = Tk()
raiz.geometry('300x400')
raiz.title('D20!!')
raiz.configure(bg='#212121')

# rola o dado


def rolar_dados(e):
    randroll = random.randint(1, 21)
    label = Label(raiz, text=str(randroll))
    label.pack()


# Botão para apertar e rolar o dado
Botão = Button(raiz, text='Jogue o Dado ')
Botão.bind('<Button-1>', rolar_dados)
Botão.pack()

raiz.mainloop()
