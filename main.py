from TelefonesBr import TelefonesBr
import re

padrao_molde = "(xx) aaaa-wwww"
padrao = "\(?\d{2}\)?\s*\d{4,5}\s*-?\s*\d{4}"
texto = "Meus telefones são +55 31 99959-1984 e (31) 3069 - 3241"
reposta = re.findall(padrao, texto)
# Resposta: ['3199959-1984', '(31) 3069 - 3241']
print(reposta)
print()

texto = texto.join([" 552126481234"])

# Crie grupos para separar componentes da RegEx
pais = "(\+?\d{1,3})?" # Repare na interrogação: torna o grupo opcional.
area = "(\d{2}|\(\d{2}\))?" # Repare na interrogação: torna o grupo opcional.
prefixo = "(\d{4,5})"
sufixo = "(\d{4})"
# padrao = "(\d{3}\)(\d{2}\)\s*(\d{4,5})\s*-?\s*(\d{4})"
# padrao = f"{pais}\s*{area}\s*{prefixo}\s*-?\s*{sufixo}"
padrao = "".join([
    pais, 
    '\s*', # Espaços opcionais 
    area, 
    '\s*', # Espaços opcionais 
    prefixo, 
    '\s*-?\s*', # Espaços e traços opcionais
    sufixo,
])
# Retorna uma lista de tuplas.
# Cada tupla contém os 4 grupos: pais, area, prefixo e sufixo.
resposta = re.findall(padrao, texto)
print("Lista de tuplas dos grupos: \n", resposta)
print()

# Retorna um objeto Match onde foi encontrado o padrão.
resposta = re.search(padrao, texto)
print("Match:\n", resposta)
#  <re.Match object; span=(0, 12), match=' 55212648123'>
print()

# Retorna o grupo que se busca por parâmetro:
texto = '+55   31   99959-1984'
print(
    "Cada grupo do match: \n",
    re.search(padrao, texto).group(1), # País.
    re.search(padrao, texto).group(2), # Área.
    re.search(padrao, texto).group(3), # Prefixo.
    re.search(padrao, texto).group(4), # Sufixo.
)
#  +55 31 99959 1984
print()

print(
    "String com o match inteiro: \n",
    re.search(padrao, texto).group()  # O match inteiro.
)
#  +55   31   99959-1984 # Repare nos espaços a mais.

telefone = TelefonesBr(texto)

print("Objeto TelefonesBr: \n", telefone)
#  +55 (31) 99959-1984
