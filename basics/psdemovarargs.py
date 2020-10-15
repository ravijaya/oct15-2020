"""variable len argument function """


def demo(*args):
    print(len(args))
    print(args)


demo()
demo(100)
demo(1, 2, 'iii', 4, 5)
print()

items = [11, 22, 33]
demo(items)
demo(*items)
print()

items = (11, 22, 33)
demo(items)
demo(*items)
print()

demo('peter')
demo(*'peter')