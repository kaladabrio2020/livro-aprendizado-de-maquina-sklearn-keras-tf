# Capítulo 1 - Cenário do Aprendizado de Máquina

Primeiro Algoritmo de Aprendizado de Máquina que se popularizou na década de 1999 , o foi *filtro de Spam* 

## 1.1 - O que é aprendizado de máquina?

* "Aprendizado de máquina é o campo de estudo que possibilita aos computadores a habilidade de de aprender sem explicitamente programa-los" , Arthur Samuel ,1959

## 1.2 - Por que usar Aprendizado de Máquina ?

```mermaid
graph LR;
    a(Estudar o Problema) ---> b(Escrever as regras) ;
    b                     ---> c((Avaliar));
    c                     ---> d([Analisar os erros]) ---> a;
    c                     ---> e[Disponibilizar];
```

##### **Desenvolvendo um filtro de spam nua abordagem tradicional**

1. Identificar as carecteristicas do spam, observando os padrões 

2. Escrever um algoritmo de detecção de spam para cada um dos padrões observados

3. Repertir o passos 1 e 2 até obter um bom desempenho

**Contras** :

* Se o problema for muito complexo o algoritmo também se tornará complexo, além disso tornando a manutenção do mesmo custosa e nada fácil

```mermaid
graph TD;
    a(Estudar o Problema) ---> b(Treinar o algoritmo de AM) ;
    b                     ---> c([Avaliar a solução]);
    c                     ---> d([Analisar os erros]) ---> a;
    c                     ---> e[[Disponibilizar]];
```

##### Nua abordagem do aprendizado de máquina

1. Um filtro de spam baseado em técnicas de aprendizado de máquina aprende automaticamente quais são os padrões e bom indicadores de spam 

**Vantagem a abordagem tradicional** : 

* Programe bem menor 
* Fácil manutenção
* Adaptabilidade de ambientes : sistema de aprendizado de maquina podem se adaptar a novos dados

## 1.3 - Tipos de Aprendizado de Máquina

* Serem ou não treinado com supervisão visão humana

* Se podem ou não aprender gradativamente em tempo real

* Se funcionam simplesmente comparando novos pontos de dados com dados conhecidos, ou se detectam padrões em dados de treinamento

### Aprendizado Supervisionado

O conjunto de treinamento que você fornece ao algoritmo inclui as soluções desejadas , chamadas de rotulos

* **Classificação**

* **Regressão**
  
  * Prever valor numéricos alvo [**target**], dado um conjunto de caracteristicas [**features**]

> São informações em um conjunto de dados que têm rótulos ou categorias associadas a eles. Cada instância ou amostra de dados em um conjunto rotulado é acompanhada por uma etiqueta ou categoria que descreve ou classifica essa amostra.

### Aprendizado Não Supervisionado

Os dados da treinamento não são rotulados,os sistema tenta aprender sem um professor

* **Clusterização** 
  
  * é uma técnica em que o algoritmo tenta dividir o conjunto de dados em grupos ou clusters, com base em características similares

* **Detecção de anomalias ou novidades**

* **Visualização** 

* **redução de dimensionalidade**
  
  * É simplificar os dados sem perder muita informação. Para tal,voce pode fazer um merge de diversas características correlacionadas em uma

* **Aprendizado de regras por associação**
  
  * É descobrir relações interessante entre atributos
  
  * Este tipo de aprendizado visa encontrar padrões que indicam relações entre variáveis no conjunto de dados.

> São conjuntos de informações em que as amostras não possuem categorias, etiquetas ou rótulos associados a elas. Esses dados consistem em observações brutas ou não classificadas, não sendo explicitamente categorizados ou identificados.

### Aprendizado semissupervisionado

São combinações de aprendizado supervisionado e não supervisionado

### Aprendizado por esforço

O sistema de aprendizado ,chamado de agente nesse contexto , pode assistir , selecionar e executar ações e obter recompensas em troca. Ele deve aprender sozinho qual e melhor estrategia (politica) para obter maior recompensas ao longo do tempo.

