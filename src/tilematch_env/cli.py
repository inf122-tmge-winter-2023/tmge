"""
    :module_name: cli
    :module_summary: a CLI for tilematch_env
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import click

@click.command()
def tmge():
    """Entry point to tmge"""
    click.echo('Hello World!')
