coffees = [4, 3, 2]


def barista(orders):
    time, s, clean = 0, 0, 2
    for i, v in enumerate(sorted(orders)):
        s += v
        time += clean*i + s
    return time


print("The order will be done in "+str(barista(coffees))+" min")
