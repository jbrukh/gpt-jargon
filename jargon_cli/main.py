import click
import os

from .cli import JargonCli

@click.group(invoke_without_command=True)
@click.option('--jargon-dir', '-d', envvar='JARGON_DIR', default=os.path.expanduser('~/.jargon'), help="Manually set the Jargon directory.", type=str)
@click.option('--model', '-m', envvar='JARGON_CLI_MODEL', default='gpt-4')
@click.option('--temperature', '-t', default=0.35, type=float)
@click.pass_context
def cli(ctx, jargon_dir, model, temperature):
    ctx.obj = JargonCli(jargon_dir=jargon_dir, model_name=model, temperature=temperature)
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

@click.command()
@click.pass_context
def ls(ctx):
    '''List available Jargon procedures.'''
    ctx.obj.ls()

@click.command()
@click.argument('proc')
@click.pass_context
def execute(ctx, proc):
    '''Execute a known procedure.'''
    ctx.obj.execute(proc)
    
@click.command()
@click.argument('proc')
@click.pass_context
def edit(ctx, proc):
    '''Edit a Jargon procedure and go to the CLI.'''
    ctx.obj.edit(proc)

@click.command(name='cli')
@click.pass_context
def cmdline(ctx):
    '''Start the Jargon CLI with autocompletion.'''
    ctx.obj.cli()


cli.add_command(ls)
cli.add_command(execute)
cli.add_command(edit)
cli.add_command(cmdline)

if __name__ == '__main__':
    cli()