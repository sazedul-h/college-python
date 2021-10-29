# this prgram reads and displays the contents
# of the philosophers.txt file one line at a time
# and strips newlines.

def main():
    # open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    # read the file's contents
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    infile.close()

    print(line1)
    print(line2)
    print(line3)


main()
