#!/usr/bin/python3
#rev 1
#Last modified 6/4/2020
#writen by Kevin Burkeland
import random

c = 0
uc = 0
sr = 0
r = 0
ur = 0
l = 0
print("Welcome to revision 1 of Kevin Burkeland's herb roller")
#gets the number of dice to roll
biome = input('What biome are you in? currently supported [Forest, River]: ')
biome = str.lower(biome)
dnum = input('how many dice do you want to roll?: ')
with open("./"+biome+"/common.txt") as f:
    commonlist = f.read().splitlines()

with open("./"+biome+"/uncommon.txt") as f:
    uncommonlist = f.read().splitlines()

with open("./"+biome+"/semirare.txt") as f:
    semirarelist = f.read().splitlines()

with open("./"+biome+"/rare.txt") as f:
    rarelist = f.read().splitlines()

with open("./"+biome+"/ultrarare.txt") as f:
    ultrararelist = f.read().splitlines()

with open("./"+biome+"/legendary.txt") as f:
    legendarylist = f.read().splitlines()

crange = len(open("./"+biome+"/common.txt").readlines())
ucrange = len(open("./"+biome+"/uncommon.txt").readlines())
srrange = len(open("./"+biome+"/semirare.txt").readlines())
rrange = len(open("./"+biome+"/rare.txt").readlines())
urrange = len(open("./"+biome+"/ultrarare.txt").readlines())
lrange = len(open("./"+biome+"/legendary.txt").readlines())

#makes sure its a number
dnum = int(dnum)
#checks for sort
rolls = []
crolls = []
ucrolls = []
srrolls = []
rrolls = []
urrolls = []
lrolls = []
for _ in range(dnum):
    roll = random.randint(1, 100)
    rolls.append(roll)
for i in rolls:
    if 1 <= i <= 39:
        c += 1
    elif 40 <= i <= 65:
        uc += 1
    elif 66 <= i <= 80:
        sr += 1
    elif 81 <= i <= 94:
        r += 1
    elif 95 <= i <= 98:
        ur += 1
    elif 99 <= i <= 100:
        l += 1
    else:
        print('tell kevin his shit is busted')
print('commons = ' + str(c))
for _ in range(c):
    croll = random.randint(0, crange - 1)
    crolls.append(croll)
crolls.sort()
for i in crolls:
    print(commonlist[i])
print('-------------------------------')

print('uncommons = ' + str(uc))
for _ in range(uc):
    ucroll = random.randint(0, ucrange - 1)
    ucrolls.append(ucroll)
ucrolls.sort()
for i in ucrolls:
    print(uncommonlist[i])
print('-------------------------------')

print('semi rares = ' + str(sr))
for _ in range(sr):
    srroll = random.randint(0, srrange - 1)
    srrolls.append(srroll)
srrolls.sort()
for i in srrolls:
    print(semirarelist[i])
print('-------------------------------')

print('rares = ' + str(r))
for _ in range(r):
    rroll = random.randint(0, rrange - 1)
    rrolls.append(rroll)
rrolls.sort()
for i in rrolls:
    print(rarelist[i])
print('-------------------------------')

print('ultra rares = ' + str(ur))
for _ in range(ur):
    urroll = random.randint(0, urrange - 1)
    urrolls.append(urroll)
urrolls.sort()
for i in urrolls:
    print(ultrararelist[i])
print('-------------------------------')

print('legendarys = ' + str(l))
for _ in range(l):
    lroll = random.randint(0, lrange - 1)
    lrolls.append(lroll)
lrolls.sort()
for i in lrolls:
    print(legendarylist[i])
print('-------------------------------')