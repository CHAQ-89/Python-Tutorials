

def money_convert(usd):
    vnd = usd * 23
    return vnd

def print_msg(usd, vnd):
    print(f"{usd} USD = {vnd} VND")

def main():
    while True:
        try:
            usd = float(input('Enter money: '))
            vnd = money_convert(usd)
            print_msg(usd, vnd)
        except:
            print('You must enter a digit value !')
            continue
        break

if __name__ == '__main__':
    main()