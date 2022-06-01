from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def get_dummies(df, column):
    '''One Hot Encode a column using pd.get_dummies'''
    df_ex = pd.get_dummies(df[column])
    df = pd.concat([df, df_ex], axis = 1)
    df = df.drop(column, axis = 1)
    return df

def preprocess_data(df):
    '''Preprocess the dataframe by scaling numerical columns and encoding categorical columns'''
    # Numerical scaling
    minmax = MinMaxScaler()
    nums = df.describe().columns.tolist()
    for num in nums:
        df[[num]] = minmax.fit_transform(df[[num]])
    # One Hot Encoding
    one_hot_columns = ['Gender', 'Type of Travel']
    for col in one_hot_columns:
        df = get_dummies(df, col)
    # Ordinal Encoding
    ordinal_columns = ['Class', 'Customer Type']
    ordinal_map = {
        "Class":{'Business' : 2, 'Eco Plus' : 1, 'Eco': 0},
        "Customer Type": {'Loyal Customer': 1,'disloyal Customer': 0}
    }
    for col in ordinal_columns:
        df[col] = df[col].map(ordinal_map.get(col))
    # Return only the first row
    return df.iloc[[0]]
