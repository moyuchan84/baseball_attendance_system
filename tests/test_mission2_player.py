from mission2.player import Player
from mission2.grade_enum import GradeEnum


def test_total_point_with_bonus():
    # Arrange
    player = Player(1, "A")
    player.point = 30
    player.attendance_counter.training_day_attendance_cnt = 10
    player.attendance_counter.weekend_attendance_cnt = 10
    # Act
    total = player.total_point
    # Assert
    assert total == 30 + 10 + 10


def test_grade_property():
    # Arrange
    player = Player(2, "B")
    player.point = 55
    # Act
    grade = player.grade
    # Assert
    assert grade == GradeEnum.GOLD


def test_is_removal_candidator_true():
    # Arrange
    player = Player(3, "C")
    player.point = 5
    player.attendance_counter.training_day_attendance_cnt = 0
    player.attendance_counter.weekend_attendance_cnt = 0
    # Act
    result = player.is_removal_candidator
    # Assert
    assert result is True


def test_is_removal_candidator_false():
    # Arrange
    player = Player(4, "D")
    player.point = 55
    player.attendance_counter.training_day_attendance_cnt = 1
    player.attendance_counter.weekend_attendance_cnt = 0
    # Act
    result = player.is_removal_candidator
    # Assert
    assert result is False
