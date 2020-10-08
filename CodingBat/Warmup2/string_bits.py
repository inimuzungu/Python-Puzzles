"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
  if len(str) < 1:
    return str
  else:
    for i in range(len(str)):
      return str[0::2]




str = "Hello"
string_bits(str)