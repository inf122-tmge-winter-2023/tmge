"""
    :module_name: cli
    :module_summary: a CLI for tilematch_env
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import click

from . import TMGE

@click.command()
def tmge():
    """Entry point to tmge"""
    TMGE().run()
