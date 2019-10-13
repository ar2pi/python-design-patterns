import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')


class Evaluate(unittest.TestCase):
    def test_module(self):
        d1 = Database()
        d2 = Database()

        self.assertEqual(d1, d2)


if __name__ == "__main__":
    unittest.main()
