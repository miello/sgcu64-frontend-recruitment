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
    print('Check in')
    phoneNumber = input('Enter phone number: ')
    
    for idx, location in enumerate(locationList):
        print(f'  {idx + 1}. {location}')

    place = None
    while True:
        try: 
            place = input('Select the place: ')
            place = int(place)
            if place < 1 or place > len(locationList):
                raise Exception()
            break
        except:
            print('Invalid index of place. Please try again.')
    
    nameOfPlace = locationList[place - 1]
    msg = ''

    if phoneNumber not in phoneLocation:
        phoneLocation[phoneNumber] = ''
    
    if phoneLocation[phoneNumber] == '':
        phoneLocation[phoneNumber] = nameOfPlace
        peopleCountLocation[nameOfPlace] += 1
        msg = f'You check in at {nameOfPlace}'
    elif phoneLocation[phoneNumber] == nameOfPlace:
        msg = f'You have already checked in at {nameOfPlace}'
    else:
        oldPlace = phoneLocation[phoneNumber]
        phoneLocation[phoneNumber] = nameOfPlace

        peopleCountLocation[oldPlace] -= 1
        peopleCountLocation[nameOfPlace] += 1

        msg = f'Check out from {oldPlace} and check in at {nameOfPlace}'

    print(msg)

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