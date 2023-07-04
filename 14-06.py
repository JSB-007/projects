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
    if dtype == 'datetime64[ns]':
        df[column] = df[column].dt.strftime(date_format)

print("\nUpdated DF:")
print(df)

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
print("\nTime now is:")
print(now)
