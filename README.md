# Validando um CPF
Classe Cpf:
```python
class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def cpf_eh_valido(self, documento):
        return len(documento) == 11

    def format_cpf(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]

        return f"{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}"

    def __str__(self):
        return self.format_cpf()
```

Invocando a classe no arquivo `main.py`:
```python
from Cpf import Cpf

cpf = "15616987913"
objeto_cpf = Cpf(cpf)

print(objeto_cpf)
```
# Pacotes Python
O PyPI tem o pacote `validate-docbr`, que cuida da validação de dados no padrão brasileiro (CPF, telefone etc.).

Mudança no arquivo `main.py`, para usar a validação do pacote `validate-docbr`:
```python
from validate_docbr import CPF

cpf =  CPF()

print(cpf.validate("01234567890")) # Retorna True
```
# Utilizando um pacote
Novo código da classe Cpf:
```python
from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError('Quantidade de dígitos inválida.')

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()
```
Usando a classe no arquivo `main.py`:
```python
from Cpf import Cpf

cpf_um =  Cpf("15316264754")

print(cpf_um) # Retorna 153.162.647-54, com os separadores.
```
# Validando CNPJ
Mudanças do código do arquivo `Cpf.py`, que foi renomeado para `cpf_cnpj.py`:
```python
from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento == 'cpf':
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido")
        elif self.tipo_documento == 'cnpj':
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido")
        else:
            raise ValueError('Documento inválido')

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida.')

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.format_cpf()
        return self.format_cnpj()

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError('Quantidade de dígitos inválida.')
```

Uso da nova clase no arquivo `main.py`:
```python
from cpf_cnpj import CpfCnpj

# cpf_um =  Cpf("15316264754")
# print(cpf_um)

exemplo_cnpj = '35379838000112'
documento = CpfCnpj(exemplo_cnpj, 'cnpj')

print(documento)
```
# Máscara para CNPJ
Na aula anterior não foi proposta uma mudança no método `__str__`. Desta vez a mudança no código foi proposta:

```python
from validate_docbr import CPF, CNPJ
class CpfCnpj:
    # Resto do código
    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.format_cpf()
        elif self.tipo_documento == 'cnpj':
            return self.format_cnpj()
    # Resto do código
```
Usando a classe modificada no arquivo `main.py`:
```python
from cpf_cnpj import CpfCnpj

exemplo_cnpj = '35379838000112'
documento = CpfCnpj(exemplo_cnpj, 'cnpj')
print(documento)

exemplo_cpf = '32007832062'
documento = CpfCnpj(exemplo_cpf, 'cpf')
print(documento)
```
# Refatorando o código
O arquivo `cpf_cnpj.py` vai conter uma fábrica de documentos (CPF, CNPJ etc.):
```python
from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de dígitos está incorreta.')

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido.')

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido.')

    def __str__(self):
        return self.format()

    def valida(self, documento):
        mascara = CNPJ()
        return mascara.validate(documento)
    
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
```
Invocando as novas classes:
```python
from cpf_cnpj import Documento

exemplo_cnpj = '35379838000112'
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

exemplo_cpf = '32007832062'
documento = Documento.cria_documento(exemplo_cpf)
print(documento)
```
# Resumo Regex
Mudanças no arquivo `main.py` para exemplificar expressões regulares:
```python
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
# Retorna "rodrigo123@gmail.com.br"
print(resposta.group())
```

# Definindo padrão para Telefones
Classe para validação de telefone:
```python
import re

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto.")

    def valida_telefone(self, telefone):
        # Padrão:   2 ou 3 dígitos para o país;
        #           2 dígitos para o código de área;
        #           4 ou 5 dígitos para o prefixo;
        #           4 dígitos para o sufixo.
        padrao = "\d{2,3}\d{2}\d{4,5}\d{4}"
        resposta= re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False
```
Uso da classe no arquivo `main.py`:
```python
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
```
# Criando Máscara para o numero de telefone
Arquivo `main.py`:
```python
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
```

Arquivo `TelefonesBr.py`:
```python
import re

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto.")

    def valida_telefone(self, telefone):
        # Crie grupos para separar componentes da RegEx
        pais = "(\+?\d{1,3})?" # Repare na interrogação: torna o grupo opcional.
        area = "(\d{2}|\(\d{2}\))?" # Repare na interrogação: torna o grupo opcional.
        prefixo = "(\d{4,5})"
        sufixo = "(\d{4})"

        padrao = "".join([
            pais, 
            '\s*', # Espaços opcionais 
            area, 
            '\s*', # Espaços opcionais 
            prefixo, 
            '\s*-?\s*', # Espaços e traços opcionais
            sufixo,
        ])
        resposta= re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "(\+?\d{1,3})?\s*(\d{2})\s*(\d{4,5})\s*-?\s*(\d{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = "{} {} {}-{}".format(
            resposta.group(1) if resposta.group(1) else '55', 
            f"({resposta.group(2)})" if resposta.group(2) else '',
            resposta.group(3), 
            resposta.group(4)
        )
        return numero_formatado

    def __str__(self):
        return self.format_numero()
```
# Datas no Python
Classe `DatasBr`:
```python
from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            'janeiro',
            'fevereiro',
            'março',
            'abril',
            'maio',
            'junho',
            'julho',
            'agosto',
            'setembro',
            'outubro',
            'novembro',
            'dezembro',
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = [
            'segunda',
            'terça',
            'quarta',
            'quinta',
            'sexta',
            'sábado',
            'domingo',
        ]
        # Em Python, a weekday começa de zero, segunda-feira.
        dia_semana =  self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]
```

Chamando a classe no arquivo `main.py`:
```python
from datas_br import DatasBr

cadastro = DatasBr()
print('Dia do cadastro:', cadastro.momento_cadastro)
print('Mês do cadastro:', cadastro.mes_cadastro())
print('Dia da semana do cadastro:', cadastro.dia_semana())
```
# Formatando Datas
Mudanças na classe DatasBr para inserir a formatação da data/hora para o padrão brasileiro:
```python
from datetime import datetime

class DatasBr:
    # Resto do código.
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada

    def __str__(self):
        return self.format_data()

```
Uso da classe `DatasBr` no arquivo `main.py`:
```python
from datas_br import DatasBr

cadastro = DatasBr()
# Resto do código

print('Dia formatado no padrão brasileiro:', cadastro.format_data())
# Dia formatado no padrão brasileiro: 26/11/2023 19:55
```
# Diferença entre datas e timedelta
A classe `timedelta` implementa os métodos especiais `__add__` e `__sub__`, que permitem somar e subtrair intervalos de tempo.

Classe `DatasBr` modificada:
```python
from datetime import datetime, timedelta

class DatasBr:
    # Resto do código
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro 
        # Momento cadastro é igual a hoje, na prática.
        # Resultado: 30 days, 0:00:00
        return tempo_cadastro
```
Uso da classe no arquivo `main.py`
```python
from datas_br import DatasBr

hoje = DatasBr()

print(hoje.tempo_cadastro())
```
# Introducao APIs e validação de CEP
Classe de busca de CEP:
```python
class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido.")

    def cep_e_valido(self, cep):
        return len(cep) == 8

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
    
    def __str__(self):
        return self.format_cep()
```

Uso da classe no arquivo `main.py`:
```python
from acesso_cep import BuscaEndereco

cep = 25870145
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
```
