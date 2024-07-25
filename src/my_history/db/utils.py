import pandas as pd

def top(n, date):
    df = pd.read_parquet("~/data/parquet")
    fdf = df[df['dt'] == date]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(n)
    ddf = sdf.drop(columns=['dt'])

    r = ddf.to_string(index=False)
    return r
