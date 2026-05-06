# Pyjokes-
Pyjokes trabalho Lucas, Thiago, Amanda GRUPO 09

Pyjokes Retorna piadas de programação.

Oq fazer

-Guardar as favoritas em uma lista/matriz.

-Botão 'Me faça rir' que muda o texto da janela.

-Botão de favoritar piadas

-Botão mostrar favoritos

Documento biblioteca tkinter
https://docs.python.org/3/library/tkinter.html


Documento biblioteca pyjokes 
https://pypi.org/project/pyjokes/

Código
(https://prod.liveshare.vsengsaas.visualstudio.com/join?17153A0BEAAE485885CAFC23A0DC9653F0F2)




from googletrans import Translator
translator = Translator()
resultado = translator.translate("Hello world", dest='pt')
print(resultado.text)


from tkinter import font

# Criando um objeto de fonte reutilizável
minha_fonte = font.Font(family="Arial", size=12, weight="bold")

label1 = tk.Label(root, text="Texto 1", font=minha_fonte)
label2 = tk.Label(root, text="Texto 2", font=minha_fonte)
