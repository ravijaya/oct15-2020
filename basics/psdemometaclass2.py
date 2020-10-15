class MyMeta(type):
    """meta class"""
    pass


class MyClass(metaclass=MyMeta):
    pass


class MySubClass(MyClass):
    pass

if __name__ == '__main__':
    print(type(MyMeta))
    print(type(MyClass))
    print(type(MySubClass))