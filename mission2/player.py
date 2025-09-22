from mission2.attendance_counter import AttendanceCounter
from mission2.grade_enum import GradeEnum
from mission2.grade_evaluator import GradeEvaluator

BONUS_ATTENDANCE_POINT = 10
BONUS_ATTENDANCE_LIMIT = 10


class Player:
    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name
        self.point: int = 0
        self.attendance_counter: AttendanceCounter = AttendanceCounter()

    @property
    def total_point(self) -> int:
        calculated_point = self.point
        if (
            self.attendance_counter.training_day_attendance_cnt
            >= BONUS_ATTENDANCE_LIMIT
        ):
            calculated_point += BONUS_ATTENDANCE_POINT
        if self.attendance_counter.weekend_attendance_cnt >= BONUS_ATTENDANCE_LIMIT:
            calculated_point += BONUS_ATTENDANCE_POINT
        return calculated_point

    @property
    def grade(self) -> GradeEnum:
        return GradeEvaluator.evaluate(self.total_point)

    @property
    def is_removal_candidator(self) -> bool:
        return (
            GradeEvaluator.is_grade_removal_candidator(self.grade)
            and self.attendance_counter.is_removal_candidator_condition
        )
