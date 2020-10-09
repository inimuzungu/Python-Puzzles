import random

def coin_flip(coins):
    lst_head = []
    lst_tails = []
    for i in range(coins):
        result = random.randint(1, 2)
        if result == 1:
            #print("Heads!")
            lst_head.append("Heads")
        elif result == 2:
            #print("Tails!")
            lst_tails.append("Tails")
        else:
            print("Not Working")

    print(f"{len(lst_head)} + {len(lst_tails)}")

coin_flip(1)
coin_flip(10)
coin_flip(100)
coin_flip(1000)
coin_flip(10000)
coin_flip(100000)
coin_flip(1000000)
coin_flip(10000000)
coin_flip(100000000)
coin_flip(1000000000)
coin_flip(10000000000)
coin_flip(100000000000)
coin_flip(1000000000000)




