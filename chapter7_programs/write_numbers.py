# This program demostrates how numbers
# mist be converted to strints before they
# are weitten to a text file.

def main():
    # open a file called numbers.txt
    outfile = open('numbers.txt', 'w')

    # get three numbers from the user
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter another number: '))

    # write the numbers to the file while converting to str
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    outfile.close()


main()
