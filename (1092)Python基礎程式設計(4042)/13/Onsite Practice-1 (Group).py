file=input('輸入5個任意檔案名稱:')#先輸入五個檔案名
x=file.split(',')#將輸入的字串切開
print(x)#印出
mylist=(i for i in x)#將x裡的資料逐一丟出，製作成generator，存入mylist
print(mylist)#印出mylist，將會顯示mylist為generator型態
print(mylist.__next__())#取得下次的值
print(next(mylist))#取得下次的值
for i in mylist:#取得mylist剩下的所有資料
  print(i)

#1.jpg,2.xls,3.jpg,4.csv,5.docx