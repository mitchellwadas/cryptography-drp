from random import randint  # for testing


# The modulo operator % computes a modulo m. Eg. r = a % m
# Equivalently, we could use the division algorithm from section 1.2 and write q, r = division(a,m).
# However, our division algorithm is quite slow! We'll use python's built in modulo operator.
# If we need the remainder we can use python's built in divmod. Eg. q, r = divmod(a,m)


# Convert an integer to its binary representation
def int_to_binary(a):
    assert a >= 0

    if a == 1:
        return "1"
    if a == 0:
        return "0"

    r = a % 2
    return int_to_binary((a-r)//2) + str(r)


# Convert an integer to its binary representation, but put the digits in the opposite order
# For fast powering, it's convenient to have these in the order a0 a1 ... ar
def int_to_binary_rev(a):
    assert a >= 0

    if a == 1:
        return "1"
    if a == 0:
        return "0"

    r = a % 2
    return str(r) + int_to_binary_rev((a-r)//2)


# test against pythons built in function bin
def test_bin(trials=10000):

    for i in range(trials):
        a = randint(0, 10**6)
        mybin = int_to_binary(a)
        assert mybin == bin(a)[2:]  # remove a prefix

    print(f"Passed {trials} trials")


# (lowish storage) variant of the fast powering algorithm
def fast_powering(g,a,m):
    assert m >= 1

    binary = int_to_binary_rev(a)
    result = 1
    gi = g

    for ai in binary:
        result = (result * (gi ** int(ai))) % m
        gi = (gi ** 2) % m
    
    return result


# test against a naive calculation
def test_powering(trials=10000):

    for i in range(trials):
        g = randint(0, 10**6)
        a = randint(0, 10**6)
        m = randint(1, 10**6)

        # computing the truth in the naive way is actually very slow
        # comparatively, our algorithm is very fast! As we hoped
        truth = (g**a) % m
        assert fast_powering(g,a,m) == truth

    print(f"Passed {trials} trials")
    

if __name__ == "__main__":
    test_bin()
    test_powering()

# It might be worth testing the speed of int_to_bin versus bin(a)