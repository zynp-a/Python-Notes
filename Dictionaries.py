# key:value
# Dictionary items are ordered, changeable, and does not allow duplicates.

dict1 = {"brand": "Porsche", "model": "911 Classic", "year": 1964}

len(dict1)  # 3

type(dict1)  # <class 'dict'>

# The dict() Constructor
dict2 = dict(first_name="Zeynep", last_name="Akkaya")

dict2["first_name"]  # Zeynep
dict2["last_name"]  # Akkaya

# .get() method
dict2.get("first_name")  # Zeynep
dict2.get("last_name")  # Akkaya

# .keys() method
dict2.keys()  # dict_keys(['first_name', 'last_name'])

# .values() method
dict2.values()  # dict_values(['Zeynep', 'Akkaya'])

# .items() method
dict2.items()  # dict_items([('first_name', 'Zeynep'), ('last_name', 'Akkaya')])

dict2["age"] = 21
# .update() method
dict2.update({"age": 22})

# .popitem() method
# removes the last inserted item
dict2.popitem()

# .pop() method
dict2.pop("first_name")
dict2.pop("last_name")

dict2  # {}

for x, y in dict1.items():
    print(x, ":", y)
"""
brand : Porsche
model : 911 Classic
year : 1964
"""

# .fromkeys() method
x = ("key1", "key2", "key3")
y = 0
dict3 = dict.fromkeys(x, y)
dict3  # {'key1': 0, 'key2': 0, 'key3': 0}
