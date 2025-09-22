### 요구사항 체크리스트

| 요구사항 | 확인 |
| :--- | :---: |
| D1 | O |
| D2 | O |
| D3 | O |
| D4 | O |
| D5 | O |

# 1. 함수 레벨리팩토링
### D1 - 가독성있는 코드로메서드추상화, 가독성좋은네이밍사용
>> mission1 - attendance.py 파일 작성


# 2. 클래스 레벨리팩토링
### D2 - Regression Test를 위한 Unit Test 개발
>> tests 폴더에 unit-test 는 별도로 분리 개발 (mission2_module명.py)로 개발
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

