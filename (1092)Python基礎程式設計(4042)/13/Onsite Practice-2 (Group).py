import time #引入時間函式庫
a=input('輸入兩個數字:') #輸入兩個數字，以逗號分隔，存入變數a
b=a.split(',') #以逗號分割字串，存入變數b
results=[int(i) for i in b] #將b陣列中每個資料轉為整數型態，存入results
print(results) #顯示result陣列
def lcm(x,y): #製作最小公倍數方法
  if x>y: #判斷x,y誰大誰小，比較大就用變數greater做儲存
    greater=x
  else:
    greater=y
  while(True):
    if((greater%x==0)and(greater%y==0)): #尋找最小公倍數，greater能整除兩個數代表為最小公倍數
      lcm=greater #找出最小公倍數，存入變數lcm
      break #找到第一個最小公倍數就離開迴圈
    greater+=1 #找不到就+1繼續找
  return lcm #回傳最小公倍數
def gcd(x,y): #製作最大公因數方法
  g=1 #假設沒有最大公因數，則公因數為1
  if x>y: #判斷x,y誰大誰小，比較大就用變數greater做儲存
    e=x
  else:
    e=y
  for k in range(e,2,-1): #從最大的數開始找最大公因數
    if x % k == 0 and y % k == 0: #若能整除兩個數代表為最大公因數
      g=k #找出最大公因數，存入變數g
      break #找到第一個最大公因數就離開迴圈
  print('最大公因數:%d'%(g))
start=time.time() #紀錄開始時間
c=lcm(results[0],results[1]) #呼叫尋找最小公倍數數的方法
end=time.time() #紀錄結束時間
d=end-start #計算尋找最小公倍數的時間
print('找到%d以及%d的最小公倍數:%d'%(results[0],results[1],c))
print('尋找所消耗時間:%f'%(d))
gcd(results[0],results[1]) #呼叫尋找最大公因數的方法