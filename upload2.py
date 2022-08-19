###Brownian Motion
import numpy

Stock=100
time=1
steps=365*time
stepsize=1/365
drift=0.1
vol=0.2
currenttime=0

#LogSt-Logs0=
for i in range(0,steps):
    rand=numpy.random.normal(0,1)
    Stock=Stock*numpy.exp(stepsize*(drift-0.5*vol**2)+vol*np.sqrt(stepsize)*rand)
    print(Stock)
    