import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.preprocessing import MinMaxScaler

# --- 1. GERAÇÃO DE DADOS DE EXEMPLO ---
# Para tornar o exemplo autocontido, vamos criar uma série temporal sintética.
# Ela terá uma tendência, uma sazonalidade e um pouco de ruído.
tempo = np.arange(0, 400, 1)
# Combinação de tendência (tempo * 0.1), sazonalidade (np.sin) e ruído (np.random)
serie_bruta = tempo * 0.1 + np.sin(tempo / 20) * 15 + np.random.randn(len(tempo)) * 2
serie_bruta = serie_bruta.reshape(-1, 1) # Formato necessário para o scaler

print(f"Tamanho total da série temporal gerada: {len(serie_bruta)} pontos.")

# --- 2. PRÉ-PROCESSAMENTO DOS DADOS ---
# É crucial escalar os dados para o intervalo [0, 1] para redes neurais.
scaler = MinMaxScaler(feature_range=(0, 1))
serie_escalada = scaler.fit_transform(serie_bruta)

# --- 3. DEFINIÇÃO DE PARÂMETROS E CRIAÇÃO DO GERADOR DE DADOS ---
# Parâmetros para a janela de tempo e o gerador
length = 50          # Comprimento da sequência de entrada (janela)
batch_size = 16      # Número de amostras por lote de treinamento

# O TimeseriesGenerator irá pegar os dados e criar lotes de (X, y)
# onde X é uma sequência de 'length' pontos e y é o ponto seguinte.
# Usaremos todos os dados para treinar o modelo para este exemplo.
generator = TimeseriesGenerator(serie_escalada, serie_escalada, length=length, batch_size=batch_size)

# O número de amostras que o gerador cria é len(dados) - length
print(f"O gerador criou {len(generator) * batch_size} amostras de treinamento.")

# --- 4. CONSTRUÇÃO E TREINAMENTO DO MODELO RNN ---
n_features = 1 # Estamos trabalhando com uma série univariada

modelo = Sequential([
    # Camada RNN simples com 50 neurônios. input_shape é (length, n_features).
    SimpleRNN(50, activation='relu', input_shape=(length, n_features)),
    # Camada de saída com 1 neurônio para prever o próximo valor.
    Dense(1)
])

# Compilar o modelo
modelo.compile(optimizer='adam', loss='mean_squared_error')
modelo.summary()

# Treinar o modelo
print("\nIniciando o treinamento do modelo...")
modelo.fit(generator, epochs=15, verbose=1)
print("Treinamento concluído.")

# --- 5. GERAÇÃO DAS PREDIÇÕES HISTÓRICAS ---
# Vamos usar o modelo treinado para prever sobre os mesmos dados usados no treinamento.
# Isso nos mostra o quão bem o modelo "aprendeu" os padrões dos dados.
# O resultado de model.predict terá o mesmo número de amostras do gerador.
predicoes_historicas_escaladas = modelo.predict(generator, verbose=0)

print(f"\nNúmero de predições históricas geradas: {len(predicoes_historicas_escaladas)}")

# --- 6. GERAÇÃO DAS PREDIÇÕES FUTURAS (FORECAST) ---
# Agora, vamos prever valores que o modelo nunca viu, de forma iterativa.
passos_futuros = 100
predicoes_futuras_escaladas = []

# O ponto de partida é a última janela de dados reais disponíveis.
batch_atual = serie_escalada[-length:].reshape((1, length, n_features))

print(f"Iniciando a geração de {passos_futuros} passos futuros...")
for i in range(passos_futuros):
    # Fazer a previsão com o batch atual
    predicao_atual = modelo.predict(batch_atual, verbose=0)[0]
    
    # Armazenar a previsão
    predicoes_futuras_escaladas.append(predicao_atual)
    
    # Atualizar o batch: remover o primeiro valor e adicionar a nova previsão no final
    batch_atual = np.append(batch_atual[:, 1:, :], [[predicao_atual]], axis=1)

# --- 7. REVERSÃO DA ESCALA E PREPARAÇÃO PARA O PLOT ---
# As predições estão na escala [0, 1]. Precisamos revertê-las para a escala original.
predicoes_historicas = scaler.inverse_transform(predicoes_historicas_escaladas)
predicoes_futuras = scaler.inverse_transform(predicoes_futuras_escaladas)

# --- 8. VISUALIZAÇÃO COMPLETA E MESCLADA ---
# Preparar os índices (eixo X) para um alinhamento perfeito no gráfico.

# Índices para as predições históricas. Elas começam após a primeira janela.
indices_historicos = np.arange(length, len(serie_bruta))

# Índices para as predições futuras. Elas começam após o último ponto real.
ultimo_indice_real = len(serie_bruta) - 1
indices_futuros = np.arange(ultimo_indice_real + 1, ultimo_indice_real + 1 + passos_futuros)

# Criar o gráfico
plt.figure(figsize=(18, 8))
plt.title("Análise Completa: Real vs. Predições Históricas e Futuras", fontsize=16)

# 1. Plotar a série original completa
plt.plot(tempo, serie_bruta, label='Série Original (Real)', color='royalblue', linewidth=2)

# 2. Plotar as predições históricas (ajuste do modelo)
plt.plot(indices_historicos, predicoes_historicas, label='Predições Históricas (Ajuste)', color='darkorange', linestyle='--', linewidth=2)

# 3. Plotar a previsão futura (forecast)
plt.plot(indices_futuros, predicoes_futuras, label='Previsão Futura (Forecast)', color='forestgreen', linestyle='--', linewidth=2)

# 4. Adicionar uma linha vertical para marcar o início da previsão futura
plt.axvline(x=ultimo_indice_real, color='red', linestyle=':', linewidth=2.5, label='Início da Previsão Futura')

plt.xlabel("Tempo", fontsize=12)
plt.ylabel("Valor", fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