### Aprendizado em bach(por ciclo)

O sistema e capaz de aprender de forma incremental : deve ser treinado com todos dos dados disponíveis. O sistema e treinado , depois colocado em produção e roda sem aprender mais nada, só o  que aprendeu.

**Contras** :

* Se o for atualizar o sistema e preciso usar os dados novos e antigos para treina-los e disponibilizar, com isso pode ser computacionalmente caro se do dados forem grandes para cada atualização

### Aprendizado Online(incremental)

É possivel treinar o sistema incrementalmente , fornecendo as instancia de forma sequancial ,individual ou em pequenos grupos 

### Aprendizado baseado em instancia

O sistema aprende os exemplos por meio da memorização e depois generaliza em novos casos , ao empregar ma medida de similaridade a fim de compara-lo aos outros exemplos aprendidos 

### Aprendizado baseado em modelo

Enfatiza a utilização de casos específicos (exemplos) como base para fazer previsões. Os casos são compostos por instâncias (entradas) e as ações ou decisões associadas a essas instâncias. O sistema aprende a adaptar as decisões com base nos casos históricos.

## Principais desafios do aprendizado de máquina

### Sobreajuste(Overfiting)

Significa que o modelo funciona bem nos dados de treinamento , mas não generaliza tão bem

* Acontece quando o modelo é muito complexo em relação á quantidade e ao ruído dos dados de treinamento , soluções:
  
  1. Simplificar o modelo ao selecionar um com menos parametros, reduzindo o número de atributos nos dados de treinamento ou retringindo o modelo
  
  2. Coletar mais dados de treinamento
  
  3. Reduzir o Ruído nos dados de treinamento(remover outliers e corrigir error de outliers)

&nbsp;

&nbsp;

-------------------

# Capítulo 2 - Projeto de Aprendizado de Máquina Ponta a Ponta

## 2.1 - Checklist do Projeto :

1. Abordar o problema e analisar o panorama em geral

2. Obter os dados

3. Explorar os dados 

4. Preparar os dados para expor melhor os padrões de dados subjacentes aos algoritmos de aprendizado de máquina

5. Explorar muitos modelos diferentes e os combinar com a melhor solução

6. Apresentar sua solução

7. Implementar , monitoriar e fazer manutenção

## 2.2 - Pipeline :

A seguencia de compenentes de processamentos de dados se chama pipeline de dados. 

## 2.3 - Medida de desempenho :

* **Erro quadrático médio :** Calcula a média dos quadrados das diferenças entre as previsões e os valores reais.
  
  * $\large RMSE(X,h) = \sqrt{\frac{1}{m} \sum^{m}_{i=1}{(h(x^{(i)}) - y^{(i)})}} $
    
    * **Pros**
      * Penaliza erros grandes mais fortemente 
      * Penaliza valores distante da média
    * **Contras**
      * Menos intuitivo, os valores estão ao quadrado, o que pode torná-lo mais sensível a outliers extremos.

* **Erro Absoluto médio :** Calcula a média das diferenças absolutas entre as previsões e os valores reais.
  
  * $\large MAE(X,h) = \frac{1}{m} \cdot \sum^{m}_{i=1} | (h(x^{(i)}) - y^{(i)})|$
    
    * **Pros**
      * Fácil interpretação, trata todos os erros de forma igual.
    * **Contras** 
      * Não tem penalidade 

* **R2** : . Quanto mais próximo o R2 estiver de 1, melhor o modelo está em explicar a variabilidade nos dados. Se R2 for próximo de 0, o modelo não está explicando bem a variabilidade nos dados.
  
  * $\large R2(pred,ytrue) = 1-\frac{\sum^{m}_{i=1}({ytrue^{i} - pred^{i})^{2}}}{ {\sum^{m}_{i=1}} ({ytrue^{i} - ytrue_{mean})^{2}} }$

## 2.3 - Tipos de atributos

<img title="" src="img/Atributos.png" alt="" width="464" data-align="center">

