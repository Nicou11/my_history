import pandas as pd
import sys
import argparse

#INPUT = sys.argv[1]

def argp():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--count", type=str, action="store_true", help="mh -c <cmd>")
    group.add_argument("-t", "--top", type=int,action="store_true", help="mh -t <num>")
    group.add_argument("-d", "--date", type=str,action="store_true", help="mh -d <date>")

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
    ddf = sdf.drop(columns=['dt']).to_string(index=False)
    print(ddf)

def read_parquet(path="~/tmp/history.parquet"):
    df = pd.read_parquet(path)
    return df
