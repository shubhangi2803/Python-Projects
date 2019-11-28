import numpy as np
import matplotlib.pyplot as plt

A=50
num_node=10
srange=15
data=0+(A-0)*np.random.random((2,num_node))

# nodes - graph plotting
plt.figure(1)
plt.plot(data[0,:],data[1,:],'r*')
for i in range(0,num_node):
         plt.text(data[0,i],data[1,i],str(i+1))

# calculating all distances
dist=np.zeros((num_node,num_node))
for i in range(0,num_node):
    for j in range(0,num_node):
        if i!=j:
            d=np.sqrt((data[0,j]-data[0,i])**2+(data[1,j]-data[1,i])**2)
            dist[i,j]=np.round(d)
print(dist)
plt.show()

# making graph matrix
for i in range(0,num_node):
    for j in range(0,num_node):
        if i!=j:
            if dist[i][j]<15:
                dist[i][j]=1
            else:
                dist[i][j]=0
        else:
            dist[i][j]=0
print(dist)

# showing neighbours joined with lines
node_no=input('Enter the node number: ')
node_no=int(node_no)
print('Neighbours: ')
for i in range(0,num_node):
    x1=data[0][node_no-1]
    y1=data[1][node_no-1]
    if dist[node_no-1][i]==1:
        print(i+1)
        x2=data[0][i]
        y2=data[1][i]
        p1=[x1,x2]
        p2=[y1,y2]
        plt.plot(p1,p2)
        plt.plot(data[0,:],data[1,:],'r*')
        plt.plot(x1,y1,'k*')
        for i in range(0,num_node):
            plt.text(data[0,i],data[1,i],str(i+1))
plt.show()

# Energy and energy graph
Enr=np.ones((num_node))*1000
for p in range(0,500):
    f=0
    etx=40+(60-40)*np.random.random()
    etx=int(np.round(etx))
    erx=20+(40-20)*np.random.random()
    erx=int(np.round(erx))
    nn=1+(num_node-1)*np.random.random()
    nn=int(np.round(nn))
    if Enr[nn-1]-etx>=0:
        Enr[nn-1]=Enr[nn-1]-etx
        for k in range(0,num_node):
            if dist[nn-1][k]==1:
                if Enr[k]-erx>=0:
                    Enr[k]=Enr[k]-erx
    for i in range(0,num_node):
        for m in range(0,num_node):
            plt.text(data[0,m],data[1,m],str(m+1))
            x3=data[0,i]
            y3=data[1,i]
            if Enr[i]>750:
                plt.plot(x3,y3,'g*')    
            if Enr[i]>500 and Enr[i]<750:
                plt.plot(x3,y3,'b*')
            if Enr[i]>250 and Enr[i]<500:
                plt.plot(x3,y3,'y*')
            if Enr[i]>120 and Enr[i]<250:
                plt.plot(x3,y3,'m*')
            if Enr[i]<120:
                plt.plot(x3,y3,'r*')
            if Enr[i]<20:
                plt.plot(x3,y3,'k*')
        plt.title(['Iteration no.',str(p+1)])
    plt.pause(0.001)
    print(Enr)
    
