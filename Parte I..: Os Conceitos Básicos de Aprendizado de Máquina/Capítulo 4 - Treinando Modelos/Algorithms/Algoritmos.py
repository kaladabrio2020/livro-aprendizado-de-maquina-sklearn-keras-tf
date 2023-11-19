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