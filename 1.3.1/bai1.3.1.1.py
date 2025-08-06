a = 3 > 5
b = 4 != 4

print("a and b =", a and b) # False do a = False và b = False nên a and b = False
print("a or b =", a or b)   # False do a = False và b = False nên a or b = False
print("a ^ b =", a ^ b) # False do a = False và b = False nên a ^ b = False
print("not a =", not a) # True do a = False nên not a = True

print("a and (not b) =", a and (not b))
# a ^ b == a and (not b)


