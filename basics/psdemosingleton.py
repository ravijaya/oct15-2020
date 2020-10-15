"""demo for the metaclass to implement the singleton pattern"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    pass


if __name__ == '__main__':
    s1 = SingletonClass()
    print(s1)
    s2 = SingletonClass()
    print(s2)