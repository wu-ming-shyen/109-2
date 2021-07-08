s = None
dic = {}
while (s != ''):
    s = input('請輸入姓名及分數:')                             #只有一個輸入，同時輸入姓名與分數，並以逗號分開
    if (s == ''):                                             #如果沒有輸入直接按Enter，則直接離開迴圈
        break
    print(s)                                                  #印出輸入的字串(Str)
    
    lis = s.split(',')                                        #將字串用"，"分隔開來，回傳一個串列(list)
    print(lis)                                                #印出分隔後的串列(list)
    
    dic[lis[0]] = int(lis[1]) if lis[1].isdigit() else 0      #註解如下
    """
    if (s[1].isdigit()):                                      #判斷字串內容是否為數字，若字串皆為數字
        dic[s[0]] = int(s[1])                                 #則將字串轉為整數，並新增於字典中
    else:                                                     #若串非完全為數字
        dic[s[0]] = 0                                         #則設值為0，並新增於字典中
    """
    print(dic)                                                #印出字典內的所有資料
    
print()                                                       #分隔段落，方便閱讀
for key,value in dic.items():                                 #將字典的鍵與值分別丟入key,value當中，一次一筆，丟完為止
    print('學生{}之分數為{}'.format(key,value))                #印出學生姓名及分數

print()                                                       #分隔段落，方便閱讀
scores = dic.values()                                         #將字典中所有的值，丟入scores當中，形成一個分數串列
score = set(scores)                                           #將scores串列轉換為集合，丟入score當中
print('總共出現的分數有:{}\nProgram terminated!'.format(score))#印出所有分數類別
