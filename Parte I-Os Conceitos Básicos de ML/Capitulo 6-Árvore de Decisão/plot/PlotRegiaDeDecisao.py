import numpy as np 
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap


def plotDecisionRegion(X,y,classifier,resolution=0.02):
    marks = ('o','s','^','v','<')
    color = ('red','blue','lightgreen','gray','cyan')

    cmap  = ListedColormap(colors=color[:len(np.unique(y))])

    x1Min, x1Max = X[:,0].min() - 1, X[:,0].max() + 1 
    x2Min, x2Max = X[:,1].min() - 1, X[:,1].max() + 1

    xx1, xx2 = np.meshgrid(
        np.arange(x1Min,x1Max,resolution),
        np.arange(x2Min,x2Max,resolution)
    ) 
    x = np.array([xx1.ravel(),xx2.ravel()])
    lab = classifier.predict(x.T)

    lab = lab.reshape(xx1.shape)

    plt.contourf(xx1,xx2,lab,alpha=0.3,cmap=cmap)
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[ y == cl,0 ],y=X[ y == cl,1 ] , alpha=0.8,c=color[idx],marker=marks[idx],edgecolors='black')
    
    plt.legend(np.unique(y))
    plt.show()


def plotDecisionRegion2(X, y, classifier, testIndex=None, resolution=0.02):
    markts = ('o','s','^','v','<')
    colors = ('red','blue','lightgreen','gray','cyan')

    cmap  = ListedColormap(colors=colors[:len(np.unique(y))])

    x1Min, x1Max = X[:,0].min() - 1, X[:,0].max() + 1 
    x2Min, x2Max = X[:,1].min() - 1, X[:,1].max() + 1

    xx1, xx2 = np.meshgrid(
        np.arange(x1Min,x1Max,resolution),
        np.arange(x2Min,x2Max,resolution)
    ) 
    x = np.array([xx1.ravel(),xx2.ravel()])
    lab = classifier.predict(x.T)

    lab = lab.reshape(xx1.shape)

    plt.contourf(xx1,xx2,lab,alpha=0.3,cmap=cmap)
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter( x=X[ y == cl,0 ],
                     y=X[ y == cl,1 ],
                     alpha=0.85,
                     c=colors[idx],
                     marker=markts[idx],
                     edgecolor='black',
                     label=f'Class {cl}',s=50)
                     


    if testIndex:
        xtest, ytest = X[testIndex,:], y[testIndex]
        plt.scatter( xtest[:,0] , xtest[:,1], 
                    c='none', 
                    edgecolors='black', 
                    alpha=1,
                    linewidths=1, 
                    marker='o', 
                    s=150, 
                    label='Test set')
    plt.legend()
    plt.tight_layout()
    plt.show()
    

