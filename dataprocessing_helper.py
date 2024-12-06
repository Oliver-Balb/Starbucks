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
    encoded_df = df[col].apply(lambda x: pd.Series(1, index=x)).fillna(0).astype(int)
    # Add prefix to the new columns
    encoded_df = encoded_df.add_prefix(col+'_')
    
    # Replace old column by new one-hot-encoded columns
    df_result = df.join(encoded_df)
    df.drop(col, axis=1, inplace=True)
    return df_result


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
