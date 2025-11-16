# main.py

from src import SistemaBancario

sistema = SistemaBancario()

def menu_principal():
    print("""
=== SISTEMA BANCÁRIO ===
1 - Criar banco
2 - Listar bancos
3 - Entrar em um banco
0 - Sair
""")

def menu_banco(banco):
    print(f"""
=== BANCO {banco.codigo} - {banco.nome} ===
1 - Criar conta
2 - Listar contas
3 - Acessar conta
0 - Voltar
""")

def menu_conta(conta):
    print(f"""
=== CONTA {conta.numero} - {conta.titular} ===
1 - Depositar
2 - Sacar
3 - Transferir
4 - Extrato
0 - Voltar
""")

def main():
    while True:
        menu_principal()
        opc = input("Escolha: ")

        if opc == "1":
            nome = input("Nome do banco: ")
            codigo = input("Código do banco: ")
            sistema.criar_banco(nome, codigo)

        elif opc == "2":
            sistema.listar_bancos()

        elif opc == "3":
            codigo = input("Código do banco: ")
            banco = sistema.buscar_banco(codigo)

            if not banco:
                print("Banco não encontrado.")
                continue

            # Menu do banco
            while True:
                menu_banco(banco)
                op2 = input("Escolha: ")

                if op2 == "1":
                    numero = input("Número da conta: ")
                    titular = input("Titular: ")
                    saldo = float(input("Saldo inicial: "))
                    limite = float(input("Limite: "))
                    data = input("Data de abertura: ")
                    tipo = input("Tipo de conta: ")

                    banco.criar_conta(numero, titular, saldo, limite, data, tipo)

                elif op2 == "2":
                    banco.listar_contas()

                elif op2 == "3":
                    numero = input("Número da conta: ")
                    conta = banco.buscar_conta(numero)

                    if not conta:
                        print("Conta não encontrada.")
                        continue

                    # Menu da conta
                    while True:
                        menu_conta(conta)
                        op3 = input("Escolha: ")

                        if op3 == "1":
                            valor = float(input("Valor: "))
                            if conta.depositar(valor):
                                print("Depósito realizado!")
                            else:
                                print("Erro no depósito.")

                        elif op3 == "2":
                            valor = float(input("Valor: "))
                            if conta.sacar(valor):
                                print("Saque realizado!")
                            else:
                                print("Saldo insuficiente.")

                        elif op3 == "3":
                            destino = input("Conta destino: ")
                            valor = float(input("Valor: "))
                            conta_destino = banco.buscar_conta(destino)

                            if not conta_destino:
                                print("Conta destino não encontrada.")
                                continue

                            if conta.transferir(valor, conta_destino):
                                print("Transferência realizada!")
                            else:
                                print("Transferência não realizada.")

                        elif op3 == "4":
                            conta.extrato()

                        elif op3 == "0":
                            break

                elif op2 == "0":
                    break

        elif opc == "0":
            print("Encerrando...")
            break

main()
