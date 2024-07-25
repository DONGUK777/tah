import argparse

def hello_msg():
    return "hello"

def cmd():
    msg = hello_msg()
    # print(msg)

    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-s', '--scount')           # positional argument
    parser.add_argument('-t', '--top')      # option that takes a value
    parser.add_argument('-d', '--dt')  # on/off flag

    args = parser.parse_args()
    print(args.scount, args.top, args.dt)

    if args.scount:
        print(f"-s => {args.scount}")
    elif args.top:    
        print(f"-t => {args.top}")
        if args.dt:
            print(f"-d => {args.dt}")
        else:
            print("todo ")
        
