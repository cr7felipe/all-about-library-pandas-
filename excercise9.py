#obtain a column of a objet dataframe how a  series object 
#obtener una columna de un marco de datos de objeto cómo un objeto de serie
import pandas as pd
dates = {'A':[1,2,3,4,5],'B':[6,7,8,9,10],'C':[11,12,13,14,15]}
df= pd.DataFrame(data=dates)# convert the set to the df
print(type(df)) #show in the screen the type
columna = df['B'] #extract the columb number 1 or b
print(columna)#show in the screen the column b
print(type(columna))