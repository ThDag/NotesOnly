import typer as tpr

app = tpr.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def goodbye(nume: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {nume}. Have a good day.")
    else:
        print(f"Bye {nume}!")

if __name__ == "__main__":
    app()

