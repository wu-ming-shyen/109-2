data = [0, -4, -2, 1, 0, 7, -5, 3, 0, 1, 1, 0, -4, 2, 4, -4, 4, 5, -3, 1, 3, 0, 0, -4, -6, 3, 1, 0, 2, 1, 0, 4, -3, 5, 1, -2, 1, 1, 3, -6, -3, 2, 2, -5, 2, 5, -5, -4, -7, 7, 0, 3, -8, -6, 5, -2, 0, 0, -3, -3, 0, 4, 0, 0, 3, 0, 0, 0, 0, -1, 3, 0, -3, 3, 0, -4, 2, 0, -4, 0, 0, 0, 0, 1, -1, -6, 0, -1, 8, 0, -1, -6, -7, 3, -9, 0, 0, 3, 4, -2, 6, 3, -3, 2, 1, 0, 3, -7, -5, -1, 0, 2, -3, -1, -1, 1, -6, 3, -3, 1, 4, -3, -2, 2, -1, 0, 1, -3]

data_set = set(data)
print(data_set)

data_times = []
for i in data_set:
    data_times.append(data.count(i))
print(data_times)