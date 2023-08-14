# Tuple items are ordered, unchangeable, and allow duplicate values.

tuple_with_one_item = ("item",)

tuple2 = tuple(("x", "y", "z"))

tuple1 = ("Mercedes", "BMW", "Volvo", 1, True)

len(tuple1) # 5

type(tuple1) # <class 'tuple'>

1 in tuple1 # True
99 not in tuple1 # True

tuple1 += tuple2
tuple1 # ('Mercedes', 'BMW', 'Volvo', 1, True, 'x', 'y', 'z')

del tuple2

# Unpacking a Tuple
(m, b, w, *others, x, y, z) = tuple1
m # Mercedes
b # BMW
w # Volvo
others # [1, True]
x # x
y # y
z # z

tuple1.index(1) # 3

tuple1.count("BMW") # 1
