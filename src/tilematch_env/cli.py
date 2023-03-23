"""
    :module_name: cli
    :module_summary: a CLI for tilematch_env
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import click

from tilematch_tools import GameEngine
from columns_widget.cli import columns_init

@click.command()
def tmge():
    """Entry point to tmge"""
    ge = GameEngine([columns_init(), columns_init()])
    ge.run()
