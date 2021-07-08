#第一題
#ken,32,64,76#vicky,56,77,34#andy,87,56,41#sam,32,36,99
data_list = []

datass = input('Enter data:')
[data_list.append(list(map(lambda data:float(data) if data.isdigit() else data, datas.split(',')))) for datas in datass.split('#')]
print(data_list)

weights = input('Enter weight:')
weights = [float(weight) for weight in weights.split(',')]
print(weights)

data_dict = {}
for data in data_list : data_dict[data[0]] = [data[1],data[2],data[3]]

fuction_list = []
for index,weight in enumerate(weights):
    def index_weight(index,weight):
        def weight_score(data_dict):
            for key in data_dict:
                score = data_dict[key]
                score[index] = round(score[index]*weight,2)
                data_dict[key] = score
            return data_dict
        return weight_score
    fuction_list.append(index_weight(index,weight))

for key in data_dict : print('學生', key, '原始分數', data_dict[key])
print('#'*25,end='')
for fuction in fuction_list : data_dict = fuction(data_dict)
print('#'*25)
for key in data_dict : print('學生', key, '加權分數', data_dict[key])

sorted_list = sorted(data_dict, key=lambda key:round(sum(data_dict[key])), reverse=True)
print('#'*50)
for index,key in enumerate(sorted_list) : print('班上第{}名是{},加權總分為:{}'.format(index+1,key,round(sum(data_dict[key]))))
