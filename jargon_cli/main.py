import click
import os

from .cli import JargonCli

@click.group()
@click.option('--jargon-dir', '-d', envvar='JARGON_DIR', default=os.path.expanduser('~/.jargon'), help="Manually set the Jargon directory.", type=str)
@click.pass_context
def cli(ctx, jargon_dir):
    ctx.obj = JargonCli(jargon_dir=jargon_dir)

@click.command()
@click.pass_context
def ls(ctx):
    '''List available Jargon procedures.'''
    for proc in ctx.obj.ls():
        print('--', proc)

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