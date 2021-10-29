# this prgram reads and displays the contents
# of the philosophers.txt file.

def main():
    # open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    # read the file's contents
    file_contents = infile.read()

    infile.close()

    print(file_contents)


main()
