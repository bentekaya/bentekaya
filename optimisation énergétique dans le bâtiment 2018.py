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
data.head()
correlation = data.corr()
plt.figure(figsize=(11,11))
sns.heatmap(correlation,annot=True)
