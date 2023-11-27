from acesso_cep import BuscaEndereco

cep = '01001000'
objeto_cep = BuscaEndereco(cep)
resposta = objeto_cep.acessa_via_cep()
print(resposta.text)
