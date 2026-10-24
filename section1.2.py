from random import randint  # for testing


# Naive division with remainder
def division(a,b):
    assert a >= 0
    assert b >  0

    r = a
    q = 0
    while True:
        if r < b:
            return (q, r)
        else:
            r -= b
            q += 1


# Simple Euclidean algorithm
def simple_euclidean(a,b):
    assert a >= 0
    assert b >= 0

    #  recursive base case
    if b == 0:
        return a

    else:
        q, r = division(a,b)
        return simple_euclidean(b,r)


# Extended Euclidean algorithm
def extended_euclidean(a,b):
    # returns (g, u, v) so that au + bv = g = (a,b)

    assert a >= 0
    assert b >= 0

    if a == b == 0: 
        return (0,0,0)

    r0 = a
    u0 = 1
    v0 = 0

    r1 = b
    u1 = 0
    v1 = 1

    while True:
        q, r = division(r0, r1)

        if r == 0:
            return (r1, u1, v1)
        
        else:
            x = u1
            y = v1
            u1 = u0 - q * u1
            v1 = v0 - q * v1
            u0 = x
            v0 = y

            r0 = r1
            r1 = r


def test(trials=10000):

    for i in range(trials):
        a = randint(0, 10**6)
        b = randint(0, 10**6)

        g, u, v = extended_euclidean(a,b)

        assert a*u + b*v == g               # check coefficients
        assert g == simple_euclidean(a, b)  # check gcd against simpler method

    print(f"Passed {trials} trials")


if __name__ == "__main__":
    test()