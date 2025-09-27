# Fourier series analysis for a sqaure wave function
# user defined function
import numpy as np
from scipy.signal import square
import matplotlib.pyplot as plt
from scipy.integrate import simpson as simps

L=4 # Periodicity of the periodic function f(x)
freq=4 # No of waves in time period L
dutycycle=0.5
samples=1000
terms=100
# Generation of square wave
x=np.linspace(0,L,samples,endpoint=False)
y=square(2.0*np.pi*x*freq/L,duty=dutycycle)
# Calculation of Fourier coefficients
a0=2./L*simps(y,x)
an=lambda n:2.0/L*simps(y*np.cos(2.*np.pi*n*x/L),x)
bn=lambda n:2.0/L*simps(y*np.sin(2.*np.pi*n*x/L),x)
# sum of the series
s=a0/2.+sum([an(k)*np.cos(2.*np.pi*k*x/L)+bn(k)*np.sin(2.*np.pi*
k*x/L) for k in range(1,terms+1)])
# Plotting
plt.plot(x,s,label="Fourier series")
plt.plot(x,y,label="Original square wave")
plt.xlabel("$x$")
plt.ylabel("$y=f(x)$")
plt.legend(loc='best',prop={'size':10})
plt.title("Sqaure wave signal analysis by Fouries series")
plt.savefig("fs_square.png")
plt.show()
