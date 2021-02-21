#!/usr/bin/env python3
# descriptive_statistics.py

"""
This script calculates the statistics of the values in a list of numbers
"""

# Import modules
import sys
import math

def mean(num):
    """
    Calculates the mean of a list of numbers
    """
    return sum(num) / len(num)

def variance(num):
    """
    Calculates the variance of a list of numbers
    """
    # Number of elements
    element = len(num)

    # Initiate result variable
    res = 0

    # Loop through the list
    for i in range(element):
        res += (num[i] - mean(num)) ** 2

    # Calculate and return the variance
    return (1 / (element - 1)) * res

def standard_deviation(num):
    """
    Calculates the standard deviation of a list of numbers
    """
    return math.sqrt(variance(num))

def median(num):
    """
    Calculates the median of a list of numbers
    """
    # Number of elements
    elements = len(num)

    # Sorted list
    num.sort()

    # Initiate result variable
    result = 0

    # Median conditions
    if elements % 2 == 0:
        med1 = num[elements//2]
        med2 = num[elements//2 - 1]
        result = (med1 + med2) / 2
    else:
        result = num[elements//2]

    return result

def descriptive_statistics(filename, column_to_parse):
    """
    Calculates the statistics of the values in a file and prints them out
    """
    # Initiate the list for the data in column_to_parse
    numbers = []

    # Initiate the list for the valid numbers
    num = []

    # Open and read the file to add data to numbers
    with open(filename, 'r') as infile:
        for line in infile:
            try:
                numbers.append(line.split("\t")[column_to_parse])
            except IndexError:
                line = "Exiting: There is no valid 'list index' in column "
                print(line + str(column_to_parse) + " in line 1 in file: " + filename)

    # Store numbers in the list num
    for i, val in enumerate(numbers):
        try:
            num.append(float(val))
        except TypeError:
            string = "Skipping line number "
            num.append(0)
            print(string + str(i) + " : could not convert string to float: " + numbers[i])


    # Valid numbers
    valnum = [i for i in num if math.isnan(i) is False]

    # Average
    try:
        avrg = mean(valnum)
    except TypeError:
        error = "Error: There were no valid number(s) in column "
        print(error + str(column_to_parse) + " in file: " + filename)

    # Variance
    try:
        var = variance(valnum)
    except ZeroDivisionError:
        var = 0

    # Standard Deviation
    try:
        std_dev = standard_deviation(valnum)
    except ZeroDivisionError:
        std_dev = 0

    print(4*"\n")

    print("Column: " + str(column_to_parse))

    print(8*"\n")

    # Print Count line
    print('{:<8}{:.{prec}} = {:.{prec}f}'.format("Count", '', len(num), prec=3))

    # Print ValidNum line
    print('{}{:.{prec}} = {:.{prec}f}'.format('ValidNum', "", len(valnum), prec=3))

    # Print Average line
    print('{:<8}{:.{prec}} = {:.{prec}f}'.format('Average', "", avrg, prec=3))

    # Print Maximum line
    print('{:<8}{:.{prec}} = {:.{prec}f}'.format('Maximum', "", max(valnum), prec=3))

    # Print Minimum line
    print('{:<8}{:.{prec}} = {:.{prec}f}'.format('Minimum', "", min(valnum), prec=3))

    # Print Variance line
    print('{:<8}{:.{prec}} = {:.{prec}f}'.format('Variance', "", var, prec=3))

    # Print Standard Deviation line
    print('{:<8}{:.{prec}} = {:.{prec}f}'.format('Std Dev', "", std_dev, prec=3))

    # Print Median line
    print('{:<8}{:.{prec}} = {:.{prec}f}'.format('Median', "", median(valnum), prec=3))

# Main function
if __name__ == "__main__":

    # Number of arguments
    A = len(sys.argv) - 1

    # Check if there are 2 arguments
    if A < 2:
        raise Exception("This script requires 2 arguments: a file name and a column number")

    # Filename
    F = sys.argv[1]

    # Column number
    C = int(sys.argv[2])

    # Print output
    print(descriptive_statistics(F, C))
