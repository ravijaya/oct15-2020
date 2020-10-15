class Foo:
    def __call__(self, *args, **kwargs):
        print(self, 'am called')


if __name__ == '__main__':
    foo = Foo()
    print(foo)
    foo()