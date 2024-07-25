import pandas as pd
import sys
import argparse
from tabulate import tabulate


def argp():
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group()
    group.add_argument("-c", "--count", type=str, help="mh -c <cmd>")
    group.add_argument("-t", "--top", type=int, help="mh -t <num>")
    group.add_argument("-d", "--date", type=str, help="mh -d <date>")

    args = parser.parse_args()
    
    if args.count:
        cnt(args.count)
    elif args.top and args.date:
        top(args.top, args.date)
    else:
        parser.print_help()

def cnt(q):
    df = read_parquet("~/data/parquet")
    fdf = df[df['cmd'] == q]
    cnt = fdf['cnt'].sum()
    print(f'{q} 사용 횟수는 {cnt}회 입니다.')

def top(n, date):
    df = read_parquet("~/data/parquet")
    fdf = df[df['dt'] == date]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(n)
    ddf = sdf.drop(columns=['dt'])
    print(tabulate(ddf, tablefmt="pipe", headers=["", "cmd", "cnt"]))

def read_parquet(path="~/data/parquet"):
    df = pd.read_parquet(path)
    return df
