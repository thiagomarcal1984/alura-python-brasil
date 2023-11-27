import requests

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

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        # Repare que o retorno agora é uma tupla, não o JSON todo.
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf'],
        )
