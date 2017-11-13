#A mother kangaroo can N kilos in her pouch. Her babies weighs what the two previous babies, the first one weiging one gram.
#This program calculates how many babies she can carry given N.

def calcLimit(x):
    summa = 0
    placeholder1 = 0
    placeholder2 = 1
    numBabies = 0
    while summa < (x*1000):
        temp = placeholder1
        placeholder1 = placeholder2
        placeholder2 += temp
        summa += placeholder2
        numBabies += 1
    return numBabies

print "how many babies?"
babies = calcLimit(int(raw_input()))
print babies
