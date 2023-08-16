# __iter__() and __next__()

# Lists, tuples, dictionaries, and sets are all iterable objects.

my_tuple = ("x", "y", "z")
my_iterator = iter(my_tuple)
print(next(my_iterator))  # x
print(next(my_iterator))  # y
print(next(my_iterator))  # z


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_class = MyNumbers()
my_iter = iter(my_class)
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # 4
