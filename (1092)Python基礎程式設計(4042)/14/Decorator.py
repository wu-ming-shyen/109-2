#第二題
data_string = input('Enter data:')
weight_string = input('Enter weight:')
data_dict = {}

def convert(fuction):
  def inner_fun(*args):
    data_string, weight_string = args[0], args[1]

    datass = data_string.split('#')
    for datas in datass:
        data = datas.split(',')
        data_dict[data[0]] = [float(data[1]),float(data[2]),float(data[3])]
    #print(data_dict)

    weights = weight_string.split(',')
    for i in range(len(weights)):
        weights[i] = float(weights[i])
    #print(weights)

    return fuction(data_dict,weights)
  
  return inner_fun

@convert
def wrapper(*args):
    data_dict,weights = args[0], args[1]
    for key in data_dict:
        score = data_dict[key]
        data_dict[key] = [round(score[0]*weights[0],2),round(score[1]*weights[1],2),round(score[2]*weights[2],2)]
    return data_dict

data_dict = wrapper(data_string,weight_string)
print('#'*50)
for key in data_dict : print('學生', key, '加權分數', data_dict[key])

sorted_list = sorted(data_dict, key=lambda key:round(sum(data_dict[key])), reverse=True)
print('#'*50)
for index,key in enumerate(sorted_list):
    print('班上第{}名是{},加權總分為:{}'.format(index+1,key,round(sum(data_dict[key]))))