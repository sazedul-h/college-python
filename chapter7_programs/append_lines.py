# this program append to the existing file
def main():

    myfile = open('friends.txt', 'a')

    myfile.write('Matt\n')
    myfile.write('John\n')
    myfile.write('James\n')

    myfile.close()


main()
