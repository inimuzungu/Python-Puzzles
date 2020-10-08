str = "not bad"
#print(str[0:1])

def not_string(str):
  if str[0:4] == 'not ':
    print(str)
  else:

    print('not '+ str)

not_string(str)