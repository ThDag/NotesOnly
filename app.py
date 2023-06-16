import click

@click.group()
def note():
    pass

@click.option('--name', default='taha', help='give your name')
@click.command()
def test():
    click.echo('did a test :)')

@note.command()
def foo():
    click.echo('did second test')

if __name__ == '__main__':
    note()
    test()
    # foo()
