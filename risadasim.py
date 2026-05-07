import pyjokes as pj
import tkinter as tk
import deep_translator #lembre de instalar (esse tradutor leva um tempinho pra traduzir dps q aperta o botao)
from tkinter import *
from tkinter import ttk
from tkinter import font
from deep_translator import GoogleTranslator

#lista favoritos
favoritos = []

#gera uma piada aleatória
def risada():
    global piada_en
    global traducao
    piada_en = pj.get_joke()
    traducao = GoogleTranslator(source='en', target='pt').translate(piada_en)
    texto.config(text=traducao)
    msg.config(text='')
    traducao = GoogleTranslator(source='en', target='pt').translate(piada_en)
   
#favoritar a piada atual
def favoritar():
    if (traducao in favoritos):
        msg.config(text='Piada ja esta favoritada')
    
    else:
        favoritos.append(traducao)
        msg.config(text='Piada Favoritada')

#janela favoritados
def favoritados():
    favoritados = tk.Toplevel()
    favoritados.title('Piadas Favoritadas')
    favoritados.geometry('800x600')
    favoritados.configure(bg="#F5F36D")

    #texto piadas favoritas
    for i in favoritos:
        ttk.Label(favoritados, text = i, wraplength=600).pack(pady=10)
    
    ttk.Button(favoritados,text='Sair', command=favoritados.destroy).pack(pady=10)


#janela
janela = tk.Tk()
janela.title('Risada Simulator')
janela.geometry('800x600')
janela.configure(bg="#F5F36D")

#estilização de fontes
style = ttk.Style()
style.configure("TButton", font=('Georgia', 12, 'italic'), background="#10837F", foreground="#000000")
style.configure("TLabel",font=('Georgia', 16), background="#F5F36D", foreground="#000000")

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
