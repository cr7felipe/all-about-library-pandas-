#extract the row from dataframe as a series object
import pandas as pd
dates ={'A':[1,2,3,4],'B':[5,6,7,8],'C':[9,10,11,12]}#is the set
df=pd.DataFrame(dates)#convert the seto to the df
row=df.iloc[2,:]#extract the row number 1 for all columns
print(row) #show
