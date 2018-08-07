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