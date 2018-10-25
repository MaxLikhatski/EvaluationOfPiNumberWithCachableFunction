def stepLeibniz(n,cache={}):
	if n not in cache:
		cache[n]=8/((4*n+1)*(4*n+3))
	return cache[n]
from numpy import linspace
from time import time
x = linspace(0,1000000,101)
print(x)
y=[]
startInstance = time()
for i in x:
    res = 0.0
    for j in range(0,int(i)):
        res+=stepLeibniz(j)
    y.append(res)
endInstance = time()
print(y)
print('Time consumed: %.6f' % (endInstance-startInstance))
