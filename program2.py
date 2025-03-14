#Calculate the average of each category of a dataframe
import pandas as pd

# Sample DataFrame
data = {'Category': ['A', 'C', 'A', 'C', 'B'],
        'Value': [50, 20, 15, 25, 30]}
df = pd.DataFrame(data)

# Calculate the average value for each category
average_df = df.groupby('Category')['Value'].mean().reset_index()

#if there are more than two columns and to keep the ordering of category column same  
#average_df = df.groupby(['Category'], sort=False, as_index=False)['Value'].mean().reset_index() 

print(average_df)
