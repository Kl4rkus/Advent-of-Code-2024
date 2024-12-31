lines = [[str(x) for x in l.strip()] for l in open("AoC2024/input/4.txt")]
maxx=len(lines)
maxy=len(lines[0])
word="XMAS"
direction=(0,0)
directions=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

def check_letter(coor,lett,a1,a2):
    dire=(a1,a2) 
    if coor[0]+dire[0]<0 or coor[1]+dire[1]<0 or coor[0]+dire[0]==maxx or coor[1]+dire[1]==maxy:
        return False
    if lines[coor[0]+dire[0]][coor[1]+dire[1]]==lett:
        return True
    return False
    
def part1():
    c=0
    check=0
    for i in range(maxx):
        for j in range(maxy):
            if lines[i][j]=="X":
                for a in directions:
                    check=1
                    for l in range(1,len(word)):
                        if not check_letter((i,j),word[l],l*a[0],l*a[1]):
                            check=0
                            break
                    if check==1: c+=1
    print(c)
                    
part1()   

def check(i,j):
    if lines[i][j]=="A":
        if lines[i+1][j+1]=="M" and lines[i-1][j-1]=="S" or lines[i-1][j-1]=="M" and lines[i+1][j+1]=="S":
            if lines[i+1][j-1]=="M" and lines[i-1][j+1]=="S" or lines[i+1][j-1]=="S" and lines[i-1][j+1]=="M":
                return True
    return False
def part2():
    c=0
    for i in range(1,maxx-1):
        for j in range(1,maxy-1):
            if check(i,j):
                c+=1
    print(c)

part2()
