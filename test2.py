
data = [
    [0, 'data0'],
    [1, 'data1'],
    [2, 'data2'],
    [3, 'data3'],
]

# Identify the index number of the item you want to delete
index_to_delete = 1

# Remove the item from the data list
del data[index_to_delete]

# Update the index numbers of the remaining items
data = [[index, item[1]] for index, item in enumerate(data)]

# Print the updated data
for item in data:
    print(item)
