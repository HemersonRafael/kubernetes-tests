import os
import pandas as pd
var_env = os.environ.get("MINHA_VAR")
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'

df = pd.read_csv(url, header=None)

df[f'{var_env}'] = df[5].apply(lambda x: x*2)

print(df.columns)

print(df.head())

print(df.shape)
