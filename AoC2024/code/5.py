d={}
with open("AoC2024/input/5a.txt") as f:
    for line in f:
        (key,val)= line.split("|")
        if not (int(key) in d.keys()):
            d[int(key)] = [int(val)]
        else:
            d[int(key)].append(int(val))
print(d)

lines = [[int(x) for x in l.strip().split(',')] for l in open("AoC2024/input/5b.txt")]
print(lines)

def part1():
    c=0
    for i in range(len(lines)):
        check=1
        for j in range(1,len(lines[i])):
            if (int(lines[i][j]) in d.keys()):
                if set(lines[i][:j]) & set(d[lines[i][j]])!=[]:
                    check=0
                    break
        if check==1: 
            c+=lines[i][len(lines[i])//2]
    print(c)
part1()

