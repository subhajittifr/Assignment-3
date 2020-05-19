import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
N=100
x_min,x_max=-50,50
y_min,y_max=-50,50

x=np.linspace(x_min,x_max,N)
y=np.linspace(y_min,y_max,N)
delta_x = (x_max-x_min)/(N-1)
delta_y = (y_max-y_min)/(N-1)
x,y = np.meshgrid(x, y)
z=np.exp(-x**2-y**2)  

k_x = 2*np.pi*np.fft.fftfreq(N, d=delta_x)
k_y = 2*np.pi*np.fft.fftfreq(N, d=delta_y)
kx,ky = np.meshgrid(k_x, k_y)

n_fft = np.fft.fft2(z, norm='ortho') 
factor = np.exp(-1j * kx * x_min)*np.exp(-1j * ky * y_min)
aft = delta_x *delta_y* (N/(2.0*np.pi)) * factor * n_fft

##PLOTTING##
fig=plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(kx,ky,np.real(aft),cmap=cm.cool) 
ax1.set_title('Using numpy')
ax1.set_xlabel(r'$k_x$',fontsize=15)
ax1.set_ylabel(r'$k_y$',fontsize=15)
ax1.set_zlabel(r'$\tilde{f}(k_x,k_y)$',fontsize=20)
ax2 = fig.add_subplot(122, projection='3d')
kx,ky = np.meshgrid(k_x, k_y)
g_arr=0.5*np.exp(0.25*(-kx**2-ky**2))
ax2.plot_surface(kx,ky,g_arr,cmap=cm.hot) 
ax2.set_title('Analytical Solution')
ax2.set_xlabel(r'$k_x$',fontsize=15)
ax2.set_ylabel(r'$k_y$',fontsize=15)
ax2.set_zlabel(r'$\tilde{f}(k_x,k_y)$',fontsize=20)
plt.show()
