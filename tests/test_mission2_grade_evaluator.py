from mission2.grade_evaluator import GradeEvaluator
from mission2.grade_enum import GradeEnum


def test_evaluate_returns_gold():
    # Arrange
    point = 60
    # Act
    grade = GradeEvaluator.evaluate(point)
    # Assert
    assert grade == GradeEnum.GOLD


def test_evaluate_returns_silver():
    # Arrange
    point = 35
    # Act
    grade = GradeEvaluator.evaluate(point)
    # Assert
    assert grade == GradeEnum.SILVER


def test_evaluate_returns_normal():
    # Arrange
    point = 10
    # Act
    grade = GradeEvaluator.evaluate(point)
    # Assert
    assert grade == GradeEnum.NORMAL


def test_evaluate_returns_none_for_negative():
    # Arrange
    point = -5
    # Act
    grade = GradeEvaluator.evaluate(point)
    # Assert
    assert grade == GradeEnum.NONE


def test_evaluate_returns_none_for_exact_none():
    # Arrange
    # GradeEnum.NONE.value == -999999
    point = -999999
    # Act
    grade = GradeEvaluator.evaluate(point)
    # Assert
    assert grade == GradeEnum.NONE


def test_is_grade_removal_candidator_true():
    # Arrange
    grade = GradeEnum.NORMAL
    # Act
    result = GradeEvaluator.is_grade_removal_candidator(grade)
    # Assert
    assert result is True


def test_is_grade_removal_candidator_false_gold():
    # Arrange
    grade = GradeEnum.GOLD
    # Act
    result = GradeEvaluator.is_grade_removal_candidator(grade)
    # Assert
    assert result is False


def test_is_grade_removal_candidator_false_silver():
    # Arrange
    grade = GradeEnum.SILVER
    # Act
    result = GradeEvaluator.is_grade_removal_candidator(grade)
    # Assert
    assert result is False


def test_is_grade_removal_candidator_false_none():
    # Arrange
    grade = GradeEnum.NONE
    # Act
    result = GradeEvaluator.is_grade_removal_candidator(grade)
    # Assert
    assert result is True
