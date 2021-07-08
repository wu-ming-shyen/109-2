import os
name = None
score = None
dicts = {}
sets = {}
while(name != ''):
    name = input('Please input name:')
    if (name == ''):
        break
    score = input('Please input score:')
    if (score.isdigit()):
        dicts[name] = int(score)
    else:
        dicts[name] = 0
    print(dicts)
    
for key,value in dicts.items():
    print('Student {} has a score of {}'.format(key, value))

print('The types of scores:{}'.format(set(dicts.values())))

os.system("pause")