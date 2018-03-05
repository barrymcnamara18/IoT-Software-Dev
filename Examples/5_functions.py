# global value to check
x = 4


def is_even(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """

    # we get here the global variable
    print 'value to check is', x

    # here we use the parameter i
    return not(i % 2)


def main():
    print is_even(x)


if __name__ == '__main__':
    main()