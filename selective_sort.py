'''Week 10 Checkpoint A - Selection Sorting'''
'''Selection sorting looks for largest number to put it at the end of list'''
"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.
Sorts a list of numbers.
"""


def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    num_length = len(numbers)
    # Loop goes through the whole list of numbers
    for number in range(num_length):
        max_number = number

        # Looks for next number in array
        for second_number in range(number + 1, num_length):
            # compares next number with largest
            if numbers[second_number] < numbers[max_number]:
                # updates largest number
                max_number = second_number

        # temporary storage variable to be enchanged later
        temporary_storage = numbers[number]
        numbers[number] = numbers[max_number]
        numbers[max_number] = temporary_storage

    return numbers


def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers


def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)


def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)


if __name__ == "__main__":
    main()

# reading: 45 min
# checlpoint: 30 min