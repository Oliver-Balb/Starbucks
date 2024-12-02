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
