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



























































import tkinter as tk
import pyjokes
from deep_translator import GoogleTranslator

def gerar_piada():
    try:
        # 1. Pega a piada em inglês
        piada_en = pyjokes.get_joke()
        
        # 2. Traduz para Português
        traducao = GoogleTranslator(source='en', target='pt').translate(piada_en)
        
        # 3. Atualiza o Label no Tkinter
        label_piada.config(text=traducao)
    except Exception as e:
        label_piada.config(text="Erro de conexão (Internet necessária)")

# Configuração Básica Tkinter
root = tk.Tk()
root.geometry("400x300")

label_piada = tk.Label(root, text="Clique para traduzir uma piada", wraplength=350, font=("Arial", 12))
label_piada.pack(pady=50)

btn = tk.Button(root, text="Nova Piada", command=gerar_piada)
btn.pack()

root.mainloop()










## 2. Usando o objeto de fonte (Recomendado)
Se você criou um objeto minha_fonte para padronizar o app, basta passá-lo para o botão. Assim, se você mudar o tamanho na variável, todos os botões mudam juntos:

import tkinter as tkfrom tkinter import font
root = tk.Tk()
# Define a fonte uma única vezfonte_botao = font.Font(family="Verdana", size=12, weight="bold")
# Aplica a mesma variável em vários botõesbtn1 = tk.Button(root, text="Confirmar", font=fonte_botao)btn2 = tk.Button(root, text="Cancelar", font=fonte_botao)

btn1.pack(side="left", padx=10)
btn2.pack(side="left", padx=10)

root.mainloop()

## Por que meu botão não mudou de cor ou estilo?
No Windows, o botão padrão do Tkinter às vezes ignora certas estilizações (como bordas ou cores de fundo muito específicas) para manter o visual do sistema operacional. No entanto, a fonte (tamanho e tipo) sempre deve funcionar.
Dica Extra: Se você quiser que o texto do botão fique colorido junto com a fonte, adicione o argumento fg (foreground):

tk.Button(root, text="Colorido", font=fonte_botao, fg="blue")

Você gostaria de ver como mudar a cor de fundo do botão quando o mouse passa por cima dele?



from tkinter import font

# Criando um objeto de fonte reutilizável
minha_fonte = font.Font(family="Arial", size=12, weight="bold")

label1 = tk.Label(root, text="Texto 1", font=minha_fonte)
label2 = tk.Label(root, text="Texto 2", font=minha_fonte)
