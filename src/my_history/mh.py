import pandas as pd
import sys
import argparse

#INPUT = sys.argv[1]

def argp():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--count", action="store_true", help="mh -c <cmd>")
    group.add_argument("-t", "--top", action="store_true", help="mh -t <YYYY-MM-DD>")

    args = parser.parse_args()
    
    if args.count:
        abc(args.count)
    elif args.top:
        xyz(args.top)
    else:
        print("사용법 확인")

def cnt(n, date):
    #df = read_parquet()
    df = read_parquet("~/data/parquet")
    fdf = df[df['dt'] == date]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(n)
    ddf = sdf.drop(columns=['dt'])
    print(ddf.to_string(index=False))

def read_parquet(path="~/tmp/history.parquet"):
    df = pd.read_parquet(path)
    return df

def query(q):
    q = sys.argv[1]
    i = cnt(q)
    print(f'{q} 사용 횟수는 {i}회 입니다.')
