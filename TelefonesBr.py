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
    