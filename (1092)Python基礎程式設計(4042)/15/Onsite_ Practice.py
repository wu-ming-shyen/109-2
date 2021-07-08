import time

#factorial = lambda n:1 if n==1 else n*factorial(n-1)

def factorial_1(n):
    f=1
    for i in range(n,0,-1):
        f*=i
    return f
    
def factorial_2(n):
    if (n==1):
        print('factorial_2(1)=1')
        return 1
    else:
        print('factorial_2({0})={0}*factorial_2({0}-1)={0}*factorial_2({1})'.format(n,n-1,))
        return n*factorial_2(n-1)

n = int(input('Enter n:'))

start1 = time.time()
print(factorial_1(n))
end1 = time.time()

start2 = time.time()
print(factorial_2(n))
end2 = time.time()

print('for loop 總共花了',(end1-start1)*1000,'ms')
print('遞迴 總共花了',(end2-start2)*1000,'ms')