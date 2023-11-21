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
