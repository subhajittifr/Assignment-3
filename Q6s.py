import numpy as np 
import matplotlib.pyplot as plt 

N=256
x_min=-5
x_max=5
x=np.linspace(x_min,x_max,N)
delta = (x_max-x_min)/(N-1)
f_arr=np.ones(N) # defining the constant to be 1 everywhere
kq_arr,fk = [],[]
#Algorithm of fast fourier transform:
for q in range(N):
    kq=(q-N/2)/(N*delta)
    F1=0
    for p in range(N):
        xp=p*delta
        F1+=f_arr[int(p*delta)]*np.exp(-2j*np.pi*kq*xp)
    u=delta*np.sqrt(N/(2.0*np.pi)) *F1/(np.sqrt(N))
    fk.append(u)
    kq_arr.append(kq)
plt.subplot(1,2,1)
plt.plot(x,f_arr,'m')
plt.xlabel('x',fontsize=15)
plt.ylabel('f',fontsize=15)
plt.grid()
plt.subplot(1,2,2)
plt.plot(kq_arr,fk,'c',label='Fourier Domain')
plt.xlabel(r'$k$',fontsize=20)
plt.ylabel(r'$\tilde{f}$',fontsize=20)

plt.legend()
plt.grid()
plt.show()