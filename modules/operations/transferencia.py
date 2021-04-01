def transferencia(pagador, valor, recebedor):
    if valor > pagador["saldo"]:
        raise Exception("Valor maior que seu saldo atual.")
    pagador["saldo"] -= valor
    recebedor["saldo"] += valor