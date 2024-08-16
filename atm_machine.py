'''
This script simulates a basic ATM transaction,
allowing users to check their balance, withdraw, and deposit funds.
'''
import time

print('Please insert your CARD')

time.sleep(5)

PAASWORD = 1234

pin = int(input('Enter your ATM PIN '))

BALANCE = 5000

if pin == PAASWORD:

    while True:

        print('''
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            '''
            )

        try:
            option = int(input('Please enter your choice '))
        except ValueError:
            print('Please enter valid option ')

        if option == 1:
            print(f'Your current balance is {BALANCE}')

            print('=================================================')
            print('=================================================')

        if option == 2:

            withdraw_amount = int(input('Please enter withdraw amount '))

            BALANCE = BALANCE - withdraw_amount

            print(f'{withdraw_amount} is debited fromm your account')

            print(f'your current balance is {BALANCE}')

            print('=================================================')
            print('=================================================')

        if option == 3:

            deposit_amount = int(input('Please enter deposit amount '))

            BALANCE = BALANCE + deposit_amount

            print(f'{deposit_amount} is credited to your account')

            print(f'Your current balane is {BALANCE}')

            print('=================================================')
            print('=================================================')

        if option == 4:
            break


else:
    print('Wrong PIN!! Please try again')
