R=['.','.','.','.','.','.','.','.','.']
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
def win():
    w=0
    if (R[0]=='x' and R[1]=='x' and R[2]=='x') or (R[3]=='x' and R[4]=='x' and R[5]=='x') or (R[6]=='x' and R[7]=='x' and R[8]=='x') or (R[0]=='x' and R[3]=='x' and R[6]=='x') or (R[1]=='x' and R[4]=='x' and R[7]=='x') or (R[2]=='x' and R[5]=='x' and R[8]=='x') or (R[0]=='x' and R[4]=='x' and R[8]=='x') or (R[2]=='x' and R[4]=='x' and R[6]=='x'):
        print('Player 1 wins')
        w=1
        return (w)
    elif (R[0]=='o' and R[1]=='o' and R[2]=='o') or (R[3]=='o' and R[4]=='o' and R[5]=='o') or (R[6]=='o' and R[7]=='o' and R[8]=='o') or (R[0]=='o' and R[3]=='o' and R[6]=='o') or (R[1]=='o' and R[4]=='o' and R[7]=='o') or (R[2]=='o' and R[5]=='o' and R[8]=='o') or (R[0]=='o' and R[4]=='o' and R[8]=='o') or (R[2]=='o' and R[4]=='o' and R[6]=='o'):
        print('Player 2 wins')
        w=1
        return (w)
# MAIN FUNCTION
print('WELCOME  TO  TIC  TAC  TOE')
display()
print()
for i in range(1,10):
    if i%2!=0:
        print('Player 1 chance:')
        p1=int(input())
        if R[p1-1]=='.':
            R[p1-1]='x'
        else:
            print('invalid entry')
            f=0
            while(f==0):
                print('Player 1 chance:')
                p1=int(input())
                if R[p1-1]=='.':
                    R[p1-1]='x'
                    f=1
                else:
                    print('invalid entry')
    else:
        print()
        print('Player 2 chance:')
        p2=int(input())
        if R[p2-1]=='.':
            R[p2-1]='o'
        else:
            print('invalid entry')
            f=0
            while(f==0):
                print('Player 2 chance:')
                p2=int(input())
                if R[p2-1]=='.':
                    R[p2-1]='o'
                    f=1
                else:
                    print('invalid entry')
    display()
    if win()==1:
        break
