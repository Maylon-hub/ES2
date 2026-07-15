def classificar_entrega(distancia, chuva):
    risco = "baixo"
    if distancia > 50:
        risco = "medio"
    if chuva:
        risco = "alto"
    return risco