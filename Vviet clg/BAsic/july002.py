'''
N = int(input("Number of elements in Fibonacci Series, N, (N>=2) : "))
fibonacciSeries = [0,1]
while ( N<2):{
    print("n greater than 2..."):
    int(input("Number of elements in Fibonacci Series, N, (N>=2) : "))
    }

if N>2:
    for i in range(2, N):
        nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
        fibonacciSeries.append(nextElement)
print(fibonacciSeries)
'''


'''
num = int(input("Enter a number: "))

factorial = 1
if num < 0:
    print("negative factorial n000")
while ( num < 0 ):{
    print("enter a positive no"):
    int(input("Enter a number: "))}
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)
         
for i in range(5):
    for j in range (i+1):
        print(chr(j+65),+i ,end=" ")
    print()

for  x in range(8):
    print(x)
    if x == 4:
        print("x is 4")
         continue
         '''
         
'''         
for i in range(10):
    if ((i % 2) == 0):
        i=i*2;
        print(i)
    else:
        print(i)
        continue
'''

"DATA STRUCTURE"
'''
group of elements combine togeater 
 list 
 tuples
 sets
 dictonary
 
    
