lines= [l for l in open("AoC2024/input/3.txt")][0]
print(lines)

def part1():
    state=0
    l="mul("
    s=0
    n1=""
    n2=""
    for i in lines:
        if state<4:
            if l[state]==i:
                state+=1
                n1=""
                n2=""
            else: state=0
        elif state==4:
            if i.isnumeric(): n1+=i
            elif i==",": state+=1
            else: state=0
        elif state==5:
            if i.isnumeric(): n2+=i
            elif i==")": 
                state=0
                s+=int(n1)*int(n2)
            else: state=0
    print(s)

def part2():
    state=0 #how far we've come
    job=0 #type (1=mul, 2=don¨t, 3=do)
    do=True
    l="mul("
    l2="don't()"
    l3="do()"
    s=0
    n1=""
    n2=""
    for i in lines:
        ##FOR CHOOSING JOB
        if state==0:
            if do and i=="m":
                job=1
                state+=1
            if i=="d":
                job=2
                state+=1
        ##FOR MUL()
        elif job==1:
            if state<4:
                if l[state]==i:
                    state+=1
                    n1=""
                    n2=""
                else: state=0
            elif state==4:
                if i.isnumeric(): n1+=i
                elif i==",": state+=1
                else: state=0
            elif state==5:
                if i.isnumeric(): n2+=i
                elif i==")": 
                    state=0
                    s+=int(n1)*int(n2)
                else: state=0
        ##FOR DON'T
        elif job==2:
            if state<7:
                if state==2 and "("==i:
                    state+=1
                    job=3
                elif l2[state]==i:
                    state+=1
                else: state=0
            if state==7:
                do=False
                state=0
        ##FOR DO
        elif job==3:
            if state<4:
                if l3[state]==i:
                    state+=1
            if state==4:
                do=True
                state=0
    print(s)
part2()

            