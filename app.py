import typer
import csv

app = typer.Typer()

@app.command()
def add_note(note: str, classid: int=2):

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


if __name__ == "__main__":
    app()
