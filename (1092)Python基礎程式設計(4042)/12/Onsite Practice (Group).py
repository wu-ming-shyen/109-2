data=[]                                                                         #產生空的data串列

def insertValue(s):                                                             #建立一個insertValue方法，傳入值為s
        value_list = s.split(',')                                               #將串列切割後，存入value_list變數中，value_list為一個一維串列
        for index_value in value_list:                                          #取得value_list中的每一筆資料為index_value
            if (index_value.isdigit()):                                         #判斷index_value字串是否皆為數值
                index_value = float(index_value)                                #若是則將字串資料轉為浮點數
            else:
                index_value = index_value                                       #否則不轉換
        data.append(value_list)                                                 #將value_list一維串列，新增至data二維串列
        
while (True):
    s = input('請輸入-姓名,英文成績,數學成績,計概成績:')                          #輸入一筆姓名及成績的字串資料，並以,隔開
    if (s==''):                                                                 #判斷是否沒有輸入，直接按Enter
        break                                                                   #若是則離開迴圈
    #16~18 等同 3~10
    s = map(lambda x:float(x) if x.isdigit() else x, s.split(','))              #將切割後的s串列，以迭代方式，判斷每筆字串是否為數字，若是則將字串轉為浮點數，否則不轉換
    s = list(s)                                                                 #由於map特性會輸出為物件，因此轉換為串列
    data.append(s)                                                              #將處理過後的串列，新增至data串列
    #insertValue(s)                                                             #如果使用方法須呼叫才能使用
    print(data)                                                                 #每處理一筆字串，即列印data二維串列當前狀態
################################################################################
w = input('請輸入-英文權重,數學權重,計概權重:')                                   #輸入一筆成績權重的字串資料，並以,隔開
w = [float(i) for i in w.split(',')]                                            #將切割後的w串列，每一筆資料轉為浮點數，做成一個新的w串列
"""
new_w = []                                                                      #產生新的w串列
for i in w.split(','):                                                          #將切割後的每一筆資料，轉為浮點數
    new_w.append(float(i))                                                      #新增至新的w串列
print(new_w)                                                                    #列印新的w串列
"""
print(w)                                                                        #列印處理過後的w串列
################################################################################
[i.append((w[0]*i[1] + w[1]*i[2] + w[2]*i[3])) for i in data]                   #將data二為串列中，每個串列的成績進行加權後相加，新增至串列中
"""
for i in data:                                                                  #取出data二維串列的每一個一維串列，放入i中
    i.append(w[0]*i[1] + w[1]*i[2] + w[2]*i[3])                                 #將三個成績各自乘上加權值，相加後，新增至i一維串列中
"""
print(data)                                                                     #列印data二維串列
################################################################################
while (True):
    bit = input('請選擇- (1)大到小 (2)小到大 排序:')                             #輸入一筆1或2的資料
    if (bit == ''):                                                             #判斷是否沒有輸入，直接按Enter
        break                                                                   #若是則離開迴圈
################################################################################
    bit = True if int(bit)==1 else False                                        #註解如下
    """
    if (int(bit)==1):                                                           #判斷bit是否為1
        bit == True                                                             #若是則bit存取為真
    else:
        bit == False                                                            #否則bit存取為假
    """
################################################################################
    sorted_list = lambda bit:sorted(data, key=lambda data:data[-1], reverse=bit)
    """
    def return_avg(oneD_list):                                                  #建立一個，能回傳一維陣列中最後一筆值(加權平均值)的方法
        return oneD_list[-1]                                                    #回傳一維串列中的最後一筆值
    def return_sorted_list(data,bit):                                           #建立一個，能回傳排序後串列的方法
        sorted_list = sorted(data, key=return_avg, reverse=bit)                 #取得data二維串列，每一筆一維串列，並使用回傳加權平均數的方法，最後輸出排序好的二為串列
        #sorted(key方法的傳入值,要呼叫的方法,是否要反轉串列)
        return sorted_list                                                      #回傳已排序的二維串列
    sorted_list = return_sorted_list(data,bit)                                  #呼叫排序的方法
    """
    print(sorted_list(bit))                                                     #列印排序後的二維串列
    