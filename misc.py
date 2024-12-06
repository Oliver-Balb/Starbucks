import pandas as pd

# Sample data for the first pivot table
data1 = {
    'gender': ['F', 'F', 'M', 'M'],
    'income_range': ['25000-49999', '50000-74999', '25000-49999', '50000-74999'],
    'age_group': ['18-27', '28-37', '18-27', '28-37'],
    'offer_trx_amount': [100, 200, 150, 250]
}

# Sample data for the second pivot table
data2 = {
    'gender': ['F', 'F', 'M', 'M'],
    'income_range': ['25000-49999', '50000-74999', '25000-49999', '50000-74999'],
    'age_group': ['18-27', '28-37', '18-27', '28-37'],
    'offer_trx_amount': [0, 100, 75, 125]
}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print(df2)

# Create pivot tables
pivot1 = pd.pivot_table(df1, values='offer_trx_amount', index=['gender', 'income_range'], columns=['age_group'], aggfunc='sum', fill_value=0)
pivot2 = pd.pivot_table(df2, values='offer_trx_amount', index=['gender', 'income_range'], columns=['age_group'], aggfunc='sum', fill_value=0)

print(pivot1)
print(pivot1)

# Perform element-wise division
result = pivot1 / pivot2

# Display the result
print(result)

quit()



### HEAT MAP based on PIVOT TABLE

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'age_group': ['18-27', '28-37', '38-47', '48-57', '58-67', '68-77', '78-'],
    'F_100000+': [0.00, 103.26, 446.39, 15664.95, 16500.35, 12965.33, 9764.05],
    'F_25000-49999': [4273.03, 4537.58, 4124.07, 4708.20, 4743.67, 3106.95, 2415.47],
    'F_50000-74999': [7863.31, 9942.97, 15551.20, 24828.90, 21917.01, 12127.88, 9764.56],
    'F_75000-99999': [745.97, 1558.76, 9134.00, 36263.05, 37566.28, 22517.17, 17117.35],
    'M_100000+': [0.00, 0.00, 335.02, 9792.16, 9143.36, 5382.01, 4773.43],
    'M_25000-49999': [7183.29, 7755.83, 7921.62, 6430.88, 7073.02, 4159.52, 1875.16],
    'M_50000-74999': [8958.66, 12714.38, 19094.04, 29471.43, 23238.07, 14126.90, 10002.03],
    'M_75000-99999': [78.20, 1300.23, 11173.95, 25097.96, 28555.39, 19967.86, 7835.13],
    'O_100000+': [0.00, 0.00, 58.30, 51.13, 0.00, 0.00, 0.00],
    'O_25000-49999': [97.62, 156.11, 221.13, 153.59, 509.13, 21.50, 1.54],
    'O_50000-74999': [158.74, 269.32, 533.10, 688.36, 915.62, 779.93, 143.76],
    'O_75000-99999': [0.00, 61.69, 390.83, 1589.44, 1300.30, 345.43, 281]
}

# Create DataFrame
df = pd.DataFrame(data)

# Reset the index to use numeric values
df = df.reset_index()

# Generate a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df.set_index('index'), annot=True, fmt=".2f", cmap="YlGnBu")

# Add title and labels
plt.title('Heat Map of Income Ranges by Age Group and Gender')
plt.xlabel('Income Range and Gender')
plt.ylabel('Age Group')

# Show the plot
plt.show()

quit()



# ### PIVOT Table ###
import pandas as pd

