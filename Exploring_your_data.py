"""
Loading and reviewing your data
"""

# import pandas
import pandas as pd
pd.set_option('display.max_columns', None)
# read the file into a dataframe: df
df = pd.read_csv('dob_job_application_filings_subset.csv', index_col=0)
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
