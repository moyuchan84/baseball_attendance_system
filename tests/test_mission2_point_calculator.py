from mission2.point_calculator import (
    BasicPlayerPointCalculator,
    TrainingDayPlayerPointCalculator,
    WeekendPlayerPointCalculator,
    PlayerPointCalculatorFactory,
)
from mission2.player import Player


def test_basic_player_point_calculator():
    # Arrange
    player = Player(1, "A")
    calc = BasicPlayerPointCalculator()
    # Act
    calc.apply_calculated_points(player)
    # Assert
    assert player.point == 1
    assert player.attendance_counter.basic_attendance_cnt == 1


def test_training_day_player_point_calculator():
    # Arrange
    player = Player(2, "B")
    calc = TrainingDayPlayerPointCalculator()
    # Act
    calc.apply_calculated_points(player)
    # Assert
    assert player.point == 3
    assert player.attendance_counter.training_day_attendance_cnt == 1


def test_weekend_player_point_calculator():
    # Arrange
    player = Player(3, "C")
    calc = WeekendPlayerPointCalculator()
    # Act
    calc.apply_calculated_points(player)
    # Assert
    assert player.point == 2
    assert player.attendance_counter.weekend_attendance_cnt == 1


def test_player_point_calculator_factory():
    # Arrange & Act
    calc_training = PlayerPointCalculatorFactory.create("wednesday")
    calc_weekend = PlayerPointCalculatorFactory.create("saturday")
    calc_basic = PlayerPointCalculatorFactory.create("monday")
    # Assert
    assert isinstance(calc_training, TrainingDayPlayerPointCalculator)
    assert isinstance(calc_weekend, WeekendPlayerPointCalculator)
    assert isinstance(calc_basic, BasicPlayerPointCalculator)
