from section1_3 import fast_powering
from section1_2 import extended_euclidean

def fermat_inverse(a, p):
    # assert p is prime.... and a > 0
    # a^{-1} = a^{p-2}
    return fast_powering(a, p-2, p)

def euclidean_inverse(a, n):
    g, u, v = extended_euclidean(a, n)
    
    # u could be negative.
    # switch to representative in 0, 1, ..., n-1.
    if g  == 1:
        return u % n
    
    return False

if __name__ == "__main__":
    print(fermat_inverse(2, 5))
    print(euclidean_inverse(2,5))