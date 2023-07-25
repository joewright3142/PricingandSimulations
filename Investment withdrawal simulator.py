###Brownian Motion
import numpy as np

Stock=100

time=1
steps=365*time
stepsize=1/365
drift=0.1
vol=0.2
Portfolio=np.zeros((100000,1))+100
#LogSt-Logs0=


def PortfolioSimulate(assets,stepsize=1/365,time=1,drift=0.1,vol=0.2):
    global Portfolio
    Portfolio=np.zeros((assets,1))+100
    steps=int(time/stepsize)
    for i in range(0,steps):
        for j in range(0,len(Portfolio)):
            rand=np.random.normal()
            Portfolio[j]=Portfolio[j]*np.exp(stepsize*(drift-0.5*vol**2)+vol*np.sqrt(stepsize)*rand)
    return Portfolio
    
def summarystats(x):
    print("Mean of Portfolio is", np.mean(x))
    print("St dev of Portfolio is", np.std(x))
    print("Max of Portfolio is", np.max(x))
    print("Min of Portfolio is", np.min(x))

PortfolioSimulate(100)
summarystats(Portfolio)

#Removing x% (of initial value) per annum

withdrawal=0.15
time=20
stepsize=1/365
drift=0.1
vol=0.3
steps=int(time/stepsize)
##withdraw annually

Portfolio=np.zeros((10,1))+100
for i in range(0,steps):
    for j in range(0,len(Portfolio)):
        rand=np.random.normal()
        Portfolio[j]=Portfolio[j]*np.exp(stepsize*(drift-0.5*vol**2)+vol*np.sqrt(stepsize)*rand)
        if i%365==0 and i!=0 and j==0: #annual withdrawal
            PortWdrawRatio=(withdrawal*100)/np.mean(Portfolio)
            Portfolio=Portfolio*(1-PortWdrawRatio)
            if Portfolio[0]<0:
                print("Gone broke in year", int(i/365))
                
                         
            
        
##require function to convert portfolio to initial wealth
summarystats(Portfolio)


