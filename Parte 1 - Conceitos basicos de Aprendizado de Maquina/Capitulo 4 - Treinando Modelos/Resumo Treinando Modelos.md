---

---
----------------------------------------------------
## Regressão Linear
Complexidade computacional para regressão linear e O(n²) ou seja se eu aumentar o números de caractéristicas (**X**) o tempo de excução será de ao quadrado.
* Ex ): $X_{10} = 0(14^{2}) = 196$

## Gradiente descendente

É um algoritmo de Programação Não Linear genérico que consegue identificar ótimas soluções para um leque amplo de  problemas. A ideia geral é ajusta iterativamente os parametros com intuito de minimizar uma função  de custo( Se aproximar do minimo local ou global ). 

Parâmetro importante é o tamanho das etapas , determinado pelos hiperparâmetro da 
**Taxa de aprendizado** , ela são os passos de cada iteração do algoritmo.
*  Se taxa for muito pequena terá muitas iterações para convergir
*  Se taxa for muito alta ele pode nunca encontrar um boa solução

> **Ao usar o gradiente descendente , e importante garantir que todoas as caracteristicas tenham escala semalhante (Normalização ou Padronização)**

* Quando aumento quantidade de parâmetros em um modelo mais diminsões esse espaço tem.
	* Ou seja quanto maior for  $n$ de $X_n$ mais dimensões n


## Gradiente descendente em batch(lote)
Ele usa todo o conjunto de treinamento para fazer a predição. Como resultado ,e ele extramente lento para conjunto de treinamento muito grande.

```python
def gradiente(self,X:np.array,Y:np.array,max_iter=1_000,eta=0.1):

	m = np.size(X)

	X = np.c_[np.ones((m,1)),X]

	for iter in range(max_iter):

		grads = ( X.T.dot(X.dot(theta)-Y) )

		if np.any(np.isnan(grads)):break
		if np.any(np.isinf(grads)):break

		if np.any(np.isneginf(grads)):break

		grads = 2/m *grads

		theta = theta - eta*(grads)

		theta = np.around(theta,decimals=4)
	return theta
```

> **Observação** : $X$ precisa está normalizado ou padronizado

## Gradiente descendente estocástico
Ele seleciona uma instância aletória no conjunto de treinamento a cada etapa e calcula os gradientes com base apenas nessas instancias única.
* Mais rápido que o gradiente descendente em batch , pois ele tem bem poucos dados para manipular e calcular a cada iteração.
* Dévido a natureza aleatória (estocástica) o algoritmo e bem menos regular
* Aleatoriedade e bom para escapar de mínimos locais ideias

```python
def CronogramaDeAprendizado(t0,t1,t):

return ( t0 / (t+t1) )

  

def GradienteEscatico(X,Y,n_epochs=50,t0=5,t1=50,theta=np.array([10,3])):
	m = np.size(X)
	X = np.c_[np.ones((m,1)),X]
	for epoch in range(n_epochs):

		for i in range(m):

			randomIndex = np.random.randint(0,m)

				xi = X[randomIndex:randomIndex+1]

				yi = Y[randomIndex:randomIndex+1]

				gradients = 2* xi.T.dot(xi.dot(theta)-yi)

				if np.any( np.isnan(gradients) ,where=True):break
				if np.any( np.isinf(gradients) ,where=True):break
				if np.any( np.isneginf(gradients) ,where=True):break

				eta = CronogramaDeAprendizado(t0,t1,epoch*m+i)

				theta = theta - eta * gradients

				if np.any( np.isnan(theta) ,where=True):break
				if np.any( np.isinf(theta) ,where=True):break
				if np.any( np.isneginf(theta) ,where=True):break

		print(f'Epochs {epoch} & eta = {eta} & theta = {theta}')

	return theta
```

| Algoritmo |  M |  Suport out-of-core | n | Hiperparametros | Escalonamento Exigido | Sklearn |
| ---------| ----| ------------| -----|---|---| ---| 
| Equação Normal    | Rápido |  Não | Lento | 0 | Não | N/A |
| Gb batch          | lento  | Não  | Rápido| 2 | SIM | SDBregressor |
| BG Escotacástico  | Rápido | Sim  | Rápido | >=2 | SIM |  SDBregressor | 
| GD Mini batch     | Rápido | Sim  | Rápido | >=2 | SIM |  SDBregressor |

## Regressão Polinomial
