import os

#1.練習利用While迴圈 來計算 n! 的總數

def factorial(n):
    result = 1
    while n>0:      #依輸入的數字，跑回圈次數，將每個數相乘
        result*=n
        n-=1
    return result

n = int(input('Please input a integer:'))
print(n,'!=',factorial(n),sep='')


#2. 利用 while loop完成 10進位轉2進位
def decTObin(dec):
    lis = []
    while dec>=2:              #當數字未小於2，代表還能輾轉相除
        lis.append(str(dec%2)) #將輾轉相除之餘數，存入陣列中
        dec//=2                #輾轉相除將數字除以2
    lis.append(str(dec))       #最後取MSD加入陣列中
    return ''.join(lis[::-1])  #lis[::-1]-反轉陣列；''.join-轉型成字串後回傳

n = int(input('Please input a integer:'))
print('{} to bitnary = {}'.format(n,decTObin(n)))


#3. 利用 while loop完成連續猜密碼，在猜密碼前先設定一組數字，只要猜錯即顯示”錯誤“，最多猜十次就結束程式，猜對就顯示”通關”，並且結束程式
def checkPassword(password,guest):
    return 'Bingo' if password==guest else 'error'

    """
    if password==guest:#判斷密碼是否與猜測相同
        return 'Bingo' #相同 回傳 "通關"
    else:
        return 'error' #不同 回傳 "錯誤"
    """
    
password = int(input('Please set a password:'))
guest = int(input('Guest a number:'))

counter = 1

while checkPassword(password,guest)=='error' and counter<10:  #記錄錯誤次數並告知，若猜錯10次則結束
    print(checkPassword(password,guest),'of',counter,'time!') #告知第幾次錯誤
    guest = int(input('Guest again:'))                        #請使用者重新再猜
    counter+=1                                                #記錄猜測次數
    
print('error of 10 time!\ngame over' if checkPassword(password,guest)=='error' else checkPassword(password,guest))
"""
if checkPassword(password,guest)=='error':
    print('error of 10 time!\ngame over')
else:
    print(checkPassword(password,guest))
"""

os.system("pause")