# class TestClass:
#     pass

TestClass = type('TestClass', (), {})
TestClass = type('TestClass', (), {'arch': 'x98_65', 'version': 2.2})


if __name__ == '__main__':
    print(TestClass)
    my_test = TestClass()
    print(my_test.arch)
    print(my_test.version)
    print()
    print(type(my_test))
    print(type(TestClass))
    print(type(type))