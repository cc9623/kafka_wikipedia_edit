'''
simplify given sample of data
'''

import pandas as pd
from datetime import datetime

pd.set_option("display.max_columns", 35)
df = pd.read_csv(r"/Users/shero/Downloads/de_challenge_sample_data.csv")

def introduce_variables(df):
    """
    introduce language column and timestamp in minute
    """
    # introduce binary if german
    language_german, timestamp_minute = [], []
    for index, row in df.iterrows():
        if row["meta_domain"][:2] == "de":
            language_german.append(1)
        else:
            language_german.append(0)
    df["language_german"] = language_german
    return df

df = introduce_variables(df)

# reduce to (for now) relevant info
df = df[["id", "timestamp", "language_german"]].reset_index(drop=True)
print(dict(df.iloc[[0, 1, 2, 3, 193]]))

