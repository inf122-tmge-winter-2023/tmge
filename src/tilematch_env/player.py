"""
    :module_name: player
    :module_summary: A representation of a player in the tilematch game env
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""


class Player:
    Players = []
    
    def __init__(self, username):
        self._name = username
        Player.Players.append(self)

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    def list_players() -> list:
        return [p.name for p in Player.Players]
