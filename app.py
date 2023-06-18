import typer
import csv

app = typer.Typer()

@app.command()
def add_note(Text: str='null', Class: int=0):
    # fill here with using open() and csv module make datas.csv add a new column with note-id, Text, Class

    with open('a', 'datas.csv') as file:
        pass
    pass

print(something)

if __name__ == "__main__":
    app()
