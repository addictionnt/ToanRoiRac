a = True
b = print("B được kiểm tra") or True
print(a and b) # True vì cả 2 cùng True
print(a or b)  # True vì a True

a = False
b = print("B được kiểm tra") or True
print(a and b)  # False vì a False
print(a or b)   # True vì a False nhưng b True


c = 3406 > 2006
d = 0 / 5 == 1

print(c and d)
print(c or d)

