import typer
import csv

app = typer.Typer()


classes = {'1': 'upper',
           '2': 'middle',
           '3': 'lower'}

# add note
@app.command(help='add new note')
def addn(note: str, classid: int=2):

    # check if Class got any invalid values
    if 4 <= classid or classid <= 0:
        raise ValueError('Classid parameter can only get; 1, 2, 3')

    # get the newest note_id
    with open('/Users/mac/desktop/programming/notesonly/datas.csv', 'r') as file:
        data = csv.reader(file)
        last_row = None
        for row in data:
            last_row = row

        if last_row:
            note_id = int(last_row[0]) + 1
        else:
            note_id = 0

    # append the note
    note_data = [note_id, note, classid]
    with open('/Users/mac/desktop/programming/notesonly/datas.csv', 'a') as file:
        data = csv.writer(file)
        data.writerow(note_data)

    print(f'note "{note}" added id:', note_id)

# edit note
@app.command(help = 'edit note with note id')
def editn(id: int):
    
    # getting all the datas
    all_data = []
    with open('/Users/mac/desktop/programming/notesonly/datas.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            all_data.append(i)


    print('--Note--', all_data[id][1], '--Edited--', sep='\n')
    new_note = input()
    all_data[id][1] = new_note

    with open('/Users/mac/desktop/programming/notesonly/datas.csv', 'w') as file:
        data = csv.writer(file)
        data.writerows(all_data)

    print('-------')


# delete note
@app.command(help='delete note')
def deln(id: int):

    # saving all the notes 
    all_data = []
    with open('/Users/mac/desktop/programming/notesonly/datas.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            all_data.append(i)

    try:
        all_data.pop(id)
    except IndexError:
        print('Note with this id does not exist.')
        return

    # Update the index numbers of the remaining items
    all_data = [[index, item[1], item[2]] for index, item in enumerate(all_data)]

    with open('/Users/mac/desktop/programming/notesonly/datas.csv', 'w') as file:
        data = csv.writer(file)
        data.writerows(all_data)

    print('note deleted:', all_data[id - 1][1])

# view notes
@app.command(help='view note')
def viewn(id: int):
    row_data = None

    # find the row with the id
    with open('/Users/mac/desktop/programming/notesonly/datas.csv', 'r') as file:
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
    with open('/Users/mac/desktop/programming/notesonly/datas.csv', 'r') as file:
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
    all_data = []
    with open('/Users/mac/desktop/programming/notesonly/datas.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            all_data.append(i)
    
    # deleting heading row
    del all_data[0]
    
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
