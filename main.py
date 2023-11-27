from acesso_cep import BuscaEndereco

cep = '01001000'
objeto_cep = BuscaEndereco(cep)

# Uso do objeto BuscaEndereco:
bairro, cidade, estado = objeto_cep.acessa_via_cep()
print(
    'Parâmetros separados:\n',
    'bairro:'.capitalize(), bairro, '\n',
    'cidade:'.capitalize(), cidade, '\n',
    'estado:'.capitalize(), estado, '\n',
)
