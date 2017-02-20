print "Welcome to our menu!"

menu_list = {}

while True:
    dish = raw_input("Please, choose your dish: ")
    print "Your dish is: " + dish
    price = raw_input("Price for '%s' : " % dish)
    menu_list(dish) = price

    new = raw_input("Would you like to enter a new dish? (yes/no) ")

    if new == "No":
        break

    print "menu_list: '%s' " % menu_list

    with open("menu_list.txt", "w+") as menu_list_file:
        for dish in menu_list:
            menu_list_file.write("%s, %s EUR\n" % (dish, menu_list(dish)))

    print "Thanks!"


