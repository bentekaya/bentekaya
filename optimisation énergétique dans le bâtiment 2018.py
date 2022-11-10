#outpout:y1 Charge de chauffage ,y2 Charge de refroidissement
 #Input:
#X1: Orientation
#x2:Surface de vitrage
#X3 :Surface des murs
#tous les variables x,y sont des variables quantitatives
#importer les données nécesaite
data = pd.read_csv(rania.csv')

import pandas as pd
import pandas_profiling
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import Normalizer
                   
data.head()
#corrélation entre les données
correlation = data.corr()
plt.figure(figsize=(11,11))
sns.heatmap(correlation,annot=True)
plt.figure(figsize=(5,5))
#corrélation entre les variables
sns.pairplot(data=data, y_vars=['Charge de chauffage', 'Charge de refroidissement'],
x_vars=[ 'Surface des murs','Orientation', 'Surface de vitrage'])
plt.show()
#prédiction de la charge de refroidissement et de chauffement par la méthade de régression linéaire
#standarisation 
                   
                   
