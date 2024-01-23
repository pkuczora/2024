import random
global guests
global name
global guest_number
global equal_split
global total_bill
global unlucky_guests
global lucky_name

guests = {}


def guest_list():
    global guests
    global name
    global guest_number
    global equal_split
    global total_bill
    global unlucky_guests
    global lucky_name
    guest_number = int(input("Enter the number of friends joining (including you):"))
    if guest_number == 0 or guest_number < 0:
        print("No one is joining for the party")
        exit()
    for person in range(0, guest_number):
        name = str(input("Enter the name of every friend (including you), each on a new line:"))
        guests[name] = 0
    check_lucky()


def check_lucky():
    global guests
    global name
    global guest_number
    global equal_split
    global total_bill
    global unlucky_guests
    global lucky_name
    total_bill = int(input("Enter the total bill value:"))
    lucky = str(input('Do you want to use the "Who is lucky?" feature? Write Yes/No:'))
    if lucky == 'Yes':
        lucky_name = random.choice(list(guests.keys()))
        print(f"""{lucky_name} is the lucky one""")
        lucky_splitting()
    else:
        print("No one is going to be lucky")
        equal_splitting()


def equal_splitting():
    global guests
    global name
    global guest_number
    global equal_split
    global total_bill
    global unlucky_guests
    equal_split = round(total_bill / guest_number, 2)
    for name in guests:
        guests[name] = equal_split
    print(guests)


def lucky_splitting():
    global guests
    global name
    global guest_number
    global equal_split
    global total_bill
    global unlucky_guests
    global lucky_name
    for name in guests:
        if name == lucky_name:
            guests[name] = 0
        else:
            equal_split = round(total_bill / (guest_number - 1))
            guests[name] = equal_split
    print(guests)


guest_list()
