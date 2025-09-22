class AttendanceCounter:
    def __init__(self):
        self.basic_attendance_cnt: int = 0
        self.training_day_attendance_cnt: int = 0
        self.weekend_attendance_cnt: int = 0

    @property
    def is_removal_candidator_condition(self) -> bool:
        return (
            self.training_day_attendance_cnt == 0 and self.weekend_attendance_cnt == 0
        )
