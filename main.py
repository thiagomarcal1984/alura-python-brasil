import re

padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"
reposta = re.search(padrao, texto)
# Retorna 1a2 (um dígito, um caractere e outro dígito.)
print(reposta.group()) 


# Padrão de email
padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbcc rodrigo123@gmail.com.br"
resposta = re.search(padrao, texto)
print(resposta.group())
