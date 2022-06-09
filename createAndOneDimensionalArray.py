import pandas as pd
dates=[1,2,3,4,5,6]
serie =pd.Series(dates)#convert to dt

print(serie)# print the dt 
print(len(serie))#get array size // obtener el tamaño del arreglo 
information=serie.describe()#this is important for to know about the array one dimension 
print(information) 