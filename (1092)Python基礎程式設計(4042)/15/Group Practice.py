import time
a=input('輸入兩個數')
b=a.split(',')
x=int(b[0])
y=int(b[1])
def gcd_1(x,y):
  
  if x<y:
    z=x
  else:
    z=y
  for i in range(1,z+1):
    if x%i==0 and y%i==0:
      gcd=i
  return gcd
start1=time.time()
print("for迴圈計算結果",gcd_1(x,y))
end1=time.time()
def gcd_2(x,y):
  if y == 0:
    return x
  else:
    return gcd_2(y, x % y)
start2=time.time()
print("遞迴計算結果",gcd_2(x,y))
end2=time.time()
print("for迴圈共使用時間",end1-start1)
print("遞迴共使用時間",end2-start2)