# Advent of Code 2023 Day 2
import re, math
test = 'testdata.txt'
data='day2a.txt'
# the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes
# maxcubes = {'red':12, 'green':13, 'blue':14}
def check(color, num):
    maxcubes = {'red': 12, 'green': 13, 'blue': 14}
    match = True
    for n in range(len(color)):
        if int(num[n]) > maxcubes[color[n]]:
            match = False
    return match
def fewest(colors,num):
    cubes = {'red':0,'blue':0,'green':0}
    for n,color in enumerate(colors):
        if cubes[color]<int(num[n]):
            cubes[color]=int(num[n])
    return  math.prod(cubes.values())

def main():
    sumgood = 0
    sumcubes = 0
    with open('day2.txt') as f:
        while games := f.readline():
            okay = True
            gamenum = re.findall('\d+',games.split(':')[0])
            #part 1
            for game in games.split(':')[1].split(';'):
                cubesnum = re.findall('\d+', game)
                cubescol = re.findall('[a-z]+', game)
                if not check(cubescol,cubesnum):
                    okay = False
            if okay:
                sumgood += int(gamenum[0])
            print(f'{gamenum}: product = {fewest(cubescol,cubesnum)}')
            #part 2
            game = games.split(':')[1]
            cubesnum = re.findall('\d+', game)
            cubescol = re.findall('[a-z]+', game)
            sumcubes += fewest(cubescol,cubesnum)
    print (f'Part 1: Sum of valid game number {sumgood}')
    print (f'Part 2: Sum of products of max {sumcubes}')





main()