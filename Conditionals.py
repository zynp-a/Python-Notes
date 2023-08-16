a = 1
b = 5

print("A") if a > b else print("=") if a == b else print("B")
# B

# pass keyword
if a > b: pass

c = 9
if c > a and c > b: print("C is the biggest")
# C is the biggest

c = -99
if not c > a and not c > b: print("C is the smallest")
# C is the smallest
