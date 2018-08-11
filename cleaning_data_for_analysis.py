"""
Converting Data Types
"""

import pandas as pd

tips = pd.read_csv('tips.csv')
# print the dataframe to check for proper loading, then comment it out once verified
# print(tips)

# This is where the exercise begins.
# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

# print the info of tips
print(tips.info())

"""
working with numeric data
"""

# convert 'total_bill' to a numeric dtype using the pd.to_numeric() function
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')

# convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')

# print the info of tips
print(tips.info())

"""
String parsing with regular expressions
"""

# import the regular expression module
import re

# compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# see if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# see if the pattern matches
result2 = prog.match('1123-456-7890')
print(bool(result2))


"""
Extracting numerical values from strings
"""
# Import the regular expression module
import re

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)


"""
Pattern Matching 
"""
# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

# Write the second pattern
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

# Write the third pattern
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)


# Write the lambda function using replace
tips['total_dollar_replace'] = tips.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('$', ''))

# Print the head of tips
print(tips.head())
