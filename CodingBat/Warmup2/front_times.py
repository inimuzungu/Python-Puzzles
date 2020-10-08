"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""

def front_times(str, n):
    if len(str) >= 3:
        print(str[0:3] * n)
    else:
        print(str[0:len(str)] * n)


str = "Ph"
n = 5

front_times(str, n)