import math

# print("sup")
# string = 'kelsey'
# upper = string.upper()
# print(upper)
# number = 5.9

# print(math.ceil(number))

# print('k' in string)

# house = 1000000000
# good_credit = False
# bad_credit = True

# if good_credit:
#     house = house * .10
# if bad_credit:
#     house = house * .20

# print(house)

# comparison problem

# name = len(input('what is your name?'))

# if name <= 3:
#     print('sorry, your name is too short')
# elif name <=50:
#     print('you entered the perfect name')

# weight = int(input('what is your weight?'))

# weight_type = input('(L)bs or (k)g? ')
# lower_case = weight_type.lower()

# print(lower_case)

# is_kilo = 'k' in lower_case
# is_pounds = 'l' in lower_case

# if is_kilo:
#     print(f'you are {weight} kilos')
# if is_pounds:
#     print(f'you are  {weight} pounds')

# Car game:

user_command = ''


while user_command.lower() != 'quit':
    user_command = input('what is your command ')
    if user_command.lower() == 'start':
        print('vroom....car started')
    elif user_command.lower() == 'stop':
        print('errrrrr stop car')
    elif user_command.lower() == 'quit':
        print('goodbye')
else:
    print('you quit')




