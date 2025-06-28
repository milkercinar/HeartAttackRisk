import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.discriminant_analysis import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('heart.csv')

df.hist(figsize=(18,12), bins=20, edgecolor='black')
plt.suptitle('Veri Dağılımı')
#plt.show()

df.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Age', y='Cholesterol', hue='HeartDisease')
plt.title('Yaş ve Kolesterol Arasındaki İlişki')
# plt.show
