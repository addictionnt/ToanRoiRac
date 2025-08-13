import math

def hoan_vi(n):
    if n < 0:
        return 0 
    return math.factorial(n)

def to_hop(n, k):
    if k < 0 or n < k:
        return 0 
    
    numerator = math.factorial(n)
    denominator = math.factorial(k) * math.factorial(n - k)
    
    return numerator // denominator

def chinh_hop(n, k):

    if k < 0 or n < k:
        return 0 
    numerator = math.factorial(n)
    denominator = math.factorial(n - k)
    
    return numerator // denominator

def to_hop_lap(n, k):
    if k < 0: 
        return 0
   
    return to_hop(n + k - 1, k)

if __name__ == "__main__":
    return "

# Tính 5!
# Tính C(9,5)
# Tính P(9,5)
# Tính A(9,5)   
    


   