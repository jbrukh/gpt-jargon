import click
import os

from .cli import JargonCli

@click.group(invoke_without_command=True)
@click.option('--jargon-dir', '-d', envvar='JARGON_DIR', default=os.path.expanduser('~/.jargon'), help="Manually set the Jargon directory.", type=str)
@click.pass_context
def cli(ctx, jargon_dir):
    ctx.obj = JargonCli(jargon_dir=jargon_dir)
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

@click.command()
@click.pass_context
def ls(ctx):
    '''List available Jargon procedures.'''
    for proc in ctx.obj.ls():
        click.echo(f'* {proc}')

@click.command()
@click.argument('proc')
@click.pass_context
def execute(ctx, proc):
    '''Execute a known procedure.'''
    try:
        ctx.obj.execute(proc)
    except Exception as e:
        click.echo(f"ERROR: {e}")

@click.command()
@click.argument('jargfile')
@click.pass_context
def edit(ctx, jargfile):
    '''Edit a procedure.'''
    jargdir = ctx.obj.jargdir
    if not jargfile.endswith('.jarg'):
        jargfile += '.jarg'
    filepath = os.path.join(jargdir, jargfile)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            file.write(f'+++ {jargfile[:-5]}\n\n+++')
    click.edit(filename=filepath)

cli.add_command(ls)
cli.add_command(execute)
cli.add_command(edit)

if __name__ == '__main__':
    cli()