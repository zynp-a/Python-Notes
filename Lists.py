# List items are ordered, changeable, and allow duplicate values.

789 in [123, 456, 789] # True
999 not in [123, 456, 789] # True

list1 = ["hello", 999, True]

# list() constructor
list1 = list(("hello", 999, True))

# len()
len(list1) # 3

# type()
type(list1) # <class 'list'>

list1[0] # hello
list1[-1] # True

list1[0:2] # ['hello', 999]
list1[1:] # [999, True]
list1[:1] # ['hello']

list1[-3:-1] # ['hello', 999]

list1[2] = False
list1 # ['hello', 999, False]

# .insert method
list1.insert(2, True)
list1 # ['hello', 999, True, False]

# .append() method
list1.append(None)
list1 # ['hello', 999, True, False, None]

# .remove() method
list1.remove(True)
list1.remove(False)
list1 # ['hello', 999, None]

# .extend() method
list1.extend([True, False])
list1 # ['hello', 999, None, True, False]

list1.extend((123, 987))
list1 # ['hello', 999, None, True, False, 123, 987]

# .pop() method
list1.pop(0)
list1.pop(1)
list1 # [999, True, False, 123, 987]

list1.pop()
list1.pop()
list1 # [999, True, False]

# del keyword
del list1[0]
list1 # [True, False]

# .clear() method
list1.clear()
list1 # []

del list1

#################### LOOP THROUGH A LIST ####################

list1 = ["BMW", "Mercedes", "Volvo"]

for x in list1:
    print(x)
"""
BMW
Mercedes
Volvo
"""

for x in range(len(list1)):
    print(list1[x])
"""
BMW
Mercedes
Volvo
"""

# List Comprehension
[print(x) for x in list1]
"""
BMW
Mercedes
Volvo
"""

[x for x in list1 if "e" not in x] # ['BMW', 'Volvo']

# .sort() method
list1.sort(reverse=True) # ['Volvo', 'Mercedes', 'BMW']

# .reverse() method
list1.reverse()
list1 # ['BMW', 'Mercedes', 'Volvo']

# .copy() method
list2 = list1.copy()
list2 # ['BMW', 'Mercedes', 'Volvo']

list3 = list1 + list2
list3 # ['BMW', 'Mercedes', 'Volvo', 'BMW', 'Mercedes', 'Volvo']

# .count() method
list3.count("BMW") # 2

# .index() method
list3.index("Mercedes") # 1
