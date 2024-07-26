import pandas as pd
from tabulate import tabulate

def read_data(path="~/data/parquet"):
    df = pd.read_parquet(path)
    return df

def top(cnt, dt, pretty=False):
    df = read_data()
    fdf = df[df['dt'] == dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(cnt)
    ddf = sdf.drop(columns=['dt'])

    if pretty:
        return tabulate(ddf,
                 headers=['cmd', 'cnt'], tablefmt='pipe')
    else:
        return ddf.to_string(index=False)


def count(query):
    df = read_data()
    fdf = df[df['cmd'].str.contains(query)]
    cnt = fdf['cnt'].sum()
    return cnt
