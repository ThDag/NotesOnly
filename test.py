import csv
import os

pwd = os.path.dirname(__file__)

def get_all_data():
    all_data = []
    with open(f'{pwd}/datas.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            all_data.append(i)
    return all_data

# saving all the notes 
all_data = get_all_data()   

# make the data pretty
pretty_data = []
for id, row in enumerate(all_data):


    if len(row) >= 2: 


        data = [id, '|', row[0], '|', row[1]]
        pretty_data.append(data)

    else:
        print('syntax is wrong')

# aligning the print file
# get the longest note
longest_note = 0
for i in pretty_data:
    if len(i[2]) > longest_note:
        longest_note = len(i[2])

for ind, i in enumerate(pretty_data):
    diffirence = longest_note - len(i[2])
    i[2] = i[2] + ' ' * diffirence
    pretty_data[ind][2] = i[2]
    


print('----all notes----')
print('--id|note|class--')
for i in pretty_data:
    print(i[0], i[1], i[2], i[3], i[4])
