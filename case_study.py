import pandas as pd
g1800s = pd.read_csv('gapminder.csv', index_col=0)
pd.set_option('display.max_columns', None)
print('This is the head \n')

print(g1800s.head())
print('This is the info \n')
print(g1800s.info())
print('This is the description of the dataframe \n')
print(g1800s.describe())
print('These are the columns of the dataframe\n')
print(g1800s.columns)
print('This is the shape of the data frame \n')
print(g1800s.shape)

import matplotlib.pyplot as plt

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()

"""

import numpy
def check_null_or_valid(row_data):
    \"\"\"Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
   \"\"\"
    no_na = row_data.dropna()[1:-1]
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

# Check whether the first column is 'Life expectancy'
assert g1800s.columns[0] == 'Life expectancy'

# Check whether the values in the row are valid
assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Check that there is only one instance of each country
assert g1800s['Life expectancy'].value_counts()[0] == 1


^^^ doesnt work here because datacamp is preloaded differently


# Add first subplot
plt.subplot(2, 1, 1)

# Create a histogram of life_expectancy
gapminder.life_expectancy.plot(kind='hist')

# Group gapminder: gapminder_agg
gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()

# Print the head of gapminder_agg
print(gapminder_agg.head())

# Print the tail of gapminder_agg
print(gapminder_agg.tail())

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
gapminder_agg.plot()

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
plt.show()

# Save both DataFrames to csv files
gapminder.to_csv('gapminder.csv')
gapminder_agg.to_csv('gapminder_agg.csv')

^^^ doesnt work here because datacamp is preloaded differently

"""
