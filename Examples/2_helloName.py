import sys


def sayHello(name):
    print 'Hello', name


def main():
    if len(sys.argv) >= 2:
        name = sys.argv[1]
        name = name.capitalize() + '!'

        if name != '':
            sayHello(name)
    else:
        print 'No one to say hello to ...'

    # an interesting thing about python
    # the empty string is interpreted as false by python
    if '':
        thisFunctionDoesNotExist()
        # ... but there is no error


if __name__ == '__main__':
    main()
