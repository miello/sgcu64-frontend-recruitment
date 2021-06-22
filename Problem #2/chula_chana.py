menu_seperator = '-----------------------------------------------------------------'
locationList = ['Mahamakut Building', 'Sara Phra Kaew', 'CU Sport Complex', 'Sanum Juub', 'Samyan Mitr Town']
peopleCountLocation = dict()
phoneLocation = dict()

def peopleCountPage():
    print('Current Population')
    for idx, location in enumerate(locationList):
        peopleCount = peopleCountLocation[location]
        print(f'  {idx + 1}. {location}: {peopleCount}')

def checkOutPage():
    pass

def checkInPage():
    pass

def main():
    initializeDatabase()
    while(True):
        print('Welcome to Chula Chana!!!')
        print('Available commands:')
        print('  1. Check in user')
        print('  2. Check out user')
        print('  3. Print people count')
        print('  4. Exit')

        command = input('Please input any number: ')

        print(menu_seperator)
        try:
            command = int(command)
        except:
            print('Invalid type of input')
            print(menu_seperator)
            continue

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
        print(menu_seperator)

def initializeDatabase():
    for location in locationList:
        peopleCountLocation[location] = 0

main()