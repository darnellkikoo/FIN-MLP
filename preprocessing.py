from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

# def get_dummies(df, column):
#     df_ex = pd.get_dummies(df[column])
#     df = pd.concat([df, df_ex], axis = 1)
#     df = df.drop(column, axis = 1)
#     return df

def preprocess_data(df):
    # Scale Numerical Data
    minmax = MinMaxScaler()
    nums = df.describe().columns.tolist()
    for num in nums:
        df[[num]] = minmax.fit_transform(df[[num]])
    
    # One Hot Encoding -> ERROR
    df[['Gender','Type of Travel']] = df[['Gender','Type of Travel']].astype("category")
    gender_encoder = OneHotEncoder(categories=[['Female', 'Male']])
    gender = gender_encoder.fit_transform(df[['Gender']])
    type_encoder = OneHotEncoder(categories=[['Business travel', 'Personal Travel']])
    type = type_encoder.fit_transform(df[['Type of Travel']])
    print(type_encoder.categories_)
    print(type.toarray())

    
    # 1 Column -> 300 rows (Male Female)
    # Get Dummies -> Male (1/0), Female (1/0)
    # 1 Row -> column -> 

    # Ordinal Encoding
    ordinal_columns = ['Class', 'Customer Type']
    ordinal_map = {
        "Class":{'Business' : 2, 'Eco Plus' : 1, 'Eco': 0},
        "Customer Type": {'Loyal Customer': 1,'disloyal Customer': 0}
    }
    for col in ordinal_columns:
        df[col] = df[col].map(ordinal_map.get(col))
    
    return df