import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df: pd.DataFrame = pd.read_csv('data.csv')

# Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
# print(df.columns.tolist())

# Numerical Cleaning
df['price'] = df['price'].astype(str).str.replace(',','').astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(',','').astype(int)
# print(df.info())

#  Categorical Cleaning
df['status'] = df['status'].str.strip().str.lower()
df['flat_type'] = df['flat_type'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera':False})
# print(df['rera_approval'])

df = df.drop_duplicates()
# print(df)

# Q1 : Which is the costliest flat in Gurugram
costliest_flat = df.loc[df['price'].idxmax()]
print(f"The costliest flat in Gurugram is a {costliest_flat['bhk_count']} BHK {costliest_flat['flat_type']} located in {costliest_flat['locality']} with a price of {costliest_flat['price']/10000000} Crores.")

# Q2 : Which locality has the highest average price?
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(f'{highest_avg_price_locality} locality has the highest average price.')

# Q3 : Which locality has the highest rate per square foot?
highest_rate_per_sqft = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f'The locality with the highest rate per sqft is {highest_rate_per_sqft}.')

# Q4 : Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()

# print(ready_to_move_avg_price)
# print(under_construction_avg_price)

if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready to Move properties costs more than Under construction properties.")
else:
    print("Under construction properties costs more than Ready to Move properties.")

# Q5: Do RERA-approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
not_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()
print(rera_approved_avg_price, not_rera_approved_avg_price)

if rera_approved_avg_price > not_rera_approved_avg_price:
    print("Yes, RERA approved properties does charge a price premium.")
else:
    print("No, RERA approved properties does not charge a price premium..")

# Q6 : How does area (sqft) impact property price?
sns.scatterplot(data=df, x='area', y='price')
plt.title('Area (sqft) vs Price')
plt.show()

# Q7 : Which BHK configuration is the most expensive on average?
most_expensive_bhk = df.groupby('bhk_count')['price'].mean().idxmax()
print(f'Most expensive BHK configuration is {most_expensive_bhk} BHK.')

# Q8 : Which property type (Apartment, Floor, Plot) is the costliest?
property_types_avg_price = df.groupby('flat_type')['price'].mean().idxmax()
print(f'The most expensive property type is {property_types_avg_price}.')

# Q9 : Do certain builders or companies consistently price higher?
print("top 5 builder who price higher are :", end=" ")
top_5_builders = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5) 
for builder in top_5_builders.index:
    print(builder, end=', ')

# Q10 : Are larger homes always more expensive per square foot?
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.title('Area (sqft) vs Rate per Sqft')
plt.show() 

