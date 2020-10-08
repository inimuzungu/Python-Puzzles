"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

"""

def hello_name(name):

    str_hello = "Hello"
    str_exc = "!"
    return str_hello +name +str_exc


name = "Door"
hello_name(name)