import csv



# append note
def add_note(Note: str, Class: int=2):
    global note_id

    # check if Class got any invalid values
    if 4 <= Class or Class <= 0:
        raise ValueError('Class parameter can only get; 1, 2, 3')

    # get the newest note_id
    with open('datas.csv', 'r') as file:
        data = csv.reader(file)
        last_row = None
        for row in data:
            last_row = row

        print(f'1{last_row}')

        if last_row:
            note_id = int(last_row[0]) + 1
        else:
            note_id = 0

        print(f'2{note_id}')

    print(f'3{note_id}')

    # append the note
    note_data = [note_id, Note, Class]
    with open('datas.csv', 'a') as file:
        data = csv.writer(file)
        data.writerow(note_data)
        
for i in range(4):
    inpput = input('text:')
    classs = input('class:')
    add_note(inpput, int(classs))


"""
with open('datas.csv', 'r') as file:
    data = csv.reader(file)
    print(type(data))
    for row in data:
        print(data)
"""
