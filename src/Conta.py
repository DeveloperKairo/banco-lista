class Conta:
  def __init__ (self, numero, titular, saldo, tipo_conta):
    self.numero = numero
    self.titular = titular
    self.saldo = saldo
    self.tipo_conta = tipo_conta

    self.extrato = []

  def depositar(self, valor):
    self.saldo += valor
    self.extrato.append(f'Depósito: +{valor}')

  def sacar(self, valor):
    if valor < self.saldo:
      self.saldo -= valor
      self.extrato.append(f'Saque: -{valor}')
    else:
      print("Saldo insuficiente!")

  def transferir(self, valor, conta_destino):
    if valor < self.saldo:
      self.saldo -= valor
      conta_destino.saldo += valor
      self.extrato.append(f'Transferência: -{valor} para conta {conta_destino.numero}')
    else:
      print("Saldo insuficiente!")

  def consultar_saldo(self, saldo):
    print(f'Saldo da conta {self.numero}: {self.saldo}')
    