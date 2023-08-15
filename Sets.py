# Set items are unordered, unchangeable, and do not allow duplicate values.
# Set items are unchangeable, but you can remove items and add new items.

set1 = {"Istanbul", "Ankara", 1, True, 0, False, 99}

set1 # {0, 1, 99, 'Istanbul', 'Ankara'}

len(set1) # 5

type(set1) # <class 'set'>

# The set() Constructor
set2 = set((1, 2, 3, "x", "y", "z"))

for x in set1:
    print(x)
"""
0
Ankara
1     
99    
Istanbul
"""

# .add() method
set1.add("Izmir")
set1 # {0, 1, 99, 'Izmir', 'Istanbul', 'Ankara'}

# .update() method
set1.update({88, 77})
set1 # {0, 1, 99, 'Istanbul', 'Ankara', 88, 'Izmir', 77}

set1.update([66, 55])
set1 # {0, 1, 66, 'Ankara', 77, 88, 99, 'Izmir', 'Istanbul', 55}

# .remove() method
set1.remove(99)
set1.remove(88)
set1.remove(77)

# .discard() method
set1.discard(66)
set1.discard(55)

set1.discard(9999) # will not raise an error

"""
If the item to remove does not exist, remove() will raise an error.
If the item to remove does not exist, discard() will NOT raise an error.
"""

set1 # {0, 1, 'Istanbul', 'Ankara', 'Izmir'}

# .pop() method
# this method will remove a random item

# .clear() and del
set1.clear()
del set1

set1 = {4, 5, 6}
set2 = {7, 8, 9}

# .union() method
set3 = set1.union(set2)
set3 # {4, 5, 6, 7, 8, 9}

# .update() method
set1.update(set2)
set1 # {4, 5, 6, 7, 8, 9}

# .intersection_update() method
set2 # {7, 8, 9}
set1 # {4, 5, 6, 7, 8, 9}
set1.intersection_update(set2)
set1 # {7, 8, 9}

# symmetric_difference_update()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)
set1 # {1, 2, 5, 6}

# .issubset() and .issuperset()
set1 = {3, 4}
set2 = {3, 4, 5, 6}
set1.issubset(set2) # True
set2.issuperset(set1) # True

# .isdisjoint()
set1 = {1, 2}
set2 = {3, 4, 5, 6}
set1.isdisjoint(set2) # True

# .difference_update()
set1 = {3, 4}
set2 = {3, 4, 5, 6}
set2.difference_update(set1)
set2 # {5, 6}
