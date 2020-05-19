import numpy as np
import matplotlib.pyplot as plt

def f(k):
        return(np.exp(-k*k/4.0)/np.sqrt(2.0))
file=open('Q4s.txt','r')
k,aft,aft_exact=[],[],[]

for line in file:
    k_,aft_data=line.split()
    k.append(float(k_))
    aft.append(float(aft_data))
    aft_exact.append(f(float(k_)))

plt.plot(k,aft,'teal',label='FFTW')    
plt.plot(k,aft_exact,'salmon',label='Exact')
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'$\tilde{f}$',fontsize=16)
plt.title('Problem 4')
plt.legend()
plt.grid()
plt.show()



