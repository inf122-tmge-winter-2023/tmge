"""
    :module_name: tilematch_env
    :module_summary: An environment supporting multiplayer tile matching games
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import logging
import tkinter as tk

from tilematch_tools import GameEngine

from columns_widget import ColumnsGameFactory
from candy_crush_widget import CCFactory

from .player import Player

LOGGER = logging.getLogger(__name__)
LOG_HANDLER = logging.StreamHandler()
LOG_FORMAT = logging.Formatter('[%(asctime)s|%(name)s|%(levelname)s] - %(message)s')

LOGGER.setLevel(logging.INFO)
LOG_HANDLER.setLevel(logging.INFO)

LOG_HANDLER.setFormatter(LOG_FORMAT)
LOGGER.addHandler(LOG_HANDLER)

class TMGE(GameEngine):
    AVAILABLE_GAMES = ('Columns', 'Candy Crush')
    def __init__(self):
        self._root = tk.Tk()
        self._game_factories = [ColumnsGameFactory, CCFactory]
        self._game_to_play = tk.StringVar()
        self._game_to_play.set(self.AVAILABLE_GAMES[0])
        self._create_default_players()
        self._player1 = tk.StringVar()
        self._player2 = tk.StringVar()
        self._player1.set(Player.list_players()[0])
        self._player2.set(Player.list_players()[1])

    def run(self):
        self._display_game_list()
        self._display_player_profiles()
        self._show_start_match_button()
        self._root.mainloop()

    def _display_game_list(self):
        options = tk.OptionMenu(self._root, self._game_to_play, *self.AVAILABLE_GAMES)
        options.configure(width=20)
        options.grid(column=1, row=0, padx=50, pady=50)

    def _display_player_profiles(self):
        p1_options = tk.OptionMenu(self._root, self._player1, *Player.list_players())
        p2_options = tk.OptionMenu(self._root, self._player2, *Player.list_players())
        p1_options.configure(width=20)
        p2_options.configure(width=20)
        p1_options.grid(column=0, row=1, padx=20, pady=20)
        p2_options.grid(column=2, row=1, padx=20, pady=20)

    def _show_start_match_button(self):
        start = tk.Button(self._root, text='Start!', width=20, height=2, relief=tk.RAISED)
        start.grid(column=1, row=2, padx=50, pady=50)

    def _create_default_players(self):
        Player('player 1')
        Player('player 2')

        
