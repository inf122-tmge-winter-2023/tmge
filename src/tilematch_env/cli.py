"""
    :module_name: cli
    :module_summary: a CLI for tilematch_env
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import click

from tilematch_tools import GameEngine
from columns_widget import ColumnsGameFactory

@click.command()
def tmge():
    """Entry point to tmge"""
    ge = GameEngine(
            [
                ColumnsGameFactory.create_game(),
                ColumnsGameFactory.create_game()
                ]
    )
    ge.run()
