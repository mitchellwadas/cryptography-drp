from random import randint
from section1_3 import fast_powering
import time # for speed tests

def random_number(nbits=1024):
    # since 2310 > 2^{11} we need k with about 1013 bits
    # there's an interesting question:
    #   since we only search for primes in some fixed range,
    #   could Eve exhaustively search this range?
    # she will not know where to end, but she can start at
    # 1024 bits and expect that we won't go much bigger

    K_bits = nbits - 11
    K = randint(2**K_bits, 2**(K_bits + 2))
    N = 2 * 3 * 5 * 7 * 11 * K + 1139

    # 1139 is relatively prime to 2,3,...,11
    # so this makes it more likely N is prime
    return N

def unnamed_helper(a):
    # write a = 2^k q with q odd

    # magic using python bit operations...
    k = (a & -a).bit_length() - 1
    q = a >> k

    return (k, q)

def miller_rabin(N, a):
    k, q = unnamed_helper(N-1)
    a = fast_powering(a, q, N)

    if (a % N) == 1:
        return False # Fail to conclude composite

    for i in range(k):
        if (a % N) == (N-1):
            return False # Fail to conclude composite

        a = fast_powering(a, 2, N)
    
    return True # N is composite and a is a witness

def is_probably_prime(N, trials=50):

    # try some witnesses...
    for i in range(trials):
        a = randint(1 ,N-1)

        # if a is a witness to compositeness
        if miller_rabin(N, a):
            return False
    
    # probably prime?
    return True

def big_prime(nbits=1024, max_iter=1000):

    for i in range(max_iter):
        p = random_number(nbits)
        if is_probably_prime(p):
            return p

    print(f"Failed to find a large prime")

if __name__ == "__main__":

    start = time.perf_counter()
    big_prime()
    end = time.perf_counter()
    print(f"Big prime: {end - start:.6f} seconds")

    # Running between 0.5 and 2.5 seconds...
    # We can do better...
