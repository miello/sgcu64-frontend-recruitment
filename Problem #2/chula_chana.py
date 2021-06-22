def peopleCountPage():
    pass

def checkOutPage():
    pass

def checkInPage():
    pass

def main():
    while(True):
        print('Welcome to Chula Chana!!!')
        print('Available commands:')
        print('  1. Check in user')
        print('  2. Check out user')
        print('  3. Print people count')
        print('  4. Exit')
        command = input('Please input any number: ')
        try:
            command = int(command)
            if command == 1:
                checkInPage()
            elif command == 2:
                checkOutPage()
            elif command == 3:
                peopleCountPage()
            elif command == 4:
                exit(0)
            else:
                print('Invalid number')
        except:
            print('Invalid type of input')

main()