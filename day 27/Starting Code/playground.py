def add(*args):
    return sum(args)


print(add(6, 2, 87, 3, 2, 3))


def calc(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calc(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
