import re


garage = [None] * 11


def parking(license):
    matched = re.match(
        "[A-Z][A-Z][A-Z][A-Z][-][0-9][0-9][-][0-9][0-9][0-9]", license)
    is_match = bool(matched)
    if is_match is True:
        print("License plate number correct.\n")
        if license in garage:
            print("Car already in the garage.")
        else:
            print("Parking...\n")
            for i in range(len(garage) + 1):
                if garage[i] == None:
                    garage[i] = license
                    break
            print("Completed! See you soon.")
    if is_match is False:
        print("License Incorrect.")
        license = str(input(
            "Please re-enter your license plate number in ABCD-12-3456 format: "))
        parking(license)


def retrieving(license, stats):
    matched = re.match(
        "[A-Z][A-Z][A-Z][A-Z][-][0-9][0-9][-][0-9][0-9][0-9]", license)
    is_match = bool(matched)
    if is_match is True:
        if license in garage:
            print("Retrieving...\n")
            garage.remove(license)
            print("Completed! Good Bye!")
        elif stats == 0:
            print("Garage empty!")
        else:
            print("Car not in garage!")
    if is_match is False:
        print("License Incorrect.")
        license = str(input(
            "Please re-enter your license plate number in ABCD-12-3456 format: "))
        retrieving(license, stats)


def garage_stats():
    stats = 0
    for i in garage:
        if i != None:
            stats += 1
    print("Cars parked:", stats)
    return stats


def main():
    while 1:
        print("\n")
        print("Welcome to Oreoluwa's Garage!\n")
        stats = garage_stats()
        print("(1) Parking")
        print("(2) Retrieving")
        print("(3) Exit\n")
        user_option = str(input("Option: "))

        if stats < 10 and user_option == "1":
            print("Standing By...\n")
            license = str(input("Enter your license plate number: "))
            parking(license)
        elif stats == 10 and user_option == "1":
            print("Garage Full. Please come back later.")
        elif user_option == "2":
            print("Standing By...\n")
            license = str(input("Enter your license plate number: "))
            retrieving(license, stats)
        elif user_option == "3":
            print("Good bye.\n")
            break
        elif user_option != "1" or user_option != "2" or user_option != "3":
            print("Incorrect option. Try again.")


main()
