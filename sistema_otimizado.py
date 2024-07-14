class DadosConta:
  def __init__(self):
    self.saldo = 0
    self.limite = 500
    self.numero_saques = 0
    self.LIMITE_SAQUES = 3
    self.extrato = ""

def depositar(saldo, extrato, /):
    try:
        valor = float(input("Informe o valor do depósito: "))
    except:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, limite, numero_saques, LIMITE_SAQUES, extrato):
    try:
        valor = float(input("Informe o valor do saque: "))
    except:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, limite, numero_saques, LIMITE_SAQUES, extrato

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, limite, numero_saques, LIMITE_SAQUES, extrato

def extrato(extrato,/,*,saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def menu(conta_dict):
    menu = """
    -----------MENU-----------
    Conta: """ + str(conta_dict["n_conta"]) + """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [v] Voltar

    ===> """
    
    c = conta_dict["dados"]

    while True:
        opcao = input(menu)

        if opcao == "d":
            c.saldo, c.extrato = depositar(c.saldo, c.extrato)

        elif opcao == "s":
            c.saldo,c.limite,c.numero_saques,c.LIMITE_SAQUES,c.extrato = sacar(saldo=c.saldo, 
            limite=c.limite, 
            numero_saques=c.numero_saques, 
            LIMITE_SAQUES=c.LIMITE_SAQUES, 
            extrato=c.extrato)

        elif opcao == "e":
            extrato(c.extrato, saldo=c.saldo)

        elif opcao == "v":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def mostrarUsuarios(lista_usuarios):
    if lista_usuarios:
        for usuario in lista_usuarios:
            print(f"Nome: {usuario["nome"]}")
            print(f"CPF: {usuario["cpf"]}\n")
    else:
        print("Nenhum usuário cadastrado.")

def mostrarContas(lista_contas):
    if lista_contas:
        for conta in lista_contas:
            print(f"Agencia: {conta["agencia"]}")
            print(f"Número conta: {conta["n_conta"]}")
            print(f"CPF Usuario: {conta["usuario"]}")
            print(f"Saldo: {conta["dados"].saldo}\n")
    else:
        print("Nenhuma conta cadastrada.")

def selecionarConta(lista_contas):
    cpf = input("CPF (Somente Números): ")
    n_conta = input("Número da conta (Somente Números): ")

    for conta in lista_contas:
        if conta["usuario"] == cpf:
            if conta["n_conta"] == int(n_conta):
                menu(conta)
                return
            
    print("Combinação inválica de CPF e Conta!")

def criarConta(lista_usuarios, lista_contas, AGENCIA):
    cpf = input("CPF (Somente Números): ")

    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            lista_contas.append({"agencia": AGENCIA,
                                 "n_conta": len(lista_contas)+1,
                                 "usuario": usuario["cpf"],
                                 "dados": DadosConta()})
            print("Conta criada com sucesso.")
            return
        
    print("Não existe usuário com este CPF!")

def criarUsuario(lista_usuarios):
    cpf = input("CPF (Somente Números): ")
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe usuário com este CPF!")
            return
    nome = input("Nome Completo: ")
    nascimento = input("Data de Nascimento dd/mm/aaaa: ")
    endereco = input("Endereço (Logradouro, Número - Bairro - Cidade/Estado): ")
    print("Novo Usuário Criado.")
    lista_usuarios.append({"cpf":cpf,
                           "nome":nome,
                           "nascimento":nascimento,
                           "endereco":endereco})
    
def main():
    menu = """
    -----------MENU-----------
    [nu] Novo Usuário
    [cc] Criar Conta Corrente
    [lu] Lista Usuários
    [lc] Lista Contas
    [su] Selecionar Conta

    [q] Sair
    
    ===> """
    AGENCIA = "0001"
    lista_usuarios = []
    lista_contas = []

    while True:
        opcao = input(menu)

        if opcao == "nu":
            criarUsuario(lista_usuarios)
        elif opcao == "cc":
            criarConta(lista_usuarios, lista_contas, AGENCIA)
        elif opcao == "lu":
            mostrarUsuarios(lista_usuarios)
        elif opcao == "lc":
            mostrarContas(lista_contas)
        elif opcao == "su":
            selecionarConta(lista_contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == '__main__':
    main()