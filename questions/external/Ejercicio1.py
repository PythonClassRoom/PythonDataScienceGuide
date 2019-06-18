# -*- coding: utf-8 -*-
"""
@author: Estefania
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#a.
os.chdir("C:/Users/Estefania/Documents/UNIVERSIDAD/I Ciclo 2019/Mineria de Datos/Archivos")
datos = pd.read_csv('Titanic.csv',delimiter=',',decimal=".",index_col=0)
print(datos)
#b.
def recodificar(col, nuevo_codigo):
  col_cod = pd.Series(col, copy=True)
  for llave, valor in nuevo_codigo.items():
    col_cod.replace(llave, valor, inplace=True)
  return col_cod

datos['Survived'] = recodificar(datos['Survived'],{0:'No',1:'Si'})
datos['Pclass'] = recodificar(datos['Pclass'],{1:'primera',2:'segunda',3:'tercera'})

#c.
print(datos.mean(numeric_only=True))
print(datos.median(numeric_only=True))
print(datos.std(numeric_only=True))
print(datos.max(numeric_only=True))
print(datos.min(numeric_only=True))
print(datos.quantile(np.array([0,.25,.50,.75,1])))

#d
#Variable Survived
g_sobrevivieron = pd.crosstab(index=datos["Survived"],columns="count") 
print(g_sobrevivieron)
alto = [g_sobrevivieron['count'][0], g_sobrevivieron['count'][1]]
barras = ('No ', 'Si')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['red','blue'])
plt.xticks(y_pos, barras)

#Variable Pclass
g_clase = pd.crosstab(index=datos["Pclass"],columns="count") 
print(g_clase)
graf = [g_clase['count'][0], g_clase['count'][1],g_clase['count'][2]]
barras = ('Primera ', 'Segunda','Tercera')
y_pos = np.arange(len(barras))
plt.bar(y_pos, graf, color=['red','blue','green'])
plt.xticks(y_pos, barras)

#Variable Sexo
g_sexo = pd.crosstab(index=datos["Sex"],columns="count") 
print(g_sexo)
alto = [g_sexo['count'][0], g_sexo['count'][1]]
barras = ('Female ', 'Male')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['red','blue'])
plt.xticks(y_pos, barras)

#Variable Embarked
g_embarked = pd.crosstab(index=datos["Embarked"],columns="count") 
print(g_embarked)
graf = [g_embarked['count'][0], g_embarked['count'][1],g_embarked['count'][2]]
barras = ('Cherbourg ', 'Queenstowns','Southampton')
y_pos = np.arange(len(barras))
plt.bar(y_pos, graf, color=['red','blue','green'])
plt.xticks(y_pos, barras)

#e
boxplots = datos.boxplot(return_type='axes')

#f
#Histogramas
hist1 = datos[datos.columns[8:9]].plot(kind='hist')
hist2 = datos[datos.columns[4:5]].plot(kind='hist')
hist3 = datos[datos.columns[5:6]].plot(kind='hist')
#Densidad
densidad1 = datos[datos.columns[8:9]].plot(kind='density')
densidad2 = datos[datos.columns[4:5]].plot(kind='density')
densidad3 = datos[datos.columns[5:6]].plot(kind='density')

#Test de normalidad Fare
import scipy.stats
dat1 = datos['Fare']
shapiro_resultados = scipy.stats.shapiro(dat1)
print(shapiro_resultados)
p_value = shapiro_resultados[1]
print(p_value)

alpha = 0.05
if p_value > alpha:
    print('Si sigue la curva Normal (No se rechaza H0)')
else:
    print('No sigue la curva Normal (Se rechaza H0)')
from statsmodels.graphics.gofplots import qqplot
qqplot(dat1, line='s')

#Test de normalidad SibSp
import scipy.stats
dat = datos['SibSp']
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


#g
#scatter plot
x = datos[datos.columns[4:5]]
y = datos[datos.columns[8:9]]
plt.plot(x, y, 'o', color='black')

x = datos[datos.columns[5:6]]
y = datos[datos.columns[4:5]]
plt.plot(x, y, 'o', color='black')
#Variables 2 a 2
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(datos, hue='Survived', height=2.5)

#h
corr = datos.corr()
print(corr)

f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),square=True, ax=ax)

