d = {'A': ['rot', 'grün', 'blau', 'rot', 'grün', 'blau'],
     'B': ['eins', 'zwei', 'eins', 'zwei', 'drei', 'vier'],
     'C': [345, 325, 898, 989, 23, 143],
     'D': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(d)

print(df)

print('\n===================================\n')

df2 = df.pivot(index = 'A', 
               columns = 'B', 
               values='C')
print(df2)

print('\n===================================\n')

quit()


import pandas as pd

def group_ages_into_n_groups(df, n):
    # Sort the dataframe by age
    df = df.sort_values(by='age')
    
    # Calculate the total number of people
    total_people = df['count_person'].sum()
    
    # Calculate the target number of people per group
    target_per_group = total_people / n
    
    # Initialize variables
    groups = []
    current_group = []
    current_group_count = 0
    
    # Iterate over the dataframe rows
    for index, row in df.iterrows():
        age = row['age']
        count = row['count_person']
        
        # If adding this age to the current group exceeds the target, start a new group
        if current_group_count + count > target_per_group and len(groups) < n - 1:
            groups.append(current_group)
            current_group = []
            current_group_count = 0
        
        # Add the current age to the group
        current_group.append((age, count))
        current_group_count += count
    
    # Add the last group if it's not empty
    if current_group:
        groups.append(current_group)
    
    return groups

# Example usage
data = {'age': [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 95, 96, 97, 98, 99, 100, 101, 118],
        'count_person': [70, 135, 135, 140, 131, 171, 101, 97, 117, 82, 147, 144, 122, 132, 80, 55, 20, 5, 5, 12, 5, 3]}
df = pd.DataFrame(data)

n = 3
groups = group_ages_into_n_groups(df, n)
for i, group in enumerate(groups):
    print(f"Group {i+1}: {group}")

# Initialize a dictionary to store the sums
sums = {}

# Iterate over each group and sum the second values of each tuple
for i, group in enumerate(groups):
    group_name = f'Group {i+1}'
    sums[group_name] = sum(value for _, value in group)

# Print the result
print(sums)

quit()



import pandas as pd

# Create a pandas dataframe transcript_norm_pers_time with column reward containing values 5, 2
data = {'reward': [4, 4, 2]}
transcript_norm_pers_time = pd.DataFrame(data)

# Define the amount to be distributed
amount = 100.0

# Calculate the total reward
total_reward = transcript_norm_pers_time['reward'].sum()

# Distribute the amount according to the reward value into a new column amount_share
transcript_norm_pers_time['amount_share'] = (transcript_norm_pers_time['reward'] / total_reward) * amount

# Display the dataframe
print(transcript_norm_pers_time)

quit()





transcript = pd.read_json('data/transcript.json', orient='records', lines=True)

def split_dict_into_cols(df, col):
    ''' 
    For an entire Pandas dataframe normalize the dictionary value pairs from
    column col into individual columns named by key value.
    Correct misspelled keys for "offer_id"
    
    Arguments:
    df - Pandas dataframe
    col - Column name containing dictionary values as strings
    
    Returns:
    df_result - Dataframe with multivalue column normalized into separate columns
    df_conversion_errors - Dataframe with rows that failed to convert
    '''   

    # Initialize a list to store rows that fail to convert
    conversion_errors = []

    # Iterate over each row in the dataframe
    for index, row in df.iterrows():

        dictval = row[col]
        for key, value in dictval.items():
            # Correct misspelled keys for "offer_id"
            if key == 'offer id':
                key = 'offer_id'
            # print(f"Key: {key}, Value: {value}")
            #df.loc[index, key] = value
            df.loc[index, (key)] = value
      
    return df 

df_result = split_dict_into_cols(transcript, 'value')
df_result.to_excel('data/transcript_normalized.xlsx')



# Process the 'event chain' person by person
for person in persons_unique:
    # Get all offers completed records in order to get their time value
    transcript_norm_pers_of_test = transcript_norm_test[((transcript_norm_test['person'] == person) & (transcript_norm_test['event'] == 'offer completed'))]
    for time in transcript_norm_pers_of_test['time']:
        # Calculate the sum of all rewards of offers at that point in time:
        sum_rewards = transcript_norm_pers_of_test[transcript_norm_pers_of_test['time'] == time]['reward'].values.sum()
        for offer_id in transcript_norm_pers_of_test[transcript_norm_pers_of_test['time'] == time]['offer_id']:
            # Use each time value to get the previous transaction record and amount
            # As sometimes multiple offers are completed at the same time, split the transaction value according to the reward ratio of all completed offers at time *time*
            amount_of_compl = round((transcript_norm_test[((transcript_norm_test['person'] == person) & (transcript_norm_test['event'] == 'transaction') & 
                                                    (transcript_norm_test['time'] == time))]['amount'].values.sum()) * 
                                    (transcript_norm_test[((transcript_norm_test['person'] == person) & (transcript_norm_test['event'] == 'offer completed') & 
                                                    (transcript_norm_test['time'] == time) & (transcript_norm_test['offer_id'] == offer_id))]['reward'].values.sum()) /
                                    sum_rewards, 2) 

            # Write the (distributed) amount of completion to the offer completed record.      
            transcript_norm_test.loc[(transcript_norm_test['person'] == person) & (transcript_norm_test['event'] == 'offer completed') & 
                                     (transcript_norm_test['time'] == time) & (transcript_norm_test['offer_id'] == offer_id), 'amount_of_compl'] = amount_of_compl
        
transcript_norm_test[transcript_norm_test['event'] == 'offer completed']
