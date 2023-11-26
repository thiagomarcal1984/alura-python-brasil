from cpf_cnpj import Documento

exemplo_cnpj = '35379838000112'
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

exemplo_cpf = '32007832062'
documento = Documento.cria_documento(exemplo_cpf)
print(documento)
