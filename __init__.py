import typer as tpr

app = tpr.Typer()

@app.command()
def foo(text: str):
    print(f'{text}')

if __name__ == "__main__":
    app()
