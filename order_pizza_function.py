

menu = {
    's': 40,
    'm': 50,
    'l': 60,
    'xl': 70,

}

drink1 = {
    'cola': 10,
    'fuze tea': 8,
    'sprite': 11,
    'fanta': 9,

}


city = {
    'b': 20,
    'x': 60,

}

sum = 0

d = 0
order = 0


def order1():
    global sum
    order = input("Choose the pizza size:")
    # order = choice()
    sum = sum + menu[order]



def amount():
    global sum
    quan = int(input("How much pizza do you want to order?"))
    sum = sum * quan
    print(sum)


def extra1():
    global sum
    extra = input("do you want extra in your pizza?")
    if extra == "y":
        sum = sum + 2
        print(sum)
    else:
        print("something is wrong")


def drink():
    global sum
    order2 = input("do you want some drink?Y/N")
    if order2 == "y":
        d = input("which drink do you want?")
        sum = sum + drink1[d]
        print(sum)
    else:
        print("something is wrong")


def location():
    global sum
    city2 = input("do you want delivery?")
    if city2 == "y":
        place = input("choose B if you live in beer sheva:")
        sum = sum + city[place]
        print(sum)

def calc():
    from utiles import playgame

    global d
    global sum
    d = sum - (sum * (playgame() / 100))
    print("the new price will be", d)



def exitance():
    con = input("do you want to continue? ")
    if con == "n":
        exit()




