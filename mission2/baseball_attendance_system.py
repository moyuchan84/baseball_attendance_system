from mission2.baseball_team import BaseballTeam
from mission2.point_calculator import PlayerPointCalculatorFactory
from mission2.baseball_file_reader import BaseballFileReader
from mission2.result_printer import ResultPrinter


FILE_PATH = "attendance_weekday_500.txt"


class BaseballAttendanceSystem:
    def __init__(self, file_path: str = FILE_PATH):
        self.file_path = file_path
        self.baseball_team = BaseballTeam()

    def run(self):
        self.parse_data()
        self.print_baseball_team_status()

    def parse_data(self):
        lines = BaseballFileReader.read_lines(self.file_path)
        for line in lines:
            if len(line) != 2:
                continue
            name, weekday = line
            player = self.baseball_team.get_player(name)
            point_calculator = PlayerPointCalculatorFactory.create(weekday)
            point_calculator.apply_calculated_points(player)

    def print_baseball_team_status(self):
        ResultPrinter.print_player_status(self.baseball_team.player_list)
        ResultPrinter.print_removed_player_list(self.baseball_team.removed_player)
