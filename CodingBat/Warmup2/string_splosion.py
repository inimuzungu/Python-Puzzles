"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""

def string_splosion(str):
    for i in range(len(str)):
      print(str[0] +str[0:2] +str[0:3] +str[0:len(str)])


str = "Code"
string_splosion(str)