import numpy as np
R=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display():
    c=-1;
    print('_________________________________________________')
    for i in range(0,3):
        print('|',end='')
        for j in range(0,3):
            c=c+1
            print('\t%c\t|'%(R[c]),end='')
        print('')
        print('_________________________________________________')
def ccheck(x,y,z):
    v=0
    if R[x]=='o' and R[y]=='o' and R[z]==' ':
        R[z]='o'
        v=1
        return v
    if R[y]=='o' and R[z]=='o' and R[x]==' ':
        R[x]='o'
        v=1
        return v
    if R[z]=='o' and R[x]=='o' and R[y]==' ':
        R[y]='o'
        v=1
        return v

def cstop(x,y,z):
    v=0
    if R[x]=='x' and R[y]=='x' and R[z]==' ':
        R[z]='o'
        v=1
        return v
    if R[y]=='x' and R[z]=='x' and R[x]==' ':
        R[x]='o'
        v=1
        return v
    if R[z]=='x' and R[x]=='x' and R[y]==' ':
        R[y]='o'
        v=1
        return v
def win():
    w=0
    if (R[0]=='x' and R[1]=='x' and R[2]=='x') or (R[3]=='x' and R[4]=='x' and R[5]=='x') or (R[6]=='x' and R[7]=='x' and R[8]=='x') or (R[0]=='x' and R[3]=='x' and R[6]=='x') or (R[1]=='x' and R[4]=='x' and R[7]=='x') or (R[2]=='x' and R[5]=='x' and R[8]=='x') or (R[0]=='x' and R[4]=='x' and R[8]=='x') or (R[2]=='x' and R[4]=='x' and R[6]=='x'):
        print('Player wins')
        w=1
        return (w)
    elif (R[0]=='o' and R[1]=='o' and R[2]=='o') or (R[3]=='o' and R[4]=='o' and R[5]=='o') or (R[6]=='o' and R[7]=='o' and R[8]=='o') or (R[0]=='o' and R[3]=='o' and R[6]=='o') or (R[1]=='o' and R[4]=='o' and R[7]=='o') or (R[2]=='o' and R[5]=='o' and R[8]=='o') or (R[0]=='o' and R[4]=='o' and R[8]=='o') or (R[2]=='o' and R[4]=='o' and R[6]=='o'):
        print('CPU wins')
        w=1
        return (w)
# MAIN FUNCTION
print('WELCOME  TO  TIC  TAC  TOE')
print()
display()
md=0
for i in range(1,10):
    f=0
    if i%2!=0:
        while(f==0):
            print('Player chance:')
            p1=int(input())
            if R[p1-1]==' ':
                R[p1-1]='x'
                f=1
            else:
                print('Invalid entry')
    else:
        print()
        v=0
        w=0
        x=[0,3,6,0,1,2,0,2]
        y=[1,4,7,3,4,5,4,4]
        z=[2,5,8,6,7,8,8,6]
        print('CPU chance:')
        for i in range(0,8):
            v=ccheck(x[i],y[i],z[i])
            if v==1:
                break
        if v!=1:
            for i in range(0,8):
                w=cstop(x[i],y[i],z[i])
                if w==1:
                    break
        if v!=1 and w!=1:
            while(f==0):
                p1=np.round(int(1+(9-1)*np.random.random(1)))
                if R[p1-1]==' ':
                    R[p1-1]='o'
                    f=1
    md=md+1
    display()
    if win()==1:
        break
if md==9 and win()!=1:
    print('Match Draw')
