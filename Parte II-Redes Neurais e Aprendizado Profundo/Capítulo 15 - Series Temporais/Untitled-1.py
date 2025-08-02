# %%
import yfinance
import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
data = yfinance.download("USDBRL=X", start="2020-01-01", end="2025-07-13", interval="1d")

# %%
data = data['Close']

# %%
data.plot(figsize=(12, 6))
plt.title("USDBRL Exchange Rate")
plt.xlabel("Date")
plt.show()

# %%
data['mean'] = data['USDBRL=X'].rolling(window=50).mean()

# %%
data.plot(figsize=(12, 6))
plt.title("USDBRL Exchange Rate")
plt.xlabel("Date")
plt.show()

# %%
# verificar se a serie é estacionária
from statsmodels.tsa.stattools import adfuller
result = adfuller(data['USDBRL=X'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])
if result[1] < 0.05:
    print("A série é estacionária")
else:
    print("A série não é estacionária")

# %%
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plot_acf(data['USDBRL=X'], lags=50)
plt.title("Autocorrelação")
plt.show()

# %%
plot_pacf(data['USDBRL=X'], lags=50)
plt.show()

# %%
from statsmodels.tsa.stattools import kpss
kpss_result = kpss(data['USDBRL=X'])
print('KPSS Statistic:', kpss_result[0])
print('p-value:', kpss_result[1])

if kpss_result[1] < 0.05:
    print("A série é estacionária")
else:
    print("A série não é estacionária")

# %%
data['diff'] = data['USDBRL=X'].diff().apply(lambda x: 0 if pd.isna(x) else x)

# %%
data['diff'].plot(figsize=(12, 6))

# %% [markdown]
# ## Example 1

# %%
# timesgeneretor tensoflow
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.preprocessing import MinMaxScaler

# %%
series = data['USDBRL=X'].values

# %%
scalar = MinMaxScaler()
series = scalar.fit_transform(series.reshape(-1, 1))

# %%
train_index = int(len(series) * 0.8)


# Split the data into training and testing sets
train = series[:train_index]
test  = series[train_index:]


# Create Timeseries Generators
train_generator = TimeseriesGenerator(
    train, train, length=40, batch_size=32
)
test_generator = TimeseriesGenerator(
    test, test, length=40, batch_size=32
)

total = TimeseriesGenerator(
    series, series, length=50, batch_size=32
)

# %%
1440/40

# %%
train_index-50

# %%
model = keras.models.Sequential([
    keras.layers.SimpleRNN(50, input_shape=[None, 1], return_sequences=True),
    keras.layers.SimpleRNN(50, input_shape=[None, 1], return_sequences=True),
    keras.layers.TimeDistributed(keras.layers.Dense(1)),
])

# %%
lr = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.01, decay_steps=10000, decay_rate=0.9)


model.compile(
    loss=keras.losses.mean_squared_error,
    optimizer=keras.optimizers.Adam(learning_rate=lr, clipvalue=1,use_ema=True),
    metrics=[keras.metrics.mean_absolute_error]
)

# %%
model.fit(
    train_generator,
    epochs=20,
    callbacks=[keras.callbacks.EarlyStopping(monitor='loss', patience=3)],
    validation_data=test_generator,
)

# %%
predicoes_completas = []

# Predições no treino
janela_tempo = 40

entrada_atual = series[:janela_tempo]


for i in range(len(series)-40):
    pred = model.predict(entrada_atual.reshape(1, janela_tempo, 1), verbose=0)
    predicoes_completas.append(pred[0, 0])
    entrada_atual = np.append(entrada_atual[1:], series[i + janela_tempo])

# %%
entrada_atual = series[-janela_tempo:]

predicoes_futuro = []
for _ in range(100):
    pred = model.predict(entrada_atual.reshape(1, janela_tempo, 1), verbose=0)
    predicoes_futuro.append(pred[0, 0])
    
    entrada_atual = np.append(entrada_atual[1:], pred[0, 0])
    entrada_atual = entrada_atual[-janela_tempo:]

# %%
len(predicoes_completas), len(series)

# %%
ultimo_indice_real = len(series[40:]) - 1
indices_futuros = np.arange(ultimo_indice_real + 1, ultimo_indice_real + 1 + 100)

# %%
plt.plot(predicoes_completas, label='Predições')
plt.plot(series[40:], label='Série Original')
plt.plot(indices_futuros, predicoes_futuro, label='Previsões Futuras')
plt.legend()
plt.show()

# %% [markdown]
# ### Exemplo 2

# %%
model = keras.models.Sequential([
    keras.layers.GRU(50, input_shape=[None, 1], return_sequences=True),
    keras.layers.GRU(50, input_shape=[None, 1], return_sequences=True),
    keras.layers.TimeDistributed(keras.layers.Dense(1)),
])
model.summary()

# %%
model.compile(
    loss=keras.losses.mean_squared_error,
    optimizer=keras.optimizers.Adam(learning_rate=lr, clipvalue=1,use_ema=True),
    metrics=[keras.metrics.mean_absolute_error]
)

# %%
series_total = TimeseriesGenerator(
    series, series, length=50, batch_size=32
)

# %%
history = model.fit(
    total,
    epochs=20,
    callbacks=[keras.callbacks.EarlyStopping(monitor='loss', patience=3)],
)

# %% [markdown]
# Plotando

# %%
janela_tempo = 50

# %%
predicoes_completas = []

pred = model.predict(series_total)

# %%
plt.plot(pred[:, -1, 0], label='Predições')
plt.plot(series[50:], label='Série Original')


