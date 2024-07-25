import argparse

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
        print(f"-s => {args.scount}")
    elif args.top:
        print(f"-t => {args.top}")
        if args.dt:
            print(f"-d => {args.dt}")
        else:
            print("Error")
    else:
        parser.print_help()
