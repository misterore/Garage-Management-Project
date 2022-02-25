import re


garage = [None] * 11


def none_checker():
    i = 0
    while i <= len(garage):
        if garage[i] is None:
            return i, True
        i += 0


def parking(license):
    matched = re.match(
        "[A-Z][A-Z][A-Z][A-Z][-][0-9][0-9][-][0-9][0-9][0-9]", license)
    is_match = bool(matched)
    if len(license) != 12:
        is_match = False

    k = 0
    j = 0

    if is_match is True:
        print("\nLicense plate number correct.\n")
        while j < len(garage):
            if license == garage[j]:
                print("Car already in the garage.")
                break
            j += 1
            while k < len(garage):
                if garage[k] == None:
                    print("Parking...\n")
                    garage[k] = license
                    print("Completed! See you soon.")
                    break
                k += 1
            break
    if is_match is False:
        print("\nLicense Incorrect.\n")
        license = str(input(
            "Please re-enter your license plate number in ABCD-12-3456 format: "))
        parking(license)


def retrieving(license, stats):
    matched = re.match(
        "[A-Z][A-Z][A-Z][A-Z][-][0-9][0-9][-][0-9][0-9][0-9]", license)
    is_match = bool(matched)
    if len(license) != 12:
        is_match = False
    i = 0

    if is_match is True:
        print("\nLicense plate number correct.\n")
        while i < (len(garage)):
            if stats == 0:
                print("Garage empty!")
                break
            if license == garage[i]:
                print("Retrieving...\n")
                garage.remove(license)
                print("Completed! Good Bye!")
                break
        else:
            print("Car not in garage!")
        if stats == 0:
            print("Garage empty!")
    if is_match is False:
        print("\nLicense Incorrect.\n")
        license = str(input(
            "Please re-enter your license plate number in ABCD-12-3456 format: "))
        retrieving(license, stats)


def garage_stats():
    stats = 0
    i = 0
    while i < len(garage):
        if garage[i] != None:
            stats += 1
        i += 1
    print("Cars parked:", stats)
    return stats


def cars():
    i = 0
    cars_list = ''
    print("\nCars in garage:")
    while i < len(garage):
        if garage[i] != None:
            cars_list += garage[i] + ('\n')
        i += 1
    print(cars_list)


def main():

    while 1:
        print("\n")
        print("Welcome to Oreoluwa's Garage!\n")
        stats = garage_stats()
        print("\n(1) Parking")
        print("(2) Retrieving")
        print("(3) Exit\n")
        user_option = str(input("Option: "))

        if stats < 10 and user_option == "1":
            print("\nStanding By...\n")
            license = str(
                input("Enter your license plate number: ").strip())
            parking(license)
            cars()
        elif stats == 10 and user_option == "1":
            print("Garage Full. Please come back later.")
        elif user_option == "2":
            print("\nStanding By...\n")
            license = str(
                input("Enter your license plate number: ").strip())
            retrieving(license, stats)
            cars()
        elif user_option == "3":
            print("Good bye.\n")
            break
        elif user_option != "1" or user_option != "2" or user_option != "3":
            print("Incorrect option. Try again.")


main()
