def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """
    if(num1 < num2 and num2 < num3):
        minval = num1
        if(num2 < num3):
            median = num2
            maxval = num3
        else:
            median = num3
            maxval = num2
            

    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
