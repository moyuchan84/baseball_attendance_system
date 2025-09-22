from mission2.grade_enum import GradeEnum


class GradeEvaluator:
    @staticmethod
    def evaluate(player_total_point: int) -> GradeEnum:
        if player_total_point < 0:
            return GradeEnum.NONE
        for grade in sorted(GradeEnum, key=lambda g: g.value, reverse=True):
            if player_total_point >= grade.value:
                return grade

    @staticmethod
    def is_grade_removal_candidator(grade: GradeEnum) -> bool:
        return grade not in (GradeEnum.GOLD, GradeEnum.SILVER)
