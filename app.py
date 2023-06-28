import typer
import csv
import os

app = typer.Typer()


classes = {'1': 'upper',
           '2': 'middle',
           '3': 'lower'}

# get the cwd 
pwd = os.path.dirname(__file__)
print(pwd)

def get_all_data():
    all_data = []
    with open(f'{pwd}/datas.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            all_data.append(i)
    return all_data



# add note
@app.command(help='add new note')
def addn(note: str, classid: int=2):

    # check if Class got any invalid values
    if 4 <= classid or classid <= 0:
        raise ValueError('Classid parameter can only get; 1, 2, 3')

    note_id = len(get_all_data()) + 1

    # append the note
    note_data = [note_id, note, classid]
    with open(f'{pwd}/datas.csv', 'a') as file:
        data = csv.writer(file)
        data.writerow(note_data)

    print(f'note "{note}" added id:', note_id)

# edit note
@app.command(help = 'edit note with note id')
def editn(id: int):
    
    # getting all the datas
    all_data = get_all_data()


    print('--Note--', all_data[id][1], '--Edited--', sep='\n')
    new_note = input()
    all_data[id][1] = new_note

    with open(f'{pwd}/datas.csv', 'w') as file:
        data = csv.writer(file)
        data.writerows(all_data)

    print('-------')


# delete note
@app.command(help='delete note')
def deln(id: int):

    # saving all the notes 
    all_data = get_all_data()
    deleted_note = all_data[id][1]

    try:
        all_data.pop(id)
    except IndexError:
        print('Note with this id does not exist.')
        return

    # Update the index numbers of the remaining items
    all_data = [[index, item[1], item[2]] for index, item in enumerate(all_data)]

    with open(f'{pwd}/datas.csv', 'w') as file:
        data = csv.writer(file)
        data.writerows(all_data)

    print('note deleted:', deleted_note)

# view notes
@app.command(help='view note')
def viewn(id: int):
    row_data = None

    # find the row with the id
    with open(f'{pwd}/datas.csv', 'r') as file:
        data = csv.reader(file)
        for row in data:
            if int(row[0]) == id:
                row_data = row

    # chck if id exists
    if row_data == None:
        print('id not found')
        return

    # print the result
    print('---note---',f'{row_data[1]}',
          '---class--',f'{classes.get(str(row_data[-1]))}',
          sep='\n')

# view class
@app.command(help='view notes from class id')
def viewc(classid: int):

    row_data =  [] 

    # find the rows with the class 
    with open(f'{pwd}/datas.csv', 'r') as file:
        data = csv.reader(file)
        for row in data:
            if row[2] == str(classid):
                row_data.append(row) 

    # make the data pretty
    pretty_data = []
    for row in row_data:
        data = [row[0], '|', row[1]]
        pretty_data.append(data)

    # print the result
    print(f'--{classes.get(str(classid))}--')
    for i in pretty_data:
        print(i[0], i[1], i[2])

# view all notes
@app.command(help='view all the notes')
def viewa():

    # saving all the notes 
    all_data = get_all_data()   

    # make the data pretty
    pretty_data = []
    for row in all_data:
        if len(row) >= 3: 
            data = [row[0], '|', row[1], '|', row[2]]
            pretty_data.append(data)

    print('----all notes----')
    print('--id|note|class--')
    for i in pretty_data:
        print(i[0], i[1], i[2], i[3], i[4])



if __name__ == "__main__":
    app()
