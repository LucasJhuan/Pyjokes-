import pyjokes as pj
import tkinter as tk
from tkinter import *
from tkinter import ttk

#lista favoritos
favoritos = []

#gera uma piada aleatória
def risada():
    global piada
    piada = pj.get_joke()
    texto.config(text=piada)
    msg.config(text='')

#favoritar a piada atual
def favoritar():
    if (piada in favoritos):
        msg.config(text='Piada ja esta favoritada')
    
    else:
        favoritos.append(piada)
        msg.config(text='Piada Favoritada')


#janela favoritados
def favoritados():
    favoritados = tk.Tk()
    favoritados.title('Piadas Favoritadas')
    favoritados.geometry('700x500')

    #texto piadas favoritas
    for i in favoritos:
        ttk.Label(favoritados, text = i, wraplength=600).pack(pady=10)
    
    ttk.Button(favoritados,text='Sair', command=favoritados.destroy).pack(pady=10)


#janela
janela = tk.Tk()
janela.title('Risada Simulator')
janela.geometry('700x500')

#texto
texto = ttk.Label(janela,text='Risada Simulator', wraplength=600)
texto.pack(pady=40)
msg = ttk.Label(janela,text='', wraplength=600)
msg.pack(pady=10)

#botões
ttk.Button(janela, text="Me faça rir!", command=risada).pack(pady=20)

ttk.Button(janela,text='Favoritar', command=favoritar).pack(pady=10)

ttk.Button(janela,text='Mostrar favoritos', command=favoritados).pack(pady=10)

ttk.Button(janela,text='Sair', command=janela.destroy).pack(pady=10)

janela.mainloop()
ttk.Button(janela,text='Favoritar', command=favoritar).pack(pady=10)

ttk.Button(janela,text='Mostrar favoritos', command=favoritados).pack(pady=10)

janela.mainloop()
