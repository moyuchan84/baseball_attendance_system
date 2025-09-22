from abc import ABC, abstractmethod

from mission2.player import Player


# point variable
BASIC_ATTENDANCE_POINT = 1
TRAININING_ATTENDANCE_POINT = 3
WEEKEND_ATTENDANCE_POINT = 2

# specialday
TRAINING_DAYS = ["wednesday"]
WEEKEND_DAYS = ["saturday", "sunday"]


class IPlayerPointCalculator(ABC):
    @abstractmethod
    def apply_calculated_points(self, player: Player):
        pass


class BasicPlayerPointCalculator(IPlayerPointCalculator):
    def apply_calculated_points(self, player: Player):
        player.point += BASIC_ATTENDANCE_POINT
        player.attendance_counter.basic_attendance_cnt += 1


class TrainingDayPlayerPointCalculator(IPlayerPointCalculator):
    def apply_calculated_points(self, player: Player):
        player.point += TRAININING_ATTENDANCE_POINT
        player.attendance_counter.training_day_attendance_cnt += 1


class WeekendPlayerPointCalculator(IPlayerPointCalculator):
    def apply_calculated_points(self, player: Player):
        player.point += WEEKEND_ATTENDANCE_POINT
        player.attendance_counter.weekend_attendance_cnt += 1


class PlayerPointCalculatorFactory:
    @staticmethod
    def create(weekday: str):
        if weekday in TRAINING_DAYS:
            return TrainingDayPlayerPointCalculator()
        elif weekday in WEEKEND_DAYS:
            return WeekendPlayerPointCalculator()
        else:
            return BasicPlayerPointCalculator()
