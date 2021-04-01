def saque(user, valor):
    if valor > user["saldo"]:
        raise Exception("Valor maior que seu saldo atual.")
    user["saldo"] -= valor