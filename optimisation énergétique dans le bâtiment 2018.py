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
from sklearn.model_selection import train_test_split        
                   
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

st = Normalizer(copy=False)

X = data.drop(['Charge de chauffage', 'Charge de refroidissement'], axis=1)
X = st.fit_transform(X)
y = data[['Charge de chauffage', 'Charge de refroidissement']  
#on prend 70% de données pour le jeu d'entrainement et 30 % pour le test        
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 123)
                   
