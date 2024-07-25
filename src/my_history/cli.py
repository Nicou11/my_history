import pandas as pd
import sys
import argparse

#INPUT = sys.argv[1]


def sort(n, date):
    #df = read_parquet()
    df = read_parquet("~/data/parquet")
    fdf = df[df['dt'] == date]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(n)
    ddf = sdf.drop(columns=['dt'])
    print(ddf.to_string(index=False))


def cnt(q): 
    df = read_parquet()
    fdf = df[df['cmd'].str.contains(q)]
    cnt = fdf['cnt'].sum()
    return cnt


def read_parquet(path="~/tmp/history.parquet"):
    df = pd.read_parquet(path)
    return df


def query():
    q = sys.argv[1]
    i = cnt(q)
    print(f'{q} 사용 횟수는 {i}회 입니다.')
