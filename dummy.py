import pandas as pd

df = pd.read_csv('USDA_Ingested.csv')
df.head()
del df['Unnamed: 0']
df.head(20)
df.isnull().sum()
x = df[(df['Protein'] <= '15(kcal/24H)') & (df['Saturated'] <= '10.0(gm)')]
x = x[x['Standard_Food_Category'] == '1']
x['FoodItem']