from mission2.baseball_team import BaseballTeam
from mission2.player import Player


class DummyPlayer(Player):
    def __init__(self, id, name):
        super().__init__(id, name)


def test_get_player_and_player_list():
    # Arrange
    team = BaseballTeam()
    p1 = team.get_player("Umar")
    p2 = team.get_player("Daisy")
    p3 = team.get_player("Umar")
    # Act & Assert
    assert p1 is p3
    assert p1.name == "Umar"
    assert p2.name == "Daisy"
    assert len(team.player_list) == 2


def test_removed_player_property():
    # Arrange
    team = BaseballTeam()
    team.players["Bob"] = DummyPlayer(1, "Bob")
    team.players["Zane"] = DummyPlayer(2, "Zane")
    # Act
    removed = team.removed_player
    # Assert
    assert len(removed) == 2
