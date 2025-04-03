
def calcularimc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def classificarimc(imc):
    if imc < 18.5:
        return "Abaixo do peso: É recomendado procurar um médico para avaliação criteriosa do resultado." 
    elif 18.5 <= imc < 24.9:
        return "Peso normal: Tudo indica que está tudo bem, mas é importante avaliar outros parâmetros."
    elif 25 <= imc < 29.9:
        return "Sobrepeso: Sobrepeso está associado ao risco de doenças como diabetes e hipertensão"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1: É importante buscar orientação médica e nutricional para entender melhor o seu caso"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2: Indica um quadro de obesidade mais evoluído em relação à classificação anterior"
    else:
        return "Obesidade grau 3: Nesse ponto, a chance de já estarmos diante de outras doenças associadas é mais elevada"
