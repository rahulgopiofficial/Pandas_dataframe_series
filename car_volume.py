# Function to obtain car volume, group by car body and number of doors, and return mean numerics of groups
def process_cars_data(df):
    # Code here
    numeric_cols = ['carlength', 'carwidth', 'carheight', 'curbweight', 'citympg', 'price', 'carvolume']
    df['carvolume'] = df['carlength'] * df['carwidth'] * df['carheight']
    df_new = df.groupby(['carbody', 'doornumber'])[numeric_cols].mean()
    return df_new

# Input and output processing (do not edit)
from ast import literal_eval
import pandas as pd
filename = 'https://d3ejq4mxgimsmf.cloudfront.net/cars_dataset-e4f25a73abf742f294f2c20e336f3c91.csv'
df = pd.read_csv(filename)
print(process_cars_data(df).round().astype(int).iloc[literal_eval(input())])