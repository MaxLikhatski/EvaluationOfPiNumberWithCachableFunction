def stepLeibniz(n,cache={}):
	'''The function returns a member of Leibniz series, which approximates the value of Pi number.''' 
	if n not in cache:#here, we're looking for n-th member of Leibniz series, which can be evaluated previously
		cache[n]=8/((4*n+1)*(4*n+3))
	return cache[n]#here, we're saving the result of evaluation in the dictionary named cache
from numpy import linspace #the function we use bellow for making an array containing values of member number in Leibniz series
from time import time #using the function time() from module time, we measure time of function operation
x = linspace(0,1000000,101) #creating the array, which contains high limits of Leibniz series
print(x) #just to show that array
y=[] #This array will serve as a storage to keep the results of evaluation
startInstance = time() #it calls just to keep the instance of calculation start
#Inside the loop, the values of Pi number are evaluated.The evaluation is ended to give rise to the resulting array y.
for i in x:
    res = 0.0
    for j in range(0,int(i)):
        res+=stepLeibniz(j)
    y.append(res)
endInstance = time() #Here, we're storing time again
print(y)#the evaluation results are printed out.
print('Time consumed: %.6f' % (endInstance-startInstance))#In conclusion, we print out time consumed by evaluation process
