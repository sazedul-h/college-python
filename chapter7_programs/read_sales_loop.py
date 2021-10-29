# this program reads all of the values in
# the sales.txt

def main():
    # open the file
    sales_file = open('sales.txt', 'r')

    # read the first line from the file, but
    # don't convert to a number yet. we still
    # need to test for an empty string

    line = sales_file.readline()

    # as long as empty string is not returned
    # from readline, continue processing.

    while line != '':
        # convert line to float
        amount = float(line)

        # format and display the amount
        print(format(amount, '.2f'))

        # read the next line.

        line = sales_file.readline()

    sales_file.close()


main()
