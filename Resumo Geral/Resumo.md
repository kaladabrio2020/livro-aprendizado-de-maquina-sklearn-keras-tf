# Capítulo 4 : Treinando Modelo

## Regressão Linear

<img title="" src="file:///home/mateus/MEGA/Projetos/AprendendoLivroMaosaObra-SkleanKerasTensorFLow/Resumo Geral/img/plot.png" alt="" width="357" data-align="center">   Modelo linear faz predições simplesmente calculando uma soma ponderada as caracteristica de entreda ,além de uma constante chamanda **viés**(`interceptor | coefiente linear`)

#### Equação : Predição do modelo de regressão linear

$$
\^{y} = \theta_0 + \theta_1 \cdot x_1 + ....... + \theta_n \cdot x_n
$$

* $\theta_0$.......: Intercepto | coeficiente linear

* $\theta_{n \ge 1}$...: Peso das caracteristicas

* $x_{n \ge 1}$...:  Valor da n-ésima caracteristica

**Treinar um modelo de regressão linear ....** significa encontrar os parametros $\theta$ para que o modelo se ajuste melhor ao conjunto de treinamento

> Ou seja o algoritmo de regressão linear me dara intercepto e peso das caracteristica para que o modelo preditivo se ajuste ao conjunto de treinamento

#### Métricas

* **[Root Mean Squared Error]()**
  
  * $$
     \sqrt{ \frac{1}{m} \cdot \sum^{m}_{i=0}(ytrue_i - pred_i)^2}
    $$
    
    * É  a média da diferença do valor real - valor previsto elevado ao quadrado da raiz 
    
    * Penaliza erros grandes
    
    * Se tiver outliers o resultado será alto

* **[Mean Absolute Error]()**
  
  * $$
    \frac{1}{m} \sum^{m}_{i=0}|ytrue_i - pred_i|
    $$
    
    * Média dos erros
    
    * Não há penalidade

* **[R2-Coeficiente de determinação]()**
  
  * $$
    1 - \frac{\sum(ytrue - pred)^2}{\sum(ytrue - ytrue_{media})²}
    $$
    
    * Varia de $[0 , 1]$ 
    
    * Informa o qual bem o meu modelo se ajusta ao conjunto de dados

#### Equação Normal

$$
\^{\theta} = (X^T X)^{-1} X^T y
$$

Encontrando os valores de $\theta$ de forma fechada





#### Complexidade computacional

No sklearn `LinearRegression` utiliza um abordagemd e decomposição de valores singulares (S.V.D) para encontrar os parametros :

+ Para caracteristicas a complexidade é de $O(n^2)$

+ Para instancias é $O(m)$

> Não se sai bem com conjunto de dados com muitas caracteristicas , mas se sai bem se tiver muitas instancias 

Na equação normal ela varia de $O(n^{2.4})$ a $O(n³)$ 

> Não se sai bem com grande número de caracterisiticas

## Gradiente Descendente

E um algoritmo de otimização generico , que a ideial geral e encontrar o parametros de maneira iterativa com o intuito de minimizar a função de custo

* O parametros $\theta$ são preenchidos com valores aletarios

* **Taxa de aprendizados**: são os tamanho etapas até que convirja para o minimo
  
  * Alta taxa : o tamanho dos passos serão alto e o resultado não é tão bom
  
  * Baixa taxa : o tamanho dos passos são pequeno o que resultara no maior tempo para que convirja , e terá muitas iterações

* Para modelos de regressão linear a função é convexa oux seja não há minimo local so tem um minimo global

* Caracteristica devem está em escala semelhante
  
  * **`StandardScaler`**
  
  * **`MinMaxScaler`**

* Quando mais parametros  um modelo tem mais dimensões ele terá

```python
from sklearn.base import RegressorMixin
from typing       import Literal
import random      
class GradienteDescendente(RegressorMixin):
    gradient = None
    def __init__(self,solver:Literal['batch','stocastic','mini']='batch',eta=0.1,lenTheta=2,t0=5,t1=50,maxIter=1_000,n_epochs=100,minilotes = 2)->None:
        self.solver  = solver
        self.theta   = np.random.randn(lenTheta+1,1)
        self.eta     = 0.1
        self.maxIter = maxIter
        self.t0       = t0
        self.t1       = t1
        self.n_epochs = n_epochs
        self.minilote = minilotes


    def condition(self,vetor):
        if np.any(np.isnan(vetor)):    return True
        if np.any(np.isinf(vetor)):    return True
        if np.any(np.isneginf(vetor)): return True
        if np.any(np.isposinf(vetor)): return True
        return False
    
    def fit(self,X:np.array,y:np.array):
        m  = np.size(X,axis=0)
        Xb = np.c_[ np.ones((m,1)) ,X]
        
        cronogramaLearning = lambda t : self.t0  / (t+self.t1)
        match self.solver:
            case 'batch':
                for iter in range(self.maxIter):
                    gradient = Xb.T.dot(Xb.dot(self.theta) - y)
                    gradient = (2/m) * gradient 
                    
                    if self.condition(gradient) :break

                    self.theta = self.theta - self.eta * gradient 
                    
                    if self.condition(self.theta):break


            case 'stocastic':
                

                for epocas in range(self.n_epochs):
                    for iter in range(m):
                        randomIndex = np.random.randint(m)
                        xi = Xb[randomIndex:randomIndex+1,:]
                        yi = y[randomIndex:randomIndex+1,:]

                        gradient = 2 * xi.T.dot(xi.dot(self.theta) - yi)

                        if self.condition(gradient) :break

                        eta        = cronogramaLearning(epocas*m+iter)
                        self.theta = self.theta - eta*gradient  

                        if self.condition(self.theta):break

            case 'mini':
                samples = self.samples(m)
                for miniLote in samples:
                    for iter in range(m):
                        xi = Xb[miniLote,:]
                        yi = y[miniLote ,:]
                        
                        gradient = 2 * xi.T.dot(xi.dot(self.theta) - yi)

                        if self.condition(gradient) :break

                        eta        = cronogramaLearning(len(miniLote)*m+iter)
                        self.theta = self.theta - eta*gradient  

                        if self.condition(self.theta):break




    def samples(self,m):
        lista  = [i for i in range(m)]
        K  = int(np.ceil(m/self.minilote))
        sample  = random.sample(lista,k = K )
        samples = [sample]
        for i in range(1,self.minilote+1):
            lista  = list(set(lista)-set(sample))
            if i <= self.minilote-1:
                sample = random.sample(lista,k=K)
            else:
                sample = lista
            samples.append(sample)
            if len(samples[len(samples)-1]) == 0: del samples[len(samples)-1]
        return samples
    
    def predict(self,X):
        soma = 0
        for i in range(np.size(X,axis=1)):
            soma += self.theta[i+1] * X[:,i] 
        return self.theta[0] + soma
    
```

## Modelos Lineares Regularizados

* Uma forma de reduzir o sobreajuste é regularizar o modelo (isso é restringi-lo)

* Para um modelo linear , a regularização é normalmente obtida retringindo todos os peso do modelos
  
  * Implica em manter os todos os peso limitados ou pequenos
  
  * Impõe penalidade

* **Vantagem:**
  
  * Robustez e estabilidade: adição de novos dados não resultam em mundancas drasticas dos pesos
