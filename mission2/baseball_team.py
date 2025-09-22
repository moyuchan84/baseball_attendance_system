from mission2.player import Player
from typing import Dict


class BaseballTeam:
    id: int = 1

    def __init__(self):
        self.players: Dict[str, Player] = dict()

    def get_player(self, name: str) -> Player:
        if name not in self.players:
            player = Player(BaseballTeam.id, name)
            BaseballTeam.id += 1
            self.players[name] = player
        return self.players[name]

    @property
    def player_list(self):
        return sorted(self.players.values(), key=lambda p: p.id)

    @property
    def removed_player(self):
        return [
            player for player in self.players.values() if player.is_removal_candidator
        ]
