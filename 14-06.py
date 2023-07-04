import datetime
import pandas as pd
import random
import numpy as np

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['2022-01-01', '2022-01-02', '2022-01-03'],
                   'C': ['10:00:00', '11:00:15', '12:00:30']})

print("Original DF:")
print(df)

# Convert 'B' column to datetime
df['B'] = pd.to_datetime(df['B'])

# Convert 'C' column to datetime and combine with 'B' column
df['C'] = pd.to_datetime(df['B'].dt.date.astype(str) + ' ' + df['C'])

# Convert datetime columns to string format
date_format = "%Y-%m-%d %H:%M:%S.%f"
for column, dtype in df.dtypes.items():
    if dtype == 'datetime64[ns]' and column != "B":
        df[column] = df[column].dt.strftime(date_format)

# Convert 'B' column back to original format
df['B'] = df['B'].dt.date.astype(str)

print("\nUpdated DF:")
print(df)

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
print("\nTime now is:")
print(now)

This code creates a DataFrame with three columns: 'A', 'B', and 'C'. The 'A' column contains the integers 1, 2, and 3. The 'B' column contains three dates in string format. The 'C' column contains three times in string format.
The code then converts the 'B' column to a datetime object using the `pd.to_datetime()` function. This allows for date-related operations to be performed on the column.
Next, the code combines the date from the 'B' column with the time from the 'C' column to create a new datetime object for the 'C' column. This is done by first converting the date in the 'B' column to a string using the `.astype(str)` method, then concatenating it with the time from the 'C' column using the `+` operator, and finally converting the resulting string to a datetime object using the `pd.to_datetime()` function.
After that, the code converts the 'C' column back to a string format using the `.dt.strftime()` method. This method takes a format string as an argument and returns a string representation of the datetime object in the specified format. In this case, the format string is `"%Y-%m-%d %H:%M:%S.%f"`, which specifies that the date and time should be represented in the format `YYYY-MM-DD HH:MM:SS.ssssss`.
Finally, the code converts the 'B' column back to its original format by first converting it to a date object using the `.dt.date` attribute, then converting it to a string using the `.astype(str)` method.
The code also prints out the current time at the end, using the `datetime.datetime.now().strftime()` method. This method returns a string representation of the current time in the specified format.
