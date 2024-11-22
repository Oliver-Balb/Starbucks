import pandas as pd
import ast
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', 100)

# Example Series
data = pd.Series([10, 20, 30, 40])

print(type(data))

for value in data:
    print(value)

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
