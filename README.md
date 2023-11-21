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
