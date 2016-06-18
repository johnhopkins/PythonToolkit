import random
heads = 0 #initialize the count variables
tails = 0

while True:
    coinresult = random.randint(1, 2) #flip coin
    if coinresult == 1: #if result = 1 then increment heads counter
        heads += 1
    elif coinresult == 2: #if result = 2 then increment tails counter
        tails += 1
    if heads == tails: #check if counts are equal and break loop if they are
        break

print("The number of flips was {count}".format(count = heads + tails))
