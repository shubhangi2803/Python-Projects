import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
from itertools import permutations 
from itertools import combinations
import array

#color=['Red','Yellow','Blue','Green','White','Black','Grey','Golden','Silver']
ran_colors=[]
color_num=[0,1,2,3,4,5,6,7,8]

##C=int(input('Enter the number of colors: '))
##D=int(input('Enter the number of digits: '))

def gen_vector(C,D):
    guess_vector=[]
##    def fact(n):
##        fact=1
##        for i in range(1,n+1):
##            fact=fact*i
##        return fact
##    p=(fact(C)/(fact(D)*fact(C-D)))*fact(D)
##    print("Total codes possible:",p)
    B=combinations(avail_color,D)
    c=0
    #print('Possible Codes: ')
    for i in list(B):
        #print(i)
        C=permutations(i)
        for j in list(C):
            guess_vector.append(j)
            c=c+1
    #print(guess_vector)
    tcodes=c
    #print('Total Combinations of codes=',c)
    ANSWER=random.choice(guess_vector)
    #print("Actual Code : ",ANSWER)
    guess=random.choice(guess_vector)
    TF=[1]*tcodes
    #print("TF vector: ",TF)
    #print("Guess: ",guess)
    def check_matches(n1,n2):
        p=0
        for i in range(0,D):
            if n1[i]==n2[i]:
                p=p+1
        return p
    R=1
    while(guess!=ANSWER and R<=8):
        N_match=check_matches(ANSWER,guess)
        #print("Matches= ",N_match)
        for i in range(0,len(guess_vector)):
            g=guess_vector[i]
            f=0
            for k in range(0,D):
                if g[k]==guess[k]:
                    f=f+1
            if f!=N_match:
                TF[i]=0
        #print("TF: ",TF)
        h=len(guess_vector)
        for j in range(len(guess_vector)-1,-1,-1):
            if TF[j]==0:
                del guess_vector[j]
        #print("Guess vector: ",guess_vector)
        guess=random.choice(guess_vector)
        #print("Guess: ",guess)
        TF=[1]*len(guess_vector)
        R=R+1
        #if R>8:
            #print("Code Breaker Lost")
    return R

N=20
print("N=20")
M=np.array([[6,4],[8,5],[9,6]])
#print(M)

R_all=np.zeros((3,N))
for s in range(0,3):
    NR=[]
    avail_color=[]
    C=M[s][0]
    D=M[s][1]
    for i in range(0,C):
        avail_color.append(color_num[i])
    #print('Available colors: ',avail_color)

    for g in range(0,N):
        NR.append(gen_vector(C,D))
        #print("NR= ",NR)
    R_all[s]=np.asarray(NR)
print('R_aLL: \n',R_all)

plt.figure(1)
for s in range(0,3):
    plt.subplot(1,3,s+1)
    plt.hist(R_all[s,:])
    plt.xlabel("Rounds")
    plt.ylabel("Occurances")
    plt.title("Combination"+str(s+1))
plt.show()

win_perc=[]
for r in range(0,3):
    u=0
    for s in range(0,N):
        if R_all[r,s]<=8:
            u=u+1
    win_perc.append(u*5)
print("Win percentage:")
print(win_perc)

R_avg=[]
for r in range(0,3):
    u=0
    for s in range(0,N):
       u=sum(R_all[r])
    R_avg.append(u/20)
print("Average Rounds")
print(R_avg)


'''Random code creation'''
##choices = list(range(C))
##random.shuffle(choices)
##print('Random colors: ')
##for i in range(0,D):
##    c=choices.pop()
##    print(c)
##    ran_colors.append(c)
##print(ran_colors)
##
##A=permutations(ran_colors)
##c=0
##code_array=[]
##print('Permutations')
##for i in list(A):
##    print(i)
##    code_array.append(i)
##    c=c+1
##print('Total Permutations=',c)
##
##CODE=random.choice(code_array)
##print('Code : ',CODE)
