from mission2.attendance_counter import AttendanceCounter


def test_is_removal_candidator_condition_true():
    # Arrange
    counter = AttendanceCounter()
    counter.training_day_attendance_cnt = 0
    counter.weekend_attendance_cnt = 0

    # Act
    result = counter.is_removal_candidator_condition

    # Assert
    assert result is True


def test_is_removal_candidator_condition_false_training():
    # Arrange
    counter = AttendanceCounter()
    counter.training_day_attendance_cnt = 1
    counter.weekend_attendance_cnt = 0

    # Act
    result = counter.is_removal_candidator_condition

    # Assert
    assert result is False


def test_is_removal_candidator_condition_false_weekend():
    # Arrange
    counter = AttendanceCounter()
    counter.training_day_attendance_cnt = 0
    counter.weekend_attendance_cnt = 2

    # Act
    result = counter.is_removal_candidator_condition

    # Assert
    assert result is False
