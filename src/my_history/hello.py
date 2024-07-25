import pandas as pd
import argparse
import sys

def hello_msg():
    return "hello"

def cmd():
    msg = hello_msg()
    #print(msg)

#def argp():
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
        
    parser.add_argument('-s', '--scount')
    parser.add_argument('-t', '--top')
    parser.add_argument('-d', '--dt')

    args = parser.parse_args()
    print(args.scount, args.top, args.dt)

    if args.scount:
        scnt(args.scount)    
    elif args.top:
        print(f"-t => {args.top}")
        if args.dt:
            print(f"-d => {args.dt}")
        else:
            print("Error")
            parser.error("-t 옵션은 -d 옵션과 함께 사용하시오!")
    else:
        parser.print_help()

def scnt(q):
    df = pd.read_parquet("~/data/parquet")
    fdf = df[df['cmd'] == q]
    cnt = fdf['cnt'].sum()
    print(f'{q} 사용 횟수는 {cnt}회 입니다.')
