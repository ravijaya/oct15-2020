def foo(a, b, *args):
    print(a)
    print(b)
    print(args)
    print(sum((a, b) + args))


foo(11, 22)
print()

foo(1, 2, 3, 4, 5)