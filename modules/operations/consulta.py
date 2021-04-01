from database import users

def consulta(username):
    info = users[username]
    print("")
    print(f"USUÁRIO: {username}")
    print(f"IDADE: {info['idade']}")
    print(f"ENDEREÇO: {info['endereco']}")

    exibirSaldo = input("  Exibir saldo? [s/n] ")
    if exibirSaldo in 'Ss':
        print(f"SALDO: R${info['saldo']}")