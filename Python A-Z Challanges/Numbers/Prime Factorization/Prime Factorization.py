lst_prime = [2, 3, 5, 7, 11, 17, 19, 23]
lst_factors = []

def factorize(nr):
    i = 2
    factors = []
    while i <= nr:
        if nr % i == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    print(factors)

factorize(9)
factorize(1024988651)
factorize(0)
factorize(87946489641631564891213499157451621)
