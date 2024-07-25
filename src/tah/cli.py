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
        # todo 명령어 카운트
    elif args.top:    
        print(f"-t => {args.top}")
        if args.dt:
            print(f"-d => {args.dt}")
            # todo 특정 날짜의 명령어 top n개 출력
        else:
            print("todo-에러나 안내 메시지 주기 ")
    else:
        # todo - (scount랑 top도 없어서 안내 메시지를 준다 -> 사용법을 알려준다.)
        parser.print_help()

    
