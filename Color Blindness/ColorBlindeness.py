import numpy as np
import matplotlib.pyplot as plt

pop_s=int(input('Enter the size of population:'))
n_gen=int(input('Enter the no. of generations:'))

def findpercents (Genes,population):
        t=0
        m=0
        f=0
        for k in range(0,pop_s):
            if population[k]==0:
                t=t+1
            if population[k]==0 and Genes[0][k]==0:
                m=m+1
            if population[k]==1 and Genes[0][k]==0 and Genes[1][k]==0:
                f=f+1
        mcb=(m/t)*100
        fcb=(f/(pop_s-t))*100
        tcb=(m+f)/pop_s*100
        print('male_percent_CB',mcb)
        print('female_percent_CB',fcb)

        print('overall_percent_CB',tcb)
        return mcb,fcb,tcb

def main (pop_s,n_gen):
    population=np.array([0]*int(pop_s/2)+[1]*int(pop_s/2))
    np.random.shuffle(population)
    print('population:',population)
    
    allel1=np.array([0]*int(pop_s*0.2)+[1]*int(pop_s*0.8))
    np.random.shuffle(allel1)
##    print('allel1:',allel1)
    
    allel2=np.array([0]*int(pop_s*0.2)+[1]*int(pop_s*0.8))
    np.random.shuffle(allel2)
##    print('Random allel2:',allel2)

    for i in range(0,pop_s):
        if population[i]==0:
            allel2[i]=5
##    print('allel2:',allel2)
    
    Genes=np.zeros((2,len(population)))
    Genes[0]=np.asarray(allel1)
    Genes[1]=np.asarray(allel2)
    print('Genes:',Genes)

    p,q,r=findpercents(Genes,population)
    male_percent=[]
    female_percent=[]
    total_percent=[]
    male_percent.append((p))
    female_percent.append((q))
    total_percent.append((r))
    print(male_percent)
    print(female_percent)
    print(total_percent)

    a=np.zeros((3,int(pop_s/2)))
    b=np.zeros((3,int(pop_s/2)))

    def randperm(c):
        for i in range(0,c):
            a[0][i]=i+1
            b[0][i]=i+1
        
    c=int(pop_s/2)
    randperm(c)

    def all_assign(population,allel1,allel2):
        s=0
        t=0
        for i in range(len(population)):
            if population[i]==0:
                  a[1][s]=allel1[i]
                  a[2][s]=allel2[i]
                  s=s+1
            else:
                b[1][t]=allel1[i]
                b[2][t]=allel2[i]
                t=t+1
                
    all_assign(population,allel1,allel2)
    print('Ordered male population:\n',a)
    print('Ordered female population:\n',b)

    l=int(len(population)/2)    
    new_genes=np.zeros((2,l))
    num_of_offsprings=[]
   
    print(new_genes)
   
    for i in range(0,l):
        offspring=0+(5-0)*np.random.random((1))
        num_of_offsprings.append(np.round(offspring[0]))
    print(num_of_offsprings)
    p=np.sum(num_of_offsprings)

    new_pop=0+1*np.random.random((int(p)))
    new_pop=np.round(new_pop)
    np.random.shuffle(new_pop)
    print('New population:',new_pop)
               

    
    

                
main(pop_s,n_gen)


        
          
              
    





















    
