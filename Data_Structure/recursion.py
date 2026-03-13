# Function calling itself is called recursion.
def fac(n):
    if n == 1:
        return 1 #base case
    else:
        return n * fac(n-1) # recursion case

print(fac(5))