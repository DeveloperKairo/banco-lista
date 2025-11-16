from .Conta import Conta

class BancoLista:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.contas = []

    def criar_conta(self, numero, titular, saldo, limite, data_abertura, tipo_conta):
        nova_conta = Conta(numero, titular, saldo, limite, data_abertura, tipo_conta)
        self.contas.append(nova_conta)
        return nova_conta

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return

        print("\n=== CONTAS DO BANCO ===")
        for c in self.contas:
            print(c)
        print("==========================\n")

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None
