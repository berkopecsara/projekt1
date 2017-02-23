import random
def loto():
    print ("Welcome to the Lottery numbers generator.")
    vprasanje = raw_input("Please enter how many random numbers would you like to have: ")

    try:
        stevilo = int(vprasanje)
        print loto(stevilo)
    except ValueError:
        print "Please enter a number."

    print "END."

if __name__ == "__main__":
    loto()

