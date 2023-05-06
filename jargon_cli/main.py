import click

@click.group()
def cli():
    pass

@click.command()
def ls():
    '''List available Jargon procedures.'''
    pass

@click.command()
def execute():
    '''Execute a known procedure.'''
    pass

@click.command()
# @click.option('--name', default='User', help='Your name')
def edit():
    '''Edit a procedure.'''
    pass

cli.add_command(ls)
cli.add_command(execute)
cli.add_command(edit)

if __name__ == '__main__':
    cli()