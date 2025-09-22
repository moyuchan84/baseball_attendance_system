<img width="1459" height="807" alt="image" src="https://github.com/user-attachments/assets/620a589f-57b7-4a3d-be32-4cd78666422e" />### 요구사항 체크리스트

| 요구사항 | 확인 |
| :--- | :---: |
| D1 | O |
| D2 | O |
| D3 | O |
| D4 | O |
| D5 | O |

# 1. 함수 레벨리팩토링
### D1 - 가독성있는 코드로메서드추상화, 가독성좋은네이밍사용
>> mission1 - attendance.py 파일 작성 (https://github.com/moyuchan84/baseball_attendance_system/blob/main/mission1/attendance.py)


# 2. 클래스 레벨리팩토링
### D2 - Regression Test를 위한 Unit Test 개발
>> tests 폴더에 unit-test 는 별도로 분리 개발 (mission2_module명.py)로 개발 (https://github.com/moyuchan84/baseball_attendance_system/tree/main/tests)
<img width="368" height="608" alt="image" src="https://github.com/user-attachments/assets/1627c8ad-b24b-4f52-b990-c6176a0a14f9" />

### D3 – 확장성을 고려한설계, 정책과 등급이추가되더라도Client Code에 변경이 없도록 한다. 
>> mission2.grade_enum.py 내 grade - cutline 선언 (cf - 음수가 들어올 일은 없으나, 예외 case 위한 NONE 추가 선언)
```
from enum import Enum


class GradeEnum(Enum):
    GOLD = 50
    SILVER = 30
    NORMAL = 0
    NONE = -1

```
>> mission2.grade_evaluator.py 내 grade 확장성 고려한 logic 개선(높은 점수 부터 체크)
```
from mission2.grade_enum import GradeEnum

class GradeEvaluator:
    @staticmethod
    def evaluate(player_total_point: int) -> GradeEnum:
        if player_total_point < 0:
            return GradeEnum.NONE
        for grade in sorted(GradeEnum, key=lambda g: g.value, reverse=True):
            if player_total_point >= grade.value:
                return grade
```

>> 클라이언트 코드에서 등급 추가되더라도, 변경 없음(mission2 - result_printer.py)
```
from mission2.player import Player


class ResultPrinter:
    @staticmethod
    def print_player_status(players: list[Player]):
        for player in players:
            print(
                f"NAME : {player.name}, POINT : {player.total_point}, GRADE : {player.grade.name}",
            )

    @staticmethod
    def print_removed_player_list(removed_players: list[Player]):
        print("\nRemoved player")
        print("==============")
        for player in removed_players:
            print(player.name)

```


# 3. 디자인 패턴사용하기
### D4 - 리팩토링에 디자인패턴을적용한다.
>> Factory Method / Strategy pattern 적용
>> 선수의 점수 계산에 대한 로직 변경가능성(확장성 고려)하여 해당 로직 strategy/ factory pattern 적용
```
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
```
>> mission2.baseball_attendance_system.py 내 parse data 에서 Factory method 호출, 
```

    def parse_data(self):
        lines = BaseballFileReader.read_lines(self.file_path)
        for line in lines:
            if len(line) != 2:
                continue
            name, weekday = line
            player = self.baseball_team.get_player(name)
            point_calculator = PlayerPointCalculatorFactory.create(weekday)
            point_calculator.apply_calculated_points(player)
```

# 4. 코드 커버리지100%
### D5 - 리팩토링이 끝난코드에, 코드 커버리지가100% 되어야한다
 >> vscode 내 pytest 로 실행
<img width="380" height="392" alt="image" src="https://github.com/user-attachments/assets/400bba34-486a-44fd-8360-fcea29defc97" />
<img width="838" height="632" alt="image" src="https://github.com/user-attachments/assets/1c1cfb53-baa9-4328-9254-23c1b24ef0d3" />

>> code coverage 100% 미만 코드 관련 내용
>> 1. mission2-main.py (run_baseball_system()) 
<img width="1410" height="465" alt="image" src="https://github.com/user-attachments/assets/5e44fbe1-734e-43be-a397-02f09a53da65" />

>> 2. mission2-grade_evaluator.py : 코드상 모든 분기분 커버하는 테스트코드 작성하였으나, 만족 안함으로 나옴(모든 케이스 커버하는 테스트코드 작성완료 - tests - mission2_grade_evaluator.py)
<img width="891" height="433" alt="image" src="https://github.com/user-attachments/assets/b8ff48cc-6c72-414f-8986-d5e153aee06c" />

>> 3. mission1-attendance.py : 테스트코드 미대상 코드로, 함수레벨 리팩터링 관련하여 test code 작성, open line 과 file 없음 관련 exception 행에 대해서 로직과 상관없음
<img width="2039" height="748" alt="image" src="https://github.com/user-attachments/assets/716d66b9-abb2-46c5-b755-2037b813704e" />

>> 4. mission1- point_calculator.py : 행중에서 abstact method 내 pass 행 테스트 미실시(로직과 상관없음)
<img width="1459" height="807" alt="image" src="https://github.com/user-attachments/assets/9cab5684-d018-4d5c-9347-e4b48aad71ce" />


