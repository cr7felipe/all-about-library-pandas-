import pandas as pd

serie= pd.Series(['10', '20','python','21','felipe']) # this is the siries with strig
dates =pd.to_numeric(serie, errors='coerce') # this is a conversion string to numeric and asign nan to values python
print(dates)
