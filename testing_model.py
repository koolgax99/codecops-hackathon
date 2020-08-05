import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from matplotlib import pyplot as plt
import seaborn as sns
import xgboost
lr=LogisticRegression()
gb=xgboost.XGBRegressor
le = preprocessing.LabelEncoder()

df = pd.read_csv("E:/hardcode/delhi.csv")
'''
df.loc[df['Status'] =="Ready_to_move" , 'Status'] = 1.0              #0:work in progress
df.loc[df['Status'] =="Almost_ready" , 'Status'] = 0.0'''
df.Parking.fillna(0,inplace=True)
df.Bathroom.fillna(df.Bathroom.median(),inplace=True)
df.Furnishing.fillna('Unfurnished',inplace=True)
df.Type.fillna('Apartment',inplace=True)
df['Parking'].replace([39,114],2,inplace=True)
df['Parking'].replace([5,9,10],4,inplace=True)

'''
plt.subplot(2,2,1)
sns.countplot(df.Parking)
plt.grid(True)
plt.subplot(2,2,2)
sns.countplot(df.Furnishing)
plt.grid(True)
plt.subplot(2,2,3)
sns.countplot(df.Type)
plt.grid(True)
plt.subplot(2,2,4)
sns.countplot(df.Transaction)
plt.grid(True)
plt.show()
'''
df.drop('Per_Sqft',axis=1,inplace=True)
df.drop('Locality',axis=1,inplace=True)
y=df[['Price']]
