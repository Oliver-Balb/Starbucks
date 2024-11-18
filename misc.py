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
