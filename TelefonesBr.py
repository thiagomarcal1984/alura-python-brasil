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
