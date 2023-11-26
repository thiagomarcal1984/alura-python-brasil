from datas_br import DatasBr

cadastro = DatasBr()
print('Dia do cadastro:', cadastro.momento_cadastro)
print('Mês do cadastro:', cadastro.mes_cadastro())
print('Dia da semana do cadastro:', cadastro.dia_semana())

print('Dia formatado no padrão brasileiro:', cadastro.format_data())
