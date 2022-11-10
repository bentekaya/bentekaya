#outpout:y1 Charge de chauffage 
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
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
                   
data.head()
#corrélation entre les données
correlation = data.corr()
plt.figure(figsize=(11,11))
sns.heatmap(correlation,annot=True)
plt.figure(figsize=(5,5))
#corrélation entre les variables
sns.pairplot(data=data, y_vars=['Charge de chauffage']
x_vars=[ 'Surface des murs','Orientation', 'Surface de vitrage'])
plt.show()
#prédiction de la charge de refroidissement et de chauffement par la méthade de régression linéaire
#standarisation 

st = Normalizer(copy=False)

X = data.drop(['Charge de chauffage'], axis=1)
X = st.fit_transform(X)
y = data['Charge de chauffage'] 
#on prend 70% de données pour le jeu d'entrainement et 30 % pour le test        
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 123)
print("xtrain",X_train.shape)
print("xtest",X_test.shape)
print("ytrain",Y_train.shape)
print("ytest",Y_test.shape)
#entrainement du modéle
model = LinearRegression()
#on cherche la droite mieux ajusté qui passe par tous les points y=ax1+bx2+cx3+a0
model.fit(X_train, Y_train)

02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
# Evaluation du training set

y_train_predict = model.predict(X_train)
rmse = (np.sqrt(mean_squared_error(Y_train, y_train_predict)))
score = r2_score(Y_train, y_train_predict)
print("score",score)
                   
