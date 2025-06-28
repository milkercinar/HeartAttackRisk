import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.discriminant_analysis import StandardScaler

df= pd.read_csv("heart.csv")

categorical_columns = ['ChestPainType','Sex','RestingBP','ExerciseAngina','ST_Slope']

le = LabelEncoder()
for column in categorical_columns:
    df[column] = le.fit_transform(df[column])


numeric_columns = ['Age','RestingBP','Cholesterol','FastingBS', 'MaxHR','Oldpeak']

scaler = StandardScaler()
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
print(df.head())

df.to_csv('heart_düzenlenmiş.csv', index=False)


