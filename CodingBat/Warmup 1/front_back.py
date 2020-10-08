#def front_back(str):
 #   first_letter = str[0]
  #  last_letter = str[len(str) - 1]

   # return last_letter + str[1:len(str) - 1] + first_letter


def front_back(str):

    if len(str) >= 2:
        first_letter = str[0]
        last_letter = str[len(str) - 1]
        return last_letter + str[1:len(str) - 1] + first_letter

    elif len(str) <= 1:
        return str


str = ""
front_back(str)
print(front_back(str))