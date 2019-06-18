# -*- coding: utf-8 -*-
"""
@author: Estefania
"""
#Ejercicio #2
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#a.
os.chdir("C:/Users/Estefania/Documents/UNIVERSIDAD/I Ciclo 2019/Mineria de Datos/Archivos")
datos1 = pd.read_csv('SAheart.csv',delimiter=';',decimal=".",index_col=0)
print(datos1)
#b. No hay variables que puedan ser recodificadas

#c.
print(datos1.mean(numeric_only=True))
print(datos1.median(numeric_only=True))
print(datos1.std(numeric_only=True))
print(datos1.max(numeric_only=True))
print(datos1.min(numeric_only=True))
print(datos1.quantile(np.array([0,.25,.50,.75,1])))

#d.
#Variable famhist
g_fam = pd.crosstab(index=datos1["famhist"],columns="count") 
print(g_fam)
alto = [g_fam['count'][0], g_fam['count'][1]]
barras = ('Absent', 'Present')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['red','blue'])
plt.xticks(y_pos, barras)

#Variable chd
g_chd = pd.crosstab(index=datos1["chd"],columns="count") 
print(g_chd)
alto = [g_chd['count'][0], g_chd['count'][1]]
barras = ('No', 'Si')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['red','blue'])
plt.xticks(y_pos, barras)

#e
boxplots = datos1.boxplot(return_type='axes')

#f
#Histogramas
hist1 = datos1[datos1.columns[6:7]].plot(kind='hist')
hist2 = datos1[datos1.columns[0:1]].plot(kind='hist')
hist3 = datos1[datos1.columns[5:6]].plot(kind='hist')
#Densidad
densidad1 = datos1[datos1.columns[6:7]].plot(kind='density')
densidad2 = datos1[datos1.columns[0:1]].plot(kind='density')
densidad3 = datos1[datos1.columns[5:6]].plot(kind='density')

#test de normalidad tobacco
import scipy.stats
dat = datos1['tobacco']
shapiro_resultados = scipy.stats.shapiro(dat)
print(shapiro_resultados)
p_value = shapiro_resultados[1]
print(p_value)

alpha = 0.05
if p_value > alpha:
    print('Si sigue la curva Normal (No se rechaza H0)')
else:
    print('No sigue la curva Normal (Se rechaza H0)')
from statsmodels.graphics.gofplots import qqplot
qqplot(dat, line='s')

dat1 = datos1['tobacco']
shapiro_resultados = scipy.stats.shapiro(dat1)
print(shapiro_resultados)
p_value = shapiro_resultados[1]
print(p_value)

#test de normalidad obesity
alpha = 0.05
if p_value > alpha:
    print('Si sigue la curva Normal (No se rechaza H0)')
else:
    print('No sigue la curva Normal (Se rechaza H0)')
from statsmodels.graphics.gofplots import qqplot
qqplot(dat, line='s')

#g
#scatter plot
x = datos1[datos1.columns[0:1]]
y = datos1[datos1.columns[5:6]]
plt.plot(x, y, 'o', color='pink')

x = datos1[datos1.columns[6:7]]
y = datos1[datos1.columns[7:8]]
plt.plot(x, y, 'o', color='pink')

#Variables 2 a 2
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(datos1, hue='chd', height=2.5)

#h
corr = datos1.corr()
print(corr)

f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),square=True, ax=ax)