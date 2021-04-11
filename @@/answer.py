import pandas as pd
import config
from tabulate import tabulate
from parser import write_df
from classifier import classified_write


def get_answer():
    write_df()
    classified_write()
    df = pd.read_csv(config.csv_classified)
    df = df.head(10).filter(
        ['link',
         'classified',
         'probability'],
        axis=1)
    return df


get_answer()

# return print(df.to_markdown())
# return print(tabulate(df), flush=True)
# return print(sdf, flush=True)


# news = (df.to_string(header=False,
#               index=False,
#               index_names=False).split('\n'))
# answer = [','.join(ele.split()) for ele in news]

# return print(df)

