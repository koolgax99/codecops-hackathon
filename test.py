import pandas as pd

path = r"Bengaluru_House_Data.csv"
df = pd.read_csv(path)

print(df)

x = df.drop('price', axis = 1)
y = df['price']

print('shape of x =', x.shape)
print('shape of y = ', y.shape)