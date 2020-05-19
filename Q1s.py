import numpy as np 
import matplotlib.pyplot as plt 
def f(x):#Definition of the function
    if x !=0:
        sol=(1/x)*np.sin(x)
    else:
        sol=1
    return sol
def fk(x):
    if abs(x)<=1:
        sol=np.sqrt((np.pi)/2)
    else:
        sol=0
    return sol
N=256
x_min=-50
x_max=50
x=np.linspace(x_min,x_max,N)
delta = (x_max-x_min)/(N-1)
f_arr,fk_arr_exact=[],[]
for i in range(N):
    f_arr.append(f(x[i]))
n_fft = np.fft.fft(f_arr, norm='ortho') 
karr = np.fft.fftfreq(N, d=delta)
karr = 2*np.pi*karr
factor = np.exp(-1j * karr * x_min)
aft = delta * np.sqrt(N/(2.0*np.pi)) * factor * n_fft
for i in range(karr.size):
    fk_arr_exact.append(fk(karr[i]))

plt.plot(karr,aft,color='c',label = 'Numerical')
plt.plot(karr,fk_arr_exact,color='r',label='Analytical')
plt.xlabel(r'$k$',fontsize=20)
plt.ylabel(r'$\tilde{f}$',fontsize=20)

plt.legend()
plt.grid()
plt.show()