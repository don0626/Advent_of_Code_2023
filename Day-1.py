# Advent of Code 2023 Day 1
import re
test = 'testdata.txt'
data='day1a.txt'
numtext = "zero,one,two,three,four,five,six,seven,eight,nine".split(',')

def main():
    sum=0
    with open (data,'r') as f:
        # part 2
        while line:= f.readline():
            #part 2
            for n in range(0,10):
                line = re.sub(numtext[n],numtext[n][0]+str(n)+numtext[n][-1],line)
            #part 1
            nums = re.findall('\d',line)
            sum += int(nums[0]+nums[-1])
    print (f'Day 1:{sum}')
# part1 took 1 try, part 2 four ties
main()