- **Atributo categórico binário**: é aquele que assumi apenas dois valores, e podem ser *também númericos*
  
  - ex : atributo "gender"" possui dois valores únicos = ['female' , ' male'].

- **Atributo categórico Nominal** : é aquele cujos valores possuem símbolos ou rótulos distintos.
  
  - Por exemplo: o atributo “estado civil” pode assumir os valores [“solteiro”,“casado”, “separado”, “divorciado”,“viúvo”].

- **Atributo categórico ordinal :** é aquele que permite ordenar suas categorias, embora não necessariamente haja uma noção explicita de distância entre as categorias
  
  - Por exemplo: o atributo “nível educacional” pode assumir
    os valores [“primário”, “secundário”, “graduação”,“especialização”,“mes trado”,“doutorado”]

- **Atributo numérico de razão(Intervalar)** : Elas têm os mesmos atributos das variáveis contínuas, mas possuem uma escala definida, onde as diferenças entre os valores são interpretáveis e significativas.

- **Atributo Numérico Discreto :** Elas assumem valores específicos e separados, e não podem ter valores intermediários entre esses valores.(geralmente são inteiros)
  
  - Número de filhos em uma família (1, 2, 3...)

## 2.3 - Tail Heavy:

Na analise dados , com histograma podemos vizualizar que certo atributos podem ter uma tail-heavy, as vezes se faz necessario passar para um distribuiçao normal

* Logaritmica

* Raiz Quadrada

* Box-cox
  
  * ```python
    from scipy.stats import boxcox
    ```

## 2.4 - Conjunto de test

#### Amostragem estratificada

* Supondo que Eua e formado por 51% de mulheres e 49% de homens , uma pesquisa e feita e mantem essa proporção na amostragem, **amostragem estratificada** a população e dividida em subgrupos homogeneos, chamados de estratos, e recolhe-se a amostra do numero certo de instancia de cada estrato, afim de garantir que o conjunto de test represente população como um todo.

## 2.5 - Prepare os dados para o algoritmos de Machine Learning

Em vez de preparar tudo manualmente , voce dever escrever funções 

1. Reutilizavel

&nbsp;

&nbsp;

---------------------------

# Capítulo 4 - Treinando Modelos

## Regressão Linear

<img title="" src="img/plot.png" alt="" width="371" data-align="center">

Modelo linear faz   um predição simplesmente calculando uma soma ponderada das caracteristicas de entrada

* $\large ŷ$...: Valor previsto

* $\large n$...: Número das caractiricas

* $X_i$.: É o valor da i-ésima das caracteríticas

* $\theta_j$..: É o j-ésimo parametro do modelo
  
  * $\theta_0$ = **interceptor** (intercept_)
  
  * $\theta_{i>0}$ = peso das caracterisitcas (**coeficiente(coef_)**)

$$
\large \^{y} = \theta_0(x_0) + \theta_1x_1 + .... + \theta_nx_n \\x_0 = 1 
$$

#### Predição do modelo linear(vetorizada)

$$
\large ŷ = h(x) = \theta \cdot x
$$

#### Equação Normal

$$
\large \^{\theta} = (X^T X)^{-1} X^T y
$$

$\large \^{\theta}$...: é o valor de $\theta$ que minimiza a função de custo.

```python
class RegressaoLinear():

    def fit(self,X:np.array,y:np.array):
        X     = np.c_[np.ones((np.size(X),1)),X]

        theta = (np.linalg.inv(X.T.dot(X)).dot(X.T)).dot(y)

        self.theta = theta

    def predict(self,X):
        X = np.c_[np.ones((np.size(X))),X]
        return X.dot(self.theta)
```

##### Prevendo

```python
X = 2 * np.random.rand(100,1)
y = 4*X +np.random.randn(100,1)

xtest = np.array([[0],[2]])

reg  = RegressaoLinear()
reg.fit(X,y)
pred = reg.predict(xtest)
```

#### Complexidade computacional

