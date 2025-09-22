import sys
from io import StringIO
from mission1.attendance import run_attendance_system


def test_run_attendance_system_stdout():
    expected = (
        "NAME : Umar, POINT : 48, GRADE : SILVER\n"
        "NAME : Daisy, POINT : 45, GRADE : SILVER\n"
        "NAME : Alice, POINT : 61, GRADE : GOLD\n"
        "NAME : Xena, POINT : 91, GRADE : GOLD\n"
        "NAME : Ian, POINT : 23, GRADE : NORMAL\n"
        "NAME : Hannah, POINT : 127, GRADE : GOLD\n"
        "NAME : Ethan, POINT : 44, GRADE : SILVER\n"
        "NAME : Vera, POINT : 22, GRADE : NORMAL\n"
        "NAME : Rachel, POINT : 54, GRADE : GOLD\n"
        "NAME : Charlie, POINT : 58, GRADE : GOLD\n"
        "NAME : Steve, POINT : 38, GRADE : SILVER\n"
        "NAME : Nina, POINT : 79, GRADE : GOLD\n"
        "NAME : Bob, POINT : 8, GRADE : NORMAL\n"
        "NAME : George, POINT : 42, GRADE : SILVER\n"
        "NAME : Quinn, POINT : 6, GRADE : NORMAL\n"
        "NAME : Tina, POINT : 24, GRADE : NORMAL\n"
        "NAME : Will, POINT : 36, GRADE : SILVER\n"
        "NAME : Oscar, POINT : 13, GRADE : NORMAL\n"
        "NAME : Zane, POINT : 1, GRADE : NORMAL\n"
        "\nRemoved player\n==============\nBob\nZane\n"
    )
    captured = StringIO()
    sys.stdout = captured
    run_attendance_system()
    sys.stdout = sys.__stdout__
    assert captured.getvalue() == expected
