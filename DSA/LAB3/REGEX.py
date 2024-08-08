import re

musica = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!
'''

# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.
ocorrencias_1 = re.findall(r'a', musica)
contador = len(ocorrencias_1)
print(f"O caractere 'a' aparece {contador} vezes no texto.")

# 2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música.
ocorrencias_2 = re.findall(r'\btempo\b', musica, re.IGNORECASE)
contador = len(ocorrencias_2)
print(f"A palavra 'tempo' aparece {contador} vezes no texto.")

# 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.
ocorrencias_3 = re.findall(r'\b(\w+!)', musica)
print(f"Palavras seguidas por exclamação: {ocorrencias_3}")

# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor seja a palavra "amargo" em um texto.
ocorrencias_4 = re.findall(r'\besse\s+(\w+)\s+amargo\b', musica)
print(f"Palavras entre 'esse' e 'amargo': {ocorrencias_4}")

# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento.
ocorrencias_5 = re.findall(r'\b[\wÀ-ÿ]+[áéíóúãõç]', musica)
print("Partes das palavras com acentos:", ocorrencias_5)