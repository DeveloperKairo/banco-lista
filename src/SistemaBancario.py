from .BancoLista import BancoLista

class SistemaBancario:
    def __init__(self):
        self.bancos = []

    def criar_banco(self, nome, codigo):
        banco = BancoLista(nome, codigo)
        self.bancos.append(banco)
        return banco

    def listar_bancos(self):
        if not self.bancos:
            print("Nenhum banco cadastrado.")
            return

        print("\n=== BANCOS CADASTRADOS ===")
        for b in self.bancos:
            print(f"{b.codigo} - {b.nome}")
        print("============================\n")

    def buscar_banco(self, codigo):
        for b in self.bancos:
            if b.codigo == codigo:
                return b
        return None
