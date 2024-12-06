import pandas as pd

def split_strlist_into_cols(df, col):
    ''' 
    For an entire Pandas dataframe split up list of values into one-hot-encoded separated columns
    with common column name prefix <col>_
    
    INPUT
    df - Pandas dataframe 
    col - Column name within dataframe
    
    OUTPUT
    df_result - Dataframe with multivalue column normalized into separate columns
    '''   
    # One-hot encode the col column
    
    # Ensure the column values are lists
    df = df.copy()
    df.loc[:, col] = df[col].apply(eval)
    
    # One-hot encode the col column
    encoded_df = df[col].apply(lambda x: pd.Series(1, index=x)).fillna(0).astype(int)
    
    # Add prefix to the new columns
    encoded_df = encoded_df.add_prefix(col + '_')
    
    # Drop the original column
    df_result = df.drop(col, axis=1)
    return df_result.join(encoded_df)


def one_hot_encode(df, col):
    ''' 
    For an entire Pandas dataframe one-hot-encode a column with singular values
    into columns with common column name prefix <col>_
    
    INPUT
    df - Pandas dataframe 
    col - Column name within dataframe
    
    OUTPUT
    df_result - Dataframe with nominal value column normalized into separate columns (one-hot-encoded)
    '''   

    # One-hot encode the col column
    encoded_df = pd.get_dummies(df[col], prefix=col).astype(int)
    
    # Replace old column by new one-hot-encoded columns
    df_result = df.join(encoded_df)
    df_result.drop(col, axis=1, inplace=True)
    return df_result

def encode_categorical_values(df, col, mapping_dict):
    ''' 
    For an entire Pandas dataframe transfrom a column with categorical (string) values
    into integer values with column name <col>_enc
    NaN values are converted into -1
    
    INPUT
    df - Pandas dataframe 
    col - Column name within dataframe
    mapping_dict - mapping of string values to integer values
    
    
    OUTPUT
    df_result - Dataframe with encoded categorical column col
    '''   

    # Encode the column col using the mapping dict and name it <col>_enc
    df[col + '_enc'] = df[col].map(mapping_dict).fillna(-1).astype(int)
    
    return df
   
    
