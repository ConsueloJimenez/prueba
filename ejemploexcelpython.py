import pandas as pd
from numpy import *
#import matplotlib.pyplot as plt
#import seaborn as sns
path= '/Users/cjimenez/Desktop/archivosPython/ejemploDatos.xlsx'
#pd.read_excel(path,'Hoja1')
xls=pd.ExcelFile(path)
print(xls.sheet_names)
df1=xls.parse('Hoja1')
print(df1)
df2=xls.parse('Hoja2')
print(df2)
columna1=df1[:3]# accede a los primeros tres registros
print(columna1)
print(df1.loc[0])#accede al primer registro
print(df1['matricula'])
print(df1['nombre'])
df2=xls.parse('Hoja2')
print(df2)
print(df2['calif'])
print(df2['calif'].mean())
""" manejo de data frames"""
alumnos=['carlos','juan','rosario']
calif=[100,100,100]
grupo={'alumnos':alumnos,'calificacion':calif}
df=pd.DataFrame(grupo)
print(df)
print(df['calificacion'].mean())
print(df['calificacion'].describe())




#manejo de arreglos

datos=[1,2,3,4]
a=array(datos)
print("longuitud", len(datos))
print("el menor es", a.min())
print("la suma es", a.sum())
serie=pd.Series(datos)
print(datos)
print(serie.size)
print(serie.describe())
datos.append(5)

for i in datos:
    print(i)



datos2=[[2,2],[4,1]]
for i in range(2):
    print(datos2[i][0],' ',datos2[i][1])
