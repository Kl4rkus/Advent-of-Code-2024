lines = [[int(x) for x in l.strip().split(' ')] for l in open("AoC2024/input/2.txt")]

def test(i):
    a=0
    for j in range(1,len(i)):
        if abs(i[j]-i[j-1])<1 or abs(i[j]-i[j-1])>3:
            return (1,j)
        if a==0:
            if i[j]<i[j-1]:
                a=1
            else:
                a=2
        if a==1 and i[j]>i[j-1]:
            return (1,j)
        if a==2 and i[j]<i[j-1]:
            return (1,j)
    return (0,-1)


def part1():
    c=0
    for i in lines:
        c+=test(i)[0]
    print(len(lines)-c)


part1()

def part2():
    c=0
    for i in lines:
        t=0
        a=test(i)
        if a[0]==1:
            for j in range(max(0,a[1])-2,a[1]+1):
                i2 = i[:j]+i[j+1:]
                if test(i2)[0]==0:
                    t=-1
                    print("safe")
                    break
                else:
                    print(i,i2)
        c+=test(i)[0]
        c+=t
    print(len(lines)-c)

part2()       
