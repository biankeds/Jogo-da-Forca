nome = input("Olá! Qual seu nome? \n")
print("\nOlá," , nome , "! Bem vindo(a) ao jogo da forca da Bibi, vamos começar! \n")

#Primeiramente iremos definir uma palavra para nossa variável e assim poder iniciar o jogo. A palavra escolhida foi "Morango";

palavra = "Morango".upper()

#Crei uma forca com caracteres para deixar o joguinho mais intuitivo e dinâmico;
forca = """
__________
|        |
|        |
|        -"""

#Logo em seguida eu criei variáveis para cada parte do corpo do nosso boneco;
vazio = """

"""
cabeca = """
         O
"""
corpin = """
         O
         |
"""
braco_e = """
         O
        /|
"""
braco_d = """
         O
        /|\\
"""
perna_e = """
         O
        /|\\
        /
"""
perna_d = """
         O
        /|\\
        / \\
"""

#Aqui foi criada uma lista para demonstrar os estados do corpo do boneco durante o jogo;
chances = [vazio, cabeca, corpin, braco_e, braco_d, perna_e, perna_d]

#Declarando variáveis para os acertos, erros, letras acertadas e letras erradas;
acertos = 0
erros = 0
letras_acertos = ""
letras_erros = ""

#Enquanto acertos for diferente que a quantidade total de letras nas quais compõem a palavra, ou os erros forem diferentes que 6, o if e else irão se repetir;
while acertos != len(palavra) and erros != 6: 

#Se a letra escolhida pelo usuário fazer parte da lista de acertos, printa a letra na tela. Caso o contrário, vai printar um "_";
  listinha = ""
  for letra in palavra:
    if letra in letras_acertos:
      listinha += letra
    else:
      listinha += "_ "
  print("Você já errou as seguintes letras: " + letras_erros, " \n")
  print(forca + chances[erros])
  print(listinha)
  letra = input("\nDigite uma letra: ").upper()
  
#Em seguida, vamos usar if e else para verificar se a palavra escolhida pelo usuário está ou não presente na palavra definida na variável do início do código;
  if letra in letras_acertos+letras_erros:
    print("Você já tentou essa letra.")
    continue
  if letra in palavra:
      print("\nVocê acertou a letra! :D")
      letras_acertos += letra
      acertos += palavra.count(letra) #Para contar uma letra caso ela exista mais de uma vez na palavra;
  
  else:
    print("\nVocê errou a letra! :(")
    letras_erros += letra
    erros += 1
