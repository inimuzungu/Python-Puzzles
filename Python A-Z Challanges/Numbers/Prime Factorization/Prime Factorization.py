lst_prime = [2, 3, 5, 7, 11, 17, 19, 23]
lst_factors = []

def factorize(nr):
    i = 2
    factors = []
    while i <= nr:
        if nr / i != 0:
            factors.append(i)
        else:
            i += 1
    print(factors)