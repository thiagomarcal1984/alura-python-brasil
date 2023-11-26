from TelefonesBr import TelefonesBr
import re

padrao_molde = "(xx) aaaa-wwww"
padrao = "\(?\d{2}\)?\s*\d{4,5}\s*-?\s*\d{4}"
texto = "Meus telefones são 3199959-1984 e (31) 3069 - 3241"
reposta = re.findall(padrao, texto)
# Resposta: ['3199959-1984', '(31) 3069 - 3241']
print(reposta) 

telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto.numero)
# Resposta: "552126481234"