* Se aumenta o número de caracteristicas $X_{n*m}$ fica complexidade de $O(n^{2.4})$  a $O(n^3)$

* No Sklearn **`RegressionLinear`** é $O(n^2)$ em relação ao numero de caracteristicas

* Se ambas lidam bem com um grande número de instancias $O(m)$

> Se tiver o dobro de instancia levarar o dobro de caracteristicas, mas lida bem com grande númedo de instancias

### Gradiente descendente

É um algoritmo de otimização genérico que consegue identificar ótimas soluções para um leque amplo de problemas.

* $min : f(x)$ O objetivo  e  minimizar a função de custo , a função para um modelo linear e convexa ou seja só tem um minimo global.

* Calcula o gradiente local da função de error em relação ao vetor de parametro $\theta$ $\nabla f(x)$ e segue em direção ao gradiente descendente

* $\theta$ e inicializado com valores aleatorios

Um parametro importante para o gradiente descendente é o tamanho as etapas , determinado pelo hiperparameto taxa de aprendizado $eta$ 

* Se for muito pequeno o algoritmo terá mais iterações para convergir , levando assim muito tempo

* Se for muito alto o algoritmo talvez nunca encontre uma boa solução

> E bom as caracteristicas estarem e uma escala semelhante 
> 
> * Normalizacao =**`MinMaxScaler`**
> 
> * Padronização = **`StandardScaler`**

* **OBS** : Quanto mais parametro um modelo tem (caracteristicas) mais dimensões esse espaço tem e fica mais dificil a pesquisa

### Gradiente decendente em bach (em lote)

Para calcular o gradiente da função de custo em relação ao parametro do modelo $\theta$ 

#### Derivada parciais da função de custo

$$
\nabla MSE(\theta) = \frac{2}{m} \cdot \sum^{m}_{i=1}(\theta^{T} x^i - y^i)x^i_j
$$

#### Vetor gradiente da função de custo

$$
\nabla_{\theta} MSE(\theta) = \frac{2}{m} \cdot X^T (X\cdot\theta - y)
$$

* A formula envolve cálculos sobre o conjunto de treinamento completo $\large X$ a cada etapa do gradiente descendente.

* Por isso se chama gradiente descendente em lote possui usa todos dos dados de treimanento a cada etapa

* **Gradiente descendente em lote** e  mutio lento se o conjunto de treinamento for muito grande , contudo ele se sai muito melhor em relação a regressão linear normal ou SVD

#### Etapa do gradiente Descente

$$
\theta_{iter} = \theta - \eta \cdot \nabla MSE(\theta)
$$

```python
class GradienteLote:
    def __init__(self,theta = np.random.randn(2,1), eta = 0.1 , maxiter = 1_000):
        self.theta   = theta
        self.eta     = eta 
        self.maxiter = maxiter


    def condition(self,vetor):
        if ( np.any(np.isinf(vetor))   ):return True 
        if ( np.any(np.isnan(vetor))   ):return True
        if ( np.any(np.isneginf(vetor))):return True
        return False

    def fit(self,X:np.array,y=None):
        m =  np.size(X)
        X =  np.c_[np.ones((m,1)),X]

        for iter in range(self.maxiter):
            vetorGradiente = X.T.dot(X.dot(self.theta) - y)
            vetorGradiente = 1/m * vetorGradiente

            if self.condition(vetorGradiente):
                break

            self.theta = self.theta - self.eta * vetorGradiente

            if self.condition(self.theta):
                break
        return self.theta
    def predict(self,X):
        X = np.c_[np.ones(np.size(X)),X]
        return X.dot(self.theta)
```

* Encontrar um boa taxa de aprendizado usano o **`GridSearch`** mas deve limitar o número de iterações

### Gradiente Descendente Estocástico

Totalmente diferente do gradiente descendente em lote que usa todo o conjunto de treinamento para calcular o gradiente a cada etapa(deixando lento para conjunto de treinamento grandes) , estocástico seleciona no conjunto de treinamentos pequenas instancias de forma aleatória a cada etapa.

