str1 = input('請輸入字串1:')                                                                        #輸入字串1
str2 = input('請輸入字串2:')                                                                        #輸入字串2
setA = set(str1)                                                                                   #轉換字串1為集合A
setB = set(str2)                                                                                   #轉換字串2為集合B
while (True):                                                                                      #重複執行程式
    N = int(input('1)找出重複的字元 2) 找出不重複的字元 3) 找出每個重複的字元各出現幾次 4) 離開程式:'))  #顯示選單，將輸入存入變數N
    if (N==4):                                                                                     #判斷N是否為4
        break                                                                                      #若是則離開程式
    if (N==1):                                                                                     #判斷N是否為1
        print(setA & setB)                                                                         #找出重複的字元(取兩集合的交集)
    elif (N==2):                                                                                   #判斷N是否為2
        print(setA ^ setB)                                                                         #找出不重複的字元(取兩集合的對稱差集)
    elif (N==3):                                                                                   #判斷N是否為3
        setR = setA & setB                                                                         #找出重複的字元(取兩集合的交集)，存入setR
        #for item in setR: print("{} 在字串1出現 {} 次".format(item,str1.count(item)))              #找出每個重複的字元，在字串1各出現幾次
        #for item in setR: print("{} 在字串2出現 {} 次".format(item,str2.count(item)))              #找出每個重複的字元，在字串2各出現幾次
        for item in setR: print("{} 總共出現 {} 次".format(item,str1.count(item)+str2.count(item))) #找出每個重複的字元，在兩字串總共出現幾次
    else:                                                                                          #判斷輸入1~4以外狀況
        continue                                                                                   #若非輸入1~4則重新輸入
print('End')                                                                                       #程式結束