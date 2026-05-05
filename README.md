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





Para não perder o que você já programou no Codespace e levar tudo para o seu computador (jeito clássico), siga estes passos. Vamos primeiro garantir que o código saia do Codespace para o GitHub e depois do GitHub para o seu PC.
## Passo 1: Salvar o que está no Codespace para o GitHub
Dentro do terminal do seu Codespace, digite os seguintes comandos para garantir que tudo foi enviado para a nuvem:

   1. Adicionar as mudanças:
   
   git add .
   
   2. Criar a versão:
   
   git commit -m "Salvando progresso do codespace"
   
   3. Enviar ao GitHub:
   
   git push origin main
   
   (Se der erro, tente git push origin master).

------------------------------
## Passo 2: Preparar o seu Computador (Local)
Agora que seu código está seguro no site do GitHub, vamos preparar sua máquina:

   1. Instale o Python: Baixe em [python.org](https://www.python.org/). IMPORTANTE: Na instalação, marque a caixinha "Add Python to PATH".
   2. Instale o Git: Baixe e instale o [Git for Windows](https://git-scm.com/downloads).
   3. Reinicie o Terminal: Feche qualquer CMD ou PowerShell que esteja aberto e abra um novo.

------------------------------
## Passo 3: Baixar o código no seu PC
Agora vamos "clonar" o repositório para o seu disco rígido:

   1. Crie uma pasta no seu computador onde ficarão seus projetos.
   2. Dentro dessa pasta, clique com o botão direito e escolha "Git Bash Here" ou abra o terminal nela.
   3. Vá no seu repositório no site do GitHub, clique no botão verde "Code" e copie o link HTTPS.
   4. No terminal do seu PC, digite:
   
   git clone https://github.com
   
   5. Entre na pasta criada: cd SEU_REPOSITORIO

------------------------------
## Passo 4: Instalar as bibliotecas no seu PC
Lembra que o erro do pip3 aconteceu? Agora vamos instalar o pyjokes e o streamlit (ou tkinter) no seu Windows:

python -m pip install pyjokes streamlit

------------------------------
## Passo 5: Como trabalhar daqui para frente (O Ciclo)
Agora você não precisa mais do navegador para codar. Use o VS Code instalado no seu PC:

   1. Abra a pasta do projeto no VS Code local.
   2. Edite seu código.
   3. Para salvar no GitHub (Commit Clássico): Abra o terminal do VS Code e digite:
   * git add .
      * git commit -m "Fiz tal mudança"
      * git push origin main
   
## Dica de Ouro: GitHub Desktop
Se você achar os comandos de git complicados no início, baixe o [GitHub Desktop](https://desktop.github.com/). Ele mostra visualmente quais arquivos você mudou e tem botões para fazer o Commit e o Push sem você precisar digitar comandos.
Conseguiu clonar o projeto para a sua máquina? Se travar em alguma parte do Git, me avise!


