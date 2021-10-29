# this program uses the for loop to read
# all the values in the sales.txt file.

def main():
    sales_file = open('sales.txt', 'r')

    for line in sales_file:
        amount = float(line)

        print(format(amount, '.2f'))

    sales_file.close()


main()
