
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
x_min=4
x_max=100
def direct_time(N):
    w_p=np.arange(N)
    t1=timer()
    w_q=[]
    for q in range(N):
        for p in range(N):
            w_q.append((w_p[p]*np.exp(-1j*2*np.pi*q*p/N))/(np.sqrt(N)))
    t2=timer()
    del_td=t2-t1
    return(del_td)
    
    
def fft_time(N):
    w_p=np.arange(N)
    t3=timer()
    w_q=np.fft.fft(w_p,norm='ortho')
    t4=timer()
    del_tf=t4-t3
    return(del_tf)
    
N,t_direct,t_fft=[],[],[]

for i in range(x_min,x_max):
    N.append(i)
    t_direct.append(direct_time(i))
    t_fft.append(fft_time(i))

plt.plot(N,t_direct,'teal',label='Direct way')
plt.plot(N,t_fft,'salmon',label='Using numpy.fft.fft')
plt.xlabel(r'$n$',fontsize=16)
plt.ylabel(r'$\Delta t$',fontsize=16)
plt.legend()
plt.grid()
plt.show()
