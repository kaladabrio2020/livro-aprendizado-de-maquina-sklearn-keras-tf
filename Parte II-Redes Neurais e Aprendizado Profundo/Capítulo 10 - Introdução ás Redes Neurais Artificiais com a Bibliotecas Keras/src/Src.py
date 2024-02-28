from collections import Counter

def calcular_pesos_classes(y):
    # Contar o número de amostras de cada classe
    contagem_classes = Counter(y)
    
    # Calcular o número total de amostras
    total_amostras = sum(contagem_classes.values())
    
    # Calcular a proporção de cada classe
    proporcoes_classes = {classe: total_amostras / contagem for classe, contagem in contagem_classes.items()}
    
    # Calcular os pesos das classes
    pesos_classes = {classe: total_amostras / (len(contagem_classes) * contagem) for classe, contagem in contagem_classes.items()}
    
    return pesos_classes
    