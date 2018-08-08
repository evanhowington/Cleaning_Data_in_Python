import pandas as pd
airquality = pd.read_csv('airquality.csv')
print(airquality)

# print the head of airquality
print(airquality.head())
# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame = airquality, id_vars=['Month','Day'], value_vars=['Ozone', 'Solar.R', 'Wind', 'Temp', 'airquality'])
# print the head of airquality_melt
print(airquality_melt.head())


"""
Customizing melted data
"""

# print the head of airquality
print(airquality.head())
# Melt airquality: airquality_melt
airquality_melt =  pd.melt(frame= airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')
# print the head of airquality_melt
print(airquality_melt.head())

"""
Pivot Data
"""
# print the head of airquality_melt
print(airquality_melt.head())
# pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')
# print the head of airquality_pivot
print(airquality_pivot.head())


print('\n BREAK IN CODE SO I CAN SEE WHAT THE DIFFERENT OUTPUTS LOOK LIKE IN THEIR ENTIRETY, NOT JUST THE HEAD \n')

print(airquality)
print(airquality_melt)
print(airquality_pivot)


"""
Resetting the index of a dataframe 
"""

# print the index of airquality_pivot
print(airquality_pivot.index)
# reset the index of airquality_pivot: airquality_pivot_reset
airquality_pivot_reset = airquality_pivot.reset_index()
# print the new index of airquality_pivot_reset
print(airquality_pivot_reset.index)
# print the head of airquality_pivot_reset
print(airquality_pivot_reset.head())

print('\n BREAK IN CODE SO I CAN SEE WHAT THE DIFFERENT OUTPUTS LOOK LIKE IN THEIR ENTIRETY, NOT JUST THE HEAD \n')


print(airquality)
print(airquality_melt)
print(airquality_pivot)
print(airquality_pivot_reset)



"""
Splitting a column with .split() and .get()
"""
# Melt ebola: ebola_melt
import pandas as pd
ebola = pd.read_csv('ebola.csv')
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())