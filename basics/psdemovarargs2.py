"""variable len argument function """


def demo(*args):
    if len(args) < 3:
        return None
    print(args[:3])


demo()
demo(100)
demo(33, 3.3, 1, 2, 'iii', 4, 5)
print()

