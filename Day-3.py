# Advent of Code 2023 Day 3 - GitHub
import re

def ispart(adj_symbols):
    #find if any of the possible symbols are in the list of adjacent symbols
    symbols = r"*&@/+#$%=-"  # scanned file for all non digits and periods
    for s in symbols:
        if s in adj_symbols:
            return True
    return False

def schematic(data):
    with open(data) as f:
        engine = [i for i in f.read().splitlines()]
    return engine

def main(data):
    engine = schematic(data)
    p = re.compile("[0-9]+")
    sum_parts = 0
    for n,line in enumerate(engine):
        schematic_st = max(0,n-1)
        schematic_end = min(len(engine)-1,n+1)
        for m in p.finditer(line):
            part_st = max(0,m.start()-1)
            part_end = min(len(line),m.end()+1)
            adj_symbols = ''
            for sch_line in range(schematic_st,schematic_end+1):
                adj_symbols += engine[sch_line][part_st:part_end]
            if ispart(adj_symbols):
                sum_parts += int(m.group())
    print(f'Part one of sum part numbers: {sum_parts}')

test = 'testdata.txt'
data = 'day3.txt'
if __name__ == '__main__':
    main(data)