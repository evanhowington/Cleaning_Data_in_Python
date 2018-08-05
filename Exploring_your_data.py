"""
Loading and reviewing your data
"""

# import pandas
import pandas as pd
pd.set_option('display.max_columns', None)
# read the file into a dataframe: df
df = pd.read_csv('dob_job_application_filings_subset.csv')
# print the head of df
print(df.head())
# print the tail of df
print(df.tail())
# print the shape of df
print(df.shape)
# print the columns of df
print(df.columns)


"""
Further Diagnosis
"""
# print the info of df
print(df.info())
# print the info of df_subset
# print(df_subset.info())
# the above line is commented out because the df_subset object is loaded in datacamp and not available locally.

print('\n This line is soley for separating outputs and serves no other function \n')

"""
Frequency counts for categorical data
"""
# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))
# print the value_counts for 'State'
print(df.State.value_counts(dropna=False))
# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))

print('\n THE LINE IS SOLEY FOR SEPARATING OUTPUTS AND SERVES NO OTHER FUNCTION \n')


"""
Visualizing single variables in histograms
"""
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()

print('\n THE LINE IS SOLEY FOR SEPARATING OUTPUTS AND SERVES NO OTHER FUNCTION \n')
"""
Visualizing multiple variables with boxplots
"""
#print(df.columns)
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# create the boxplot
df.plot(kind='box', rot=90, x='Initial Cost', by='Borough')
# display the plot
plt.show()
### THIS BOXPLOT IS STILL THROWING AN ERROR:  RUNTIMEWARNING: INVALID VALUE ENCOUNTERED IN PERCENTILE INTERPOLATION=INTERPOLATION
### original code replaced 'x' with 'column' and 'by' was 'by', however that did NOT produce a plot
###  Need to figure out the plot issue with df.boxplot.......