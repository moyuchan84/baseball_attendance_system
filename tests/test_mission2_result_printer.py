from mission2.result_printer import ResultPrinter
from mission2.player import Player
from mission2.grade_enum import GradeEnum
import sys
from io import StringIO


def test_print_player_status(monkeypatch):
    # Arrange
    player1 = Player(1, "A")
    player1.point = 48
    player2 = Player(2, "B")
    player2.point = 45
    players = [player1, player2]
    expected = (
        "NAME : A, POINT : 48, GRADE : SILVER\n"
        "NAME : B, POINT : 45, GRADE : SILVER\n"
    )
    captured = StringIO()
    monkeypatch.setattr(sys, "stdout", captured)
    # Act
    ResultPrinter.print_player_status(players)
    # Assert
    sys.stdout = sys.__stdout__
    assert captured.getvalue() == expected


def test_print_removed_player_list(monkeypatch):
    # Arrange
    player1 = Player(1, "A")
    player2 = Player(2, "B")
    removed_players = [player1, player2]
    expected = "\nRemoved player\n==============\nA\nB\n"
    captured = StringIO()
    monkeypatch.setattr(sys, "stdout", captured)
    # Act
    ResultPrinter.print_removed_player_list(removed_players)
    # Assert
    sys.stdout = sys.__stdout__
    assert captured.getvalue() == expected
