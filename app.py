from typing import Annotated, List, Optional
import typer
import csv
import os
import sys

app = typer.Typer()

'''
Commands:
addn; add note
deln; delete note
dela; delete all notes  
editn; edit note
viewn; view note
viewc; view class
viewa; view all
sern; search note
'''



classes = {'1': 'upper',
           '2': 'middle',
           '3': 'lower'}

# get the cwd 
pwd = os.path.dirname(__file__)

# gets all the data from the csv file 
def get_all_data():
    all_data = []
    with open(f'{pwd}/data.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            all_data.append(i)
    return all_data


def pretty_printing(id_numbers: List[int], heading: str) -> None:

    all_data = get_all_data()

    
    # the demanded data is the data demanded by the function caller  
    # and it's obtained by id numbers given for all_data 
    demanded_data = []
    for i in id_numbers:
        demanded_data.append(all_data[i])


    # this just adds pipeline between items in the data given to it.
    pretty_data = []
    for ind, row in enumerate(demanded_data):
        if len(row) >= 2: 
            data = [str(id_numbers[ind]), '|', row[0], '|', row[1]]
            pretty_data.append(data)

        else:
            print('data.csv has been touched (in a bad way)')

    # aligning the print file

    # get the longest note
    longest_note = 0
    for i in pretty_data:
        if len(i[2]) > longest_note:
            longest_note = len(i[2])

    # get the longest id (highest digit for alignment)
    longest_id = str(id_numbers[-1])
    # length_of_longest_id doesn't start counting from 0 it starts from 1
    length_of_longest_id = len(longest_id)


    # add spaces to the end of the note to make it evenly spaced
    for ind, i in enumerate(pretty_data):
        diffirence = longest_note - len(i[2])
        i[2] = i[2] + ' ' * diffirence
        pretty_data[ind][2] = i[2]

    # add spaced to the end of id numbers to make it evenly spaced
    for ind, i in enumerate(pretty_data):
        diffirence = length_of_longest_id - len(i[0])
        i[0] = i[0] + ' ' * diffirence
        pretty_data[ind][0] = i[0]
        

    print(f'----{heading}----')

    # aligning the id heading with the longest id
    id_heading_spaces = ' ' * (length_of_longest_id - 1)

    # aligning the note heading with the longest note
    note_heading_spaces = ' ' * (longest_note - 2)
    print(f'id{id_heading_spaces}|note{note_heading_spaces}|class')

    for i in pretty_data:
        print(i[0], i[1], i[2], i[3], i[4])

# add note                      
@app.command(help='add new note')
def addn(note: Annotated[Optional[str], typer.Argument(help='note itself')]=None, classid: Annotated[int, typer.Option(help='id of the note\'s class')]=2):

    # check if Class got any invalid values
    if 4 <= classid or classid <= 0:
        raise ValueError('Classid parameter can only get; 1, 2, 3')

    note_id = len(get_all_data())

    print('<====------=========={note}==========------====>')
    note = input()
    print('<====------==========================------====>')

    # append the note
    note_data = [note, classid]
    with open(f'{pwd}/data.csv', 'a') as file:
        data = csv.writer(file)
        data.writerow(note_data)

    print(f'note "{note}" class: {classid} id: {note_id} added.')

# edit note
@app.command(help = 'edit note with note id')
def editn(id: Annotated[str, typer.Argument(help='id of the note to edit')]):
    
    # getting all the data
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

    with open(f'{pwd}/data.csv', 'w') as file:
        data = csv.writer(file)
        data.writerows(all_data)

    print('-------')


# delete note
@app.command(help='delete note')
def deln(id: Annotated[List[str], typer.Argument(help='id of the note to delete')]):

    # saving all the notes 
    all_data = get_all_data()
    
    # deleted notes for visual feed back to the user
    deleted_notes = []

    if id == ['00']:
        # the last item in all_data
        deleted_notes.append(all_data[-1][0])
        # delete last item
        all_data.pop()

        with open(f'{pwd}/data.csv', 'w') as file:
            data = csv.writer(file)
            data.writerows(all_data)

        print('note(s) deleted:', all_data[-1][0])



    else:
        # gets the id's given from the user and sorts them in reverse order
        ids = tuple(int(num) for num in id)
        ids = tuple(sorted(ids, reverse=True))

        for i in ids:
            int_id = int(i)

            try:
                deleted_notes.append(all_data[int_id][0])
                all_data.pop(int_id)
            except IndexError:
                print('Note with this id does not exist.')
                return

        with open(f'{pwd}/data.csv', 'w') as file:
            data = csv.writer(file)
            data.writerows(all_data)

        # revesing the list so it will be in the right order as they are deleted
        deleted_notes.reverse()
        deleted_notes_str = ', '.join(deleted_notes)

        print('note(s) deleted:', deleted_notes_str)


# delete all notes
@app.command(help='delete all the notes')
def dela():
    print('!THIS WILL DELETE ALL THE NOTES!')
    a = input("Please type \'yes\' to comfirm: ")
    if a == 'yes':
        file = open(f'{pwd}/data.csv', 'w')
        file.close
        print('All the notes are deleted.')



    else:
        print('Deletion cancelled.')
        return

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
def viewc(classid: Annotated[str, typer.Argument(help='id of the class to view')]):

    # raises error if the class id is not number
    try:
        int(classid)
    except:
        print('Classid parameter can only get; 1, 2, 3')
        return

    # raise error if the class id is not 1, 2, 3
    if 4 <= int(classid) or int(classid) <= 0:
        print('Classid parameter can only get; 1, 2, 3')
        return

    all_ids = []

    all_data = get_all_data()
    # all the items with the class id of Classid from all_data
    for id, row in enumerate(all_data):
        if row[-1] == str(classid):
            all_ids.append(id)

    pretty_printing(all_ids, f'{classes.get(str(classid))}')

# view all notes
@app.command(help='view all the notes')
def viewa():

    all_data = get_all_data()

    # getting id of all the notes
    all_ids = []
    for ind in range(len(all_data)):
        all_ids.append(ind)

    pretty_printing(all_ids, 'all notes')



# Search notes
@app.command(help='search for notes')
def sern(class_id: Annotated[Optional[List[str]], typer.Argument(help='id of the class to search')] = None):

    # raises error if the class id is not number
    if class_id != None:
        for i in class_id:
            try:
                int(i)
            except:
                print('Classid parameter can only get; 1, 2, 3')
                return

    # raise error if the class id is not 1, 2, 3
    if class_id != None:
        for i in class_id:
            if 4 <= int(i) or int(i) <= 0:
                print('Classid parameter can only get; 1, 2, 3')
                return


    print('<====------========={search}=========------====>')
    search_query = input()
    print('<====------==========================------====>')


    # if class_id is empty then it will search for all the classes
    if class_id == []:
        class_id = ['1', '2', '3']

    # data of the results
    row_data = []

    all_data = get_all_data()

    # search for the query
    for id, row in enumerate(all_data):
        if search_query in row[0] and row[-1] in class_id:
            row = [id, row[0], row[1]]
            row_data.append(row)

    # make the data pretty
    pretty_data = []
    for row in row_data:
        data = [row[0], '|', row[1], '|', row[2]]
        pretty_data.append(data)

    # get the longest note
    longest_note = 0
    for i in pretty_data:
        if len(i[2]) > longest_note:
            longest_note = len(i[2])

    # add spaces to the end of the note to make it aligned
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