* Bem poucos dados para manipular a cada manipulação

* Pega instancias unicas de maneira aleatoria para calcular o gradiente

* Devido a natureza aleatoria o algoritmo e muito menos regular que o gradiente descendente em lote , ou seja , tem mais etapas até alcançãr o minimo .

* Tem mais chances de encontrar o minimo global

```python
class GradientStocastic:
    def __init__(self,t0 = 5, t1 = 50, n_epochs=50 ,theta = np.random.randn(2,1)):
        self.t0 = t0
        self.t1 = t1
        self.n_epochs = n_epochs
        self.theta    = theta

    def condition(self,vetor):
        if ( np.any(np.isinf(vetor))   ):return True 
        if ( np.any(np.isnan(vetor))   ):return True
        if ( np.any(np.isneginf(vetor))):return True
        return False

    def learning_rate(self,t):
        return self.t0 / (t+self.t1)

    def fit(self,X,y=None):
        m = np.size(X)
        X = np.c_[np.ones((m,1)),X]

        for epoch in range(self.n_epochs):
            for i in range(m):
                randomIndex = np.random.randint(m)
                xi = X[randomIndex:randomIndex+1]
                yi = y[randomIndex:randomIndex+1]

                gradient = 2 * xi.T.dot(xi.dot(self.theta)-yi)

                if (self.condition(gradient)):break

                eta        = self.learning_rate(epoch*m+i)
                self.theta = self.theta - eta * gradient

                if (self.condition(self.theta)):break

        return self.theta
    def predict(self,X):
        X = np.c_[np.ones(np.size(X)),X]
        return X.dot(self.theta)
```

#### Comparando

| x              | Instancias | Caracteristica | Hiperparametro | Escalonamento Exigido | Sklearn                | out-of-core |
| -------------- | ---------- | -------------- | -------------- | --------------------- | ---------------------- | ----------- |
| Equação Normal | Rápido     | Lento          | 0              | Não                   | N/A                    | não         |
| Svd            | Rápido     | Lento          | 0              | Não                   | **`LinearRegression`** | não         |
| GD Batch       | Lento      | Rápido         | 2              | sim                   | **`SGBRegressor`**     | não         |
| Estocático     | Rápido     | Rápido         | $\geq 2$       | sim                   | **`SGBRegressor`**     | sim         |
| Mini-Batch     | Rápido     | Rápido         | $\geq 2$       | sim                   | **`SGBRegressor`**     | sim         |

```python
from sklearn.linear_model import SGDRegressor
# Batch
batch = SGDRegressor(penalty=None,alpha=0.1,max_iter=1000,learning_rate='constant')

# Estocástico
stocastic = SGDRegressor(penalty=None,alpha=0.1,max_iter=1000,learning_rate='adaptive') 
```

## Regressão Polinomial

<img title="" src="img/polinomio.png" alt="" width="410" data-align="center">

Se os dados forem mais complexo de um linha reta , pode usar um modelo não linear para ajusta dados não lineares. Adicionando potencia de cada caracterista como novas caracteristicas e depois treinar um modelo linear nesse conjunto dilatado de caracteristicas. Essa tecnica se chama regressão polinomial.

----------**1.input**

```python
from sklearn.preprocessing import PolynomialFeatures

poly  = PolynomialFeatures(degree=2,include_bias=False)
xpoly = poly.fit_transform(X)


print(xpoly[0],X[0],X[0]**2)
```

---------**output**

```bash
[-0.58572307  0.34307152] [-0.58572307] [0.34307152]
```

----------**2.input**

```python
from sklearn.linear_model import LinearRegression

linReg = LinearRegression()
linReg.fit(xpoly,y)

print(linReg.intercept_,linReg.coef_)
```

-----**output**

```bash
[-0.12324421] [[1.13392779 2.0372897 ]]
```





## Modelos Lineares Regularizados

### Regressão Ridge

$||w||_2 = \sqrt{w_1²+ w_2^2 +...+w_n^2}$

### Regressão Lasso
