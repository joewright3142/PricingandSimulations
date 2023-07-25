import time
import random
import numpy
import math
class Tools:
    def __init__(self,good):
        self.good=good
    


tic=time.perf_counter()
for i in range(10**6):
    random.gauss(0,1)
toc=time.perf_counter()

tic2=time.perf_counter()
for i in range(10**6):
    numpy.random.normal()
toc2=time.perf_counter()
print("\nRunning time random = {} ms".format(int((toc-tic)*10**3))+
      "\nRunning time np.normal = {} ms".format(int((toc2-tic2)*10**3)))
#we use random.gauss due to it's ability to generate normal draws more quickly!


vol=0.1
t=1/365
sqrtt=math.sqrt(t)
mu=0.05 #drift
Spot=100
Strike=105

#dS=mu*S*dt+sigma*dWt
totsum=0
sims=10000

for j in range(sims):
    Spot=100
    for i in range(365):
        N01=random.gauss(0,1)
        Spot=Spot*(1+(mu*t+vol*sqrtt*N01))  #in this discrete approximate model we can go negative!!
    totsum+=Spot

mean=totsum/sims
#The mean represents the expected value of the asset or option
#- in this exercise we will be analysing various payoffs via MC to their BS price
#Section one looks at pricing
#Fwd Contract
#Call
#barrier
#straddle
#Asian option
#CDO
#CDO Sq

#####Section I###
##Forward contract.




##Section two will look at pricing under different assumptions, specifically stochastic volatility

##Section three will pull data via apis and compare with pricing and observed volatilities