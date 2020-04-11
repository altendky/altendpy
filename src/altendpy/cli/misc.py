import pathlib

import click

import altendpy.processtemplates


@click.command()
@click.option(
    '--root',
    default='.', type=click.Path(file_okay=False),
    help='Recursively search this directory for templates',
    show_default = True,
)
@click.option(
    '--suffix',
    default='_template',
    help='Extension suffix used to identify templates',
    show_default=True,
    type=str,
)
def processtemplates(root, suffix):
    """Search for and process templates"""

    root = pathlib.Path(root)
    altendpy.processtemplates.process_root(
        root=root,
        suffix=suffix,
        output=click.echo,
    )
