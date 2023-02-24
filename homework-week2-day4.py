#!/usr/bin/python

#Exercise 1: Interactive Address Book

def run():
    print("\n")
    print("#"*50)
    print("######## Welcome to the Address Database! ########")
    print("#"*50)
    address_book = {}
    user_input = True

    while user_input:
        name = input("\nPlease enter a name: ").title()
        address = input(f"What is {name}'s address? ").title()
        address_book[name] = address
        print(f"{name}'s address saved as {address}.")
        if input("\nMake another entry? (y/n) ").lower() == "n":
            if input("\nThank you for your input!\
                    \nWould you like to view your address book before you go? (y/n) ").lower() == "n":
                print("\nGoodbye!")
                user_input = False    
            else:
                max_length = 0
                for k, v, in address_book.items():
                    entry_length = len(k) + len(v) + 7
                    if entry_length > max_length:
                        max_length = entry_length
                print("\n")
                print("#"*max_length)
                for k, v in address_book.items():
                    entry_length = len(k) + len(v) + 7
                    if entry_length == max_length:
                        print(f"# {k} - {v} #")
                    else:
                        print(f"# {k} - {v} " + " "*(max_length - entry_length) + "#")
                print("#"*max_length)
                print("\nGoodbye!")
                user_input = False
run()

#Exercise 2: Finding the common meeting times in an arbitrary number of individual schedules 

person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']
person5 = ['22:00']

def meeting_times(*args):
    common_set = set()
    for schedule in args:
        for time in schedule:
            common_set.add(time)
    for schedule in args:
        common_set &= set(schedule)
    if common_set:
        return common_set
    return 0                        # Return 0 if there are no common times
