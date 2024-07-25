import pandas as pd

def read_data(path="~/data/parquet"):
    df = pd.read_parquet(path)
    return df

def top(n, date):
    df = read_data()
    fdf = df[df['dt'] == date]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(n)
    ddf = sdf.drop(columns=['dt'])

    r = ddf.to_string(index=False)
    return r

def count(query):
    df = read_data()
    fdf = df[df['cmd'] == query]
    cnt = fdf['cnt'].sum()
    print(f'{q} 사용 횟수는 {cnt}회 입니다.')
