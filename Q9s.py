#Question 9: Convolution of box function with itself.
import numpy as np
import matplotlib.pyplot as plt

def f(x):#Definition of the function
    if abs(x)<=1:
        sol=1
    else:
        sol=0
    return sol

N=256
x_min=-5
x_max=5
x=np.linspace(x_min,x_max,N)
del_x=x[1]-x[0]
fx=[]
for i in range(N):
        fx.append(f(x[i]))
        
k=2*np.pi* np.fft.fftfreq(N,d=del_x)
del_k=k[1]-k[0]
x_new=2*np.pi*np.fft.fftfreq(N,d=del_k) #Arranging x 

fk=np.fft.fft(fx,norm="ortho")
Fx=del_x*np.sqrt(N)*np.fft.ifft(fk**2,norm='ortho') #convolution with itself

plt.plot(x,fx,'g--')
plt.plot(x_new,np.real(Fx),'teal')
plt.legend(['$f(x)$',r'$[f\otimes f](x)$'],fontsize=14)
plt.xlabel('$x$')
plt.grid()
plt.show()
