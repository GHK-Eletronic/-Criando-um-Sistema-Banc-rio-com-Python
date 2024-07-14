class Cliente:
  def __init__(self):
    self.saldo = 0
    self.limite = 500
    self.numero_saques = 0
    self.LIMITE_SAQUES = 3
    self.extrato = ""

def depositar(cliente):
    try:
        valor = float(input("Informe o valor do depósito: "))
    except:
        print("Operação falhou! O valor informado é inválido.")
        return

    if valor > 0:
        cliente.saldo += valor
        cliente.extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(cliente):
    try:
        valor = float(input("Informe o valor do saque: "))
    except:
        print("Operação falhou! O valor informado é inválido.")
        return

    if valor > cliente.saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > cliente.limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif cliente.numero_saques >= cliente.LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        cliente.saldo -= valor
        cliente.extrato += f"Saque: R$ {valor:.2f}\n"
        cliente.numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def extrato(cliente):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not cliente.extrato else cliente.extrato)
    print(f"\nSaldo: R$ {cliente.saldo:.2f}")
    print("==========================================")

def main(cliente):
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            depositar(cliente)
        elif opcao == "s":
            sacar(cliente)
        elif opcao == "e":
            extrato(cliente)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == '__main__':
    cliente = Cliente()
    main(cliente)