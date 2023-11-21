from cpf_cnpj import CpfCnpj

exemplo_cnpj = '35379838000112'
documento = CpfCnpj(exemplo_cnpj, 'cnpj')
print(documento)

exemplo_cpf = '32007832062'
documento = CpfCnpj(exemplo_cpf, 'cpf')
print(documento)
