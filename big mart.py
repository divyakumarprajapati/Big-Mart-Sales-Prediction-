import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("Train.csv")
#viewing different types of characters in different variables
A = dataset.Item_Fat_Content.value_counts()
B = dataset.Item_Type.value_counts()
C = dataset.Outlet_Identifier.value_counts()
D = dataset.Outlet_Establishment_Year.value_counts()
E = dataset.Outlet_Size.value_counts()
F = dataset.Outlet_Location_Type.value_counts()
G = dataset.Outlet_Type.value_counts()
dataset = dataset.replace("low fat", "Low Fat")
dataset.Item_Fat_Content = dataset.Item_Fat_Content.replace("LF", "Low Fat")
dataset.Item_Fat_Content = dataset.Item_Fat_Content.replace("reg", "Regular")
dataset.isnull().sum()
A1 = dataset[dataset.Item_Weight.isnull() == True]
A2 = dataset[dataset.Outlet_Size.isnull() == True]
B1 = dataset.Outlet_Size[dataset.Outlet_Location_Type == "Tier 3" ].value_counts()

df=dataset.dropna() 
df = df[df.Outlet_Size == "Small"]
sns.distplot(df['Item_Outlet_Sales']); 

df1=dataset.dropna() 
df1 = df1[df1.Outlet_Size == "Medium"]
sns.distplot(df1['Item_Outlet_Sales']); 

df2=dataset.dropna() 
df2 = df2[df2.Outlet_Size == "High"]
sns.distplot(df2['Item_Outlet_Sales']); 

df3 = dataset.dropna()
df3.Outlet_Size[df3.Item_Outlet_Sales <= 800].value_counts()

dataset.Outlet_Size = dataset.Outlet_Size.replace(dataset.Outlet_Size[dataset.Outlet_Location_Type == "Tier 3"][dataset.Outlet_Establishment_Year == 1998],"Medium-Small")
dataset.Outlet_Size = dataset.Outlet_Size.replace(dataset.Outlet_Size[dataset.Outlet_Location_Type == "Tier 2"][dataset.Outlet_Type == "Supermarket Type1"],"Small")
dataset.Item_Fat_Content = dataset.Item_Fat_Content.replace("Low Fat", 1)
dataset.Item_Fat_Content = dataset.Item_Fat_Content.replace("Regular", 0)
A1.Item_Fat_Content = A1.Item_Fat_Content.replace("Low Fat", 1)
A1.Item_Fat_Content = A1.Item_Fat_Content.replace("Regular", 0)
df = dataset.dropna()

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(dataset.iloc[:, 1:2])
dataset.iloc[:, 1:2] = imputer.transform(dataset.iloc[:, 1:2])

dataset.Item_Type.value_counts().plot.bar()



