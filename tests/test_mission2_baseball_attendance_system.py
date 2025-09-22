from mission2.baseball_attendance_system import BaseballAttendanceSystem
from mission2.baseball_team import BaseballTeam
import tempfile
import os


def test_parse_data_len_2(monkeypatch):
    # Arrange
    test_content = "Umar monday\nDaisy tuesday\nInvalidLine\n"
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as tmp:
        tmp.write(test_content)
        tmp_path = tmp.name

    system = BaseballAttendanceSystem(file_path=tmp_path)

    # Act
    system.parse_data()

    # Assert
    player_names = [p.name for p in system.baseball_team.player_list]
    assert "Umar" in player_names
    assert "Daisy" in player_names
    assert len(player_names) == 2  # Only valid lines processed

    # Clean up
    os.remove(tmp_path)


def test_parse_data_len_not_2(monkeypatch):
    # Arrange
    test_content = "OnlyOneField\nUmar monday\nToo Many Fields here\n"
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as tmp:
        tmp.write(test_content)
        tmp_path = tmp.name

    system = BaseballAttendanceSystem(file_path=tmp_path)

    # Act
    system.parse_data()

    # Assert
    player_names = [p.name for p in system.baseball_team.player_list]
    assert "Umar" in player_names
    assert len(player_names) == 1  # Only the valid line processed

    # Clean up
    os.remove(tmp_path)
