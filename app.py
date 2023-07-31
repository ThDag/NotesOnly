from typing import Annotated
import typer
import csv
import os
import sys

app = typer.Typer()

classes = {'1': 'upper',
           '2': 'middle',
           '3': 'lower'}

# get the cwd 
pwd = os.path.dirname(__file__)

# gets all the data from the csv file 
def get_all_data():
    all_data = []
    with open(f'{pwd}/datas.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            all_data.append(i)
    return all_data


# add note                      
@app.command(help='add new note')
def addn(classid: Annotated[int, typer.Argument(help='id of the note\'s class')]=422):
    # the 422 is used as None with keeping it as int and when its 422 it will ask for input
    # for the classid its primarily used for the 'noon' command without the addn sub command
    if classid == 422:
        print('<====------========{class id}========------====>')
        try:
            classid = int(input('1/2/3 : '))
        except:
            print('only one of those options excepted.')
            return

    # check if Class got any invalid values
    if 4 <= classid or classid <= 0:
        raise ValueError('Classid parameter can only get; 1, 2, 3')

    note_id = len(get_all_data())

    print('<====------=========={note}==========------====>')
    note = input()
    print('<====------==========================------====>')

    # append the note
    note_data = [note, classid]
    with open(f'{pwd}/datas.csv', 'a') as file:
        data = csv.writer(file)
        data.writerow(note_data)

    print(f'note "{note}" class: {classid} id: {note_id} added.')

# edit note
@app.command(help = 'edit note with note id')
def editn(id: Annotated[str, typer.Argument(help='id of the note to edit')]):
    
    # getting all the datas
    all_data = get_all_data()


    if id == '00':
        print('--Note--', all_data[-1][0], '--Edited--', sep='\n')
        new_note = input()
        all_data[-1][0] = new_note
        

    else:
        try:
            int_id = int(id)

        except:
            print('note id is just number')
            return

        print('--Note--', all_data[int_id][0], '--Edited--', sep='\n')
        new_note = input()
        all_data[int_id][0] = new_note

    with open(f'{pwd}/datas.csv', 'w') as file:
        data = csv.writer(file)
        data.writerows(all_data)

    print('-------')


# delete note
@app.command(help='delete note')
def deln(id: Annotated[str, typer.Argument(help='id of the note to delete')]):

    # saving all the notes 
    all_data = get_all_data()
    print(all_data)
    
    if id == '00':
        # the last item in all_data
        deleted_note = all_data[-1][0]
        # delete last item
        all_data.pop()



    else:
        int_id = int(id)
        deleted_note = all_data[int_id][0]

        try:
            all_data.pop(int_id)
        except IndexError:
            print('Note with this id does not exist.')
            return

    with open(f'{pwd}/datas.csv', 'w') as file:
        data = csv.writer(file)
        data.writerows(all_data)

    print('note deleted:', deleted_note)

# view notes
@app.command(help='view note')
def viewn(id: Annotated[str, typer.Argument(help='id of the note to view')]):
    row_data = None
    all_data = get_all_data()

    if id == '00':
        row_data = all_data[-1]

    else:
        try:
            int_id = int(id)
        except:
            print('note id is just numbers')
            return

        try:
            row_data = all_data[int_id]
        except IndexError:
            print('Note with this id does not exist.')
            return

    # print the result
    print('---note---',f'{row_data[0]}',
          '---class--',f'{classes.get(str(row_data[-1]))}',
          sep='\n')

# view class
@app.command(help='view notes from class id')
def viewc(classid: Annotated[int, typer.Argument(help='id of the class to view')]):

    row_data =  [] 

    all_data = get_all_data()
    # all the items with the class id of Classid from all_data
    for id, row in enumerate(all_data):
        if row[-1] == str(classid):
            row = [id, row[0]]
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
    for id, row in enumerate(all_data):
        if len(row) >= 2: 
            data = [id, '|', row[0], '|', row[1]]
            pretty_data.append(data)

        else:
            print('keep in mind syntax is wrong')

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

# run the code command is used to check if the noon command is used alone then the __name__ == __main__ and the app()
# is not executed because it gives error saying it need a sub command etc (i couldent find a way to quit the code)
run_the_code = 1
if len(sys.argv) == 1:
    run_the_code = 0
    """
    after making the addn command interactive which means it will not ask for any arguments
    use addn() to run the code when there is no arguments spesified 
    currently it needs arguments which has to spesifed with sys.argv which is possible but
    i already have to make it interactive
    """
    addn()
    
if run_the_code:
    if __name__ == "__main__":
        app()
