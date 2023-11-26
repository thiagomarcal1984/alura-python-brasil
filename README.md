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
