###Brownian Motion
import numpy

Stock=100
time=1
steps=365*time
stepsize=1/365
drift=0.05
vol=0.1
currenttime=0


for i in range(0,steps):
    Stock=Stock*numpy.exp(stepsize*drift)
    