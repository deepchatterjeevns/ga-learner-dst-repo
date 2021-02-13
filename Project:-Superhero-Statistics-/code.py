# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Reading of the file
data=pd.read_csv(path)

# Code starts here
data.Gender.replace('-','Agender',inplace=True)

# Barplot for Gender count
sns.countplot(x=data['Gender'])

# Pie chart for Alignment
sns.countplot(x=data['Alignment'])

# Covariance of Strength','Combat'
new_df = data[['Combat','Strength']].copy()

covariance = new_df.cov().iloc[0,1]
std_Combat = new_df['Combat'].std()
std_Strength = new_df['Strength'].std()
pearson = covariance/(std_Combat * std_Strength)

print('Pearson Correlation Coefficient :', pearson)


super_best_list = data['Total'].quantile(q=0.99)
super_best_df = data[data['Total']> super_best_list]
super_best_names=list(super_best_df['Name'])










