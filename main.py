from database import users, passwords
from modules.users import register, edit
from modules.operations import saque, consulta, deposito, transferencia

def login(username):
    if username in users:
        passwd = input("Digite sua senha:\n>>> ")
        while passwd != passwords[username]:
            passwd = input("Senha errada. Tente novamente.\n>>> ")
        return True
    
    print("")
    print("Estou vendo que você é um usuário novo...")
    print("Precisamos do seu cadastro, que tal começarmos pela sua idade?")
    idade = int(input("Digite sua idade:\n>>> "))
    if idade < 16:
        faltando = 16-idade
        print(f"Oops! Você não tem a idade mínima de 16 anos.")
        print(f"Tente novamente daqui a {faltando} ano"+("s" if faltando > 1 else "")+" :)")
        return False
    
    print("")
    print("Ótimo! Agora me diga seu endereço!")
    print("Fique tranquilo, os seus dados são secretos e não são divulgados.")
    endereco = input("Digite seu endereço:\n>>> ")

    print("")
    print("Quase lá, agora crie uma senha de seis caracteres. Sinta-se livre para usar quaisquer caracteres, e capriche!")
    passwd = input("Digite sua senha:\n>>> ")
    while len(passwd) < 6:
        passwd = input("Senha com número de caracteres insuficiente. Digite uma senha com 6 caracteres ou mais:\n>>> ")
    
    print("")
    users.update({
        username: {
            "idade": idade,
            "endereco": endereco.upper(),
            "saldo": 1000
        }
    })
    passwords.update({username: passwd})
    print("Usuário criado!")
    return True

def handleOperation(option, username, info):
    print("")
    if option == 0:
        return False
    elif option == 1:
        valor = int(input("Digite o valor desejado:\n>>> "))
        saque(info, valor)
        print("Saque autorizado!")
    elif option == 2:
        valor = int(input("Digite o valor a transferir:\n>>> "))
        who = input("Digite o username do recebedor:\n>>> ")
        while who not in users:
            who = input("Usuário inexistente! Digite o username do recebedor:\n>>> ")
        transferencia(info, valor, users[who])
        print("Transferência concluída!")
    elif option == 3:
        consulta(username)
    elif option == 4:
        valor = int(input("Digite o valor a depositar:\n>>> "))
        deposito(info, valor)
        print("Depósito concluído!")

def main():
    username = input("Digite um nome de usuário:\n>>> ")
    succeeded = login(username)
    if not succeeded:
        return
    
    info = users[username]
    print(f"""
**** BANCO BLUE ****
usuário: {username}""")

    
    while True:
        option = int(input("""\nO que deseja fazer?
1. Saque
2. Transferência
3. Consulta
4. Depósito
0. Sair\n>>> """))

        try:
            if not handleOperation(option, username, info):
                break
        except Exception as e:
            print(f"    !!! Operação falhou: {e} !!!")

main()