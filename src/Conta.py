class Conta:
    def __init__(self, numero, titular, saldo, limite, data_abertura, tipo_conta):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura
        self.tipo_conta = tipo_conta

        self.historico_transacoes = []

    def registrar(self, mensagem):
        self.historico_transacoes.append(mensagem)

    def depositar(self, valor):
        self.saldo += valor
        self.registrar(f"Depósito: +{valor}")
        return True

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            return False
        self.saldo -= valor
        self.registrar(f"Saque: -{valor}")
        return True

    def transferir(self, valor, conta_destino):
        if valor > self.saldo + self.limite:
            return False

        self.saldo -= valor
        conta_destino.saldo += valor

        self.registrar(f"Transferência: -{valor} para {conta_destino.numero}")
        conta_destino.registrar(f"Transferência: +{valor} de {self.numero}")

        return True

    def consultar_saldo(self):
        print(f"Saldo: R${self.saldo:.2f}")
