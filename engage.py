import random

from scipy import rand

boys = {"ali", "reza", "yasin", "benyamin", "mehrdad", "sajjad", "aidin", "shahin"}

girls = {"sara", "zari", "neda", "homa", "eli", "goli", "mary" , "mina"}

c = []

bl = len(boys)

gl = len(girls)

if(bl == gl):

    while bl > 0:

        randomboy = random.choice(tuple(boys))
        randomgirl = random.choice(tuple(girls))

        c.append((randomboy , randomgirl))

        boys.remove(randomboy)
        girls.remove(randomgirl)

        bl = bl - 1
    print(c)
    
else:

    print("not true")
