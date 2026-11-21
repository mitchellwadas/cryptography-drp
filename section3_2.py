from section1_2 import extended_euclidean
from section1_3 import fast_powering
from section1_7 import *
from section3_3 import big_prime
import math
import time # for speed tests

def key_gen(nbits=2048, e=65537):
    # returns (N, p, q, d, e)

    # What psycho is going to give me an odd number of bits..
    prime_bits = math.ceil(nbits/2)
    p = big_prime()
    q = big_prime()

    # if we found primes
    if p and q:
        g, u, v = extended_euclidean(e, (p-1)*(q-1))

        # if gcd(e, (p-1)(q-1)) = 1 as required
        if g == 1: 
            # decryption exponent = inverse of e mod (p-1)(q-1)
            # grab positive representative
            d = u % ((p-1)*(q-1))

            return (p*q, p, q, d, e)

        else:
            print("Failed to find suitable primes. Try again")

    else:
        print("Failed to find primes. Try again")

def encrypt_int(m, e, N):
    # c = m^{e} mod N
    return fast_powering(m, e, N)

def decrypt_int(c, d, N):
    # m = c^{d} mod N
    return fast_powering(c, d, N)

def encrypt_message(m, e, N):
    cs = []
    for m in message_to_integer_blocks(m):
        cs.append(encrypt_int(m, e, N))
    return cs

def decrypt_message(cs, d, N):
    ms = []
    for c in cs:
        ms.append(decrypt_int(c, d, N))
    return integer_blocks_to_message(ms)


if __name__ == "__main__":

    # This is a little slow.... :(

    start = time.perf_counter()
    N, p, q, d, e = key_gen()
    end = time.perf_counter()
    print(f"Key gen: {end - start:.6f} seconds")

    m = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum."
    
    start = time.perf_counter()
    c = encrypt_message(m, e, N)
    end = time.perf_counter()
    print(f"Encrypt: {end - start:.6f} seconds")

    start = time.perf_counter()
    m_ = decrypt_message(c, d, N)
    end = time.perf_counter()
    print(f"Decrypt: {end - start:.6f} seconds")

    # in the process of decryption, the coding scheme may # introduce some null characters "\x00", so get rid of them
    print(m == m_.rstrip("\x00"))

    # verify (by looking) that these are the same message
    print(m_)