# Initialize the constant variable and database
menu_seperator = '-----------------------------------------------------------------'

# Represent the list of available location
locationList = ['Mahamakut Building', 'Sara Phra Kaew', 'CU Sport Complex', 'Sanum Juub', 'Samyan Mitr Town']

# The database for storing number of people in location
# [str] -> int
peopleCountLocation = dict()

# The database for mapping phone number to location
# [str] -> str
phoneLocation = dict()

'''
Initialize the database by inserting each key (location) into database with default value zero
Input:
    None
Return:
    None
'''
def initializeDatabase():
    for location in locationList:
        peopleCountLocation[location] = 0

'''
The method that used for showing how many people in each location
Input:
    None
Return:
    None
'''
def peopleCountPage():
    print('Current Population')
    for idx, location in enumerate(locationList):
        # Get number of people in location
        peopleCount = peopleCountLocation[location]
        print(f'  {idx + 1}. {location}: {peopleCount}')
'''
The method that used for displaying check out page 
which need to input the phone number
Input:
    None
Return:
    None
'''
def checkOutPage():
    print('Check out')
    phoneNumber = input('Enter phone number: ')

    # If phone number key is not in phoneLocation 
    # then add the new phone number
    if phoneNumber not in phoneLocation:
        phoneLocation[phoneNumber] = ''
    
    msg = None

    # Case: Not check in
    if phoneLocation[phoneNumber] == '':
        msg = 'You have not checked in yet'

    # Case: Check out from location
    else:
        oldPlace = phoneLocation[phoneNumber]

        # Decrease people counter
        peopleCountLocation[oldPlace] -= 1

        # Reset the location of phone number
        phoneLocation[phoneNumber] = ''
        
        msg = f'Check out from {oldPlace}'

    print(msg)

'''
The method that used for displaying check in page 
which need to input the phone number and index of location
Input:
    None
Return:
    None
'''
def checkInPage():
    print('Check in')
    # Phone number input
    phoneNumber = input('Enter phone number: ')
    
    for idx, location in enumerate(locationList):
        print(f'  {idx + 1}. {location}')

    place = None

    # Loop until get the valid index input
    while True:
        try: 
            place = input('Select the place: ')
            place = int(place)
            if place < 1 or place > len(locationList):
                raise Exception()
            break
        except:
            print('Invalid index of place. Please try again.')
    
    # Get name of place by index
    nameOfPlace = locationList[place - 1]
    msg = ''

    # If phone number key is not in phoneLocation 
    # then add the new phone number
    if phoneNumber not in phoneLocation:
        phoneLocation[phoneNumber] = ''
    
    # Case: Not check in yet
    if phoneLocation[phoneNumber] == '':
        phoneLocation[phoneNumber] = nameOfPlace
        peopleCountLocation[nameOfPlace] += 1
        msg = f'Check in at {nameOfPlace}'
    
    # Case: The location which will check in is equal to current check in location
    elif phoneLocation[phoneNumber] == nameOfPlace:
        msg = f'You have already checked in at {nameOfPlace}'
    
    # Case: The location which will check in is not equal to current check in location
    else:
        # Get the current location
        oldPlace = phoneLocation[phoneNumber]

        # Change to new location
        phoneLocation[phoneNumber] = nameOfPlace

        # Decrease number of people of past location
        peopleCountLocation[oldPlace] -= 1

        # Increase number of people of new location
        peopleCountLocation[nameOfPlace] += 1

        msg = f'Check out from {oldPlace} and check in at {nameOfPlace}'

    print(msg)

'''
The main program
Input: 
    None
Return: 
    None
'''
def main():
    # Initialize the database
    initializeDatabase()

    # Loop the menu
    while(True):
        print('Welcome to Chula Chana!!!')
        print('Available commands:')
        print('  1. Check in user')
        print('  2. Check out user')
        print('  3. Print people count')
        print('  4. Exit')

        command = input('Please input any number: ')

        print(menu_seperator)

        # Check the error from parsing
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
            print('Exit program')
            exit(0)
        else:
            print('Invalid number')
        print(menu_seperator)

# Run the main program
main()