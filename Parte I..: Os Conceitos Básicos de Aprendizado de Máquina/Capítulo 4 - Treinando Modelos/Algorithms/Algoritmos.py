import numpy as np
from typing       import Literal,_LiteralGenericAlias
from sklearn.base import RegressorMixin


class RegressaoLinear(RegressorMixin):
    theta = None
    def __init__(self, solver=Literal['normal','svd']):
    
        if (type(solver) == _LiteralGenericAlias):
            self.solver = 'normal'
        else:
            self.solver = solver

    def fit(self,X:np.array, y:np.array):
        m = np.size(X)
        X = np.c_[ np.ones((m,1)) , X]
        if (self.solver == 'normal'):
            self.theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)     
        
        return self.theta
        
    
    def predict(self,X:np.array)->Literal['Valor y']:
        return (self.theta[1] * X ) + self.theta[0] # y = theta_0 + theta_1x1.....
    

import numpy as np
import plotly.graph_objects as go

# Gerar dados aleatórios para x
np.random.seed(0)
x = np.linspace(-100, 100, 50)
# Gerar dados aleatórios para y com uma relação linear acrescida de ruído
y = 2 * x + 1 + np.random.normal(size=x.size)

# Função para calcular o erro quadrático
def calcular_erro_quadratico(coeficiente, intercepto):
    y_pred = coeficiente * x + intercepto
    erro = np.sum((y_pred - y) ** 2)
    return erro

# Criar uma grade de valores para coeficiente e intercepto
coef_grid, intercepto_grid = np.meshgrid(np.linspace(1, 3, 100), np.linspace(-2, 4, 100))

# Calcular o erro quadrático para cada combinação de coeficiente e intercepto
erro_grid = np.array([[calcular_erro_quadratico(coef, intercepto) for coef, intercepto in zip(row_coef, row_intercepto)] for row_coef, row_intercepto in zip(coef_grid, intercepto_grid)])

# Criar o gráfico 3D usando Plotly
fig = go.Figure(data=[go.Surface(z=erro_grid, x=coef_grid, y=intercepto_grid)])
fig.update_layout(title='Erro Quadrático em relação aos Coeficientes da Regressão Linear',
                  scene=dict(
                      xaxis_title='Coeficiente',
                      yaxis_title='Intercepto',
                      zaxis_title='Erro Quadrático'
                  ))

# Mostrar o gráfico
fig.show()
