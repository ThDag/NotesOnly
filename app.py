import typer
import csv

app = typer.Typer()

# add note
@app.command()
def addn(note: str, classid: int=2):

    # check if Class got any invalid values
    if 4 <= classid or classid <= 0:
        raise ValueError('Classid parameter can only get; 1, 2, 3')

    # get the newest note_id
    with open('datas.csv', 'r') as file:
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
    with open('datas.csv', 'a') as file:
        data = csv.writer(file)
        data.writerow(note_data)

# view notes
@app.command()
def viewn(id: int):
    row_data = None

    # find the row with the id
    with open('datas.csv', 'r') as file:
        data = csv.reader(file)
        for row in data:
            if int(row[0]) == id:
                row_data = row

    # chck if id exists
    if row_data == None:
        print('id not found')
        return

    # print the result
    classes = {'1': 'upper',
               '2': 'middle',
               '3': 'lower'}
    print(row_data[0])
    print('---note---',f'{row_data[1]}',
          '---class--',f'{classes.get(str(row_data[-1]))}',
          sep='\n')

@app.command()
def viewc(classid: int):

    row_data =  [] 

    # find the rows with the class 
    with open('datas.csv', 'r') as file:
        data = csv.reader(file)
        for row in data:
            if int(row[2]) == classid:
                row_data.append(row) 

    # TODO also print the class number and print the id in the heading
    pretty_data = []
    for row in row_data:
        data = [row[1], ' | id:', row[0]]
        pretty_data.append(data)

    for i in pretty_data:
        print(i)




if __name__ == "__main__":
    app()
