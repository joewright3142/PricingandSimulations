import math

 
# Calculate the value of n choose r using the binomial coefficient formula
# Calculate the value of n choose r using the binomial coefficient formula
def combs(n,r):
    sum=1
    for i in range(1, r+1):
        sum = sum * (n - r + i) / i
    return sum 

def f(n,k,g):
    res=0
    for i in range(n):
        res+=((n-i)**(g))*((-1)**i)*combs(n,i)
    return res

print(f(5,5,5))





for k in range(3,10):
    print("###########"+str(k)+"#########")
    for j in range(10):
        l=f(k,0,k+j)
        print(l/math.factorial(k))
        
def f2(n,k,g)        
mod=10**9+7
computed={}
def stirling2(n, k):
    key = (n,k)

    if key in computed:
        return computed[key]
    if n == k == 0:
        return 1
    if (n > 0 and k == 0) or (n == 0 and k > 0):
        return 0
    if n == k:
        return 1
    if k > n:
        return 0
    result = k * stirling2(n - 1, k)%mod + stirling2(n - 1, k - 1)%mod
    computed[key] = result%mod
    return result



  return ((math.factorial(n)%mod)*(stirling2(goal-k,n-k))%mod)%mod
