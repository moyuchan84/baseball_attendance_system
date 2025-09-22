playername_playerid_dict = {}
auto_generated_id_number = 0

# dat[사용자ID][요일]
playerid_weekday_cnt = [[0] * 100 for _ in range(100)]
player_points = [0] * 100
player_grade = [0] * 100
names = [""] * 100
training_day_attendance_cnt = [0] * 100
weekend_attendance_cnt = [0] * 100

# point variable
BASIC_ATTENDANCE_POINT = 1
TRAININING_ATTENDANCE_POINT = 3
WEEKEND_ATTENDANCE_POINT = 2
BONUS_ATTENDANCE_POINT = 10
BONUS_ATTENDANCE_LIMIT = 10

# grade variable
GRADE_ZONE = {"GOLD": 50, "SILVER": 30, "NORMAL": 0}

# specialday
TRAINING_DAYS = ["wednesday"]
WEEKEND_DAYS = ["saturday", "sunday"]

# file path
FILE_PATH = "attendance_weekday_500.txt"

# weekday
WEEKDAYS_DICT_INDEX = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}


def get_total_player_range():
    return range(1, auto_generated_id_number + 1)


def get_playerid(player_name):
    global auto_generated_id_number

    if player_name not in playername_playerid_dict:
        auto_generated_id_number += 1
        playername_playerid_dict[player_name] = auto_generated_id_number
        names[auto_generated_id_number] = player_name

    playerid = playername_playerid_dict[player_name]
    return playerid


def calculate_attendance_point(player_name, weekday):
    playerid = get_playerid(player_name)

    add_point = 0
    weekday_index = WEEKDAYS_DICT_INDEX.get(weekday, -1)

    if weekday in TRAINING_DAYS:
        add_point += TRAININING_ATTENDANCE_POINT
        training_day_attendance_cnt[playerid] += 1
    elif weekday in WEEKEND_DAYS:
        add_point += WEEKEND_ATTENDANCE_POINT
        weekend_attendance_cnt[playerid] += 1
    else:
        add_point += BASIC_ATTENDANCE_POINT
    playerid_weekday_cnt[playerid][weekday_index] += 1
    player_points[playerid] += add_point


def read_attendance_data_file():
    lines = []
    with open(FILE_PATH, encoding="utf-8") as f:
        for _ in range(500):
            line = f.readline()
            if not line:
                break
            parts = line.strip().split()
            lines.append(parts)
    return lines


def calculate_players_attendance_point(lines):
    for line in lines:
        if len(line) == 2:
            playername, weekday = line
            calculate_attendance_point(playername, weekday)


def calculate_players_bonus_point():
    for i in get_total_player_range():
        if training_day_attendance_cnt[i] >= BONUS_ATTENDANCE_LIMIT:
            player_points[i] += BONUS_ATTENDANCE_POINT
        if weekend_attendance_cnt[i] >= BONUS_ATTENDANCE_LIMIT:
            player_points[i] += BONUS_ATTENDANCE_POINT


def print_removed_player_list():
    print("\nRemoved player")
    print("==============")
    for i in get_total_player_range():
        if (
            player_grade[i] not in ("GOLD", "SILVER")
            and training_day_attendance_cnt[i] == 0
            and weekend_attendance_cnt[i] == 0
        ):
            print(names[i])


def print_player_point_grade():
    for i in get_total_player_range():
        print(
            f"NAME : {names[i]}, POINT : {player_points[i]}, GRADE : {player_grade[i]}",
        )


def judge_players_grade():
    for i in get_total_player_range():
        for grade_name, score_limit in sorted(
            GRADE_ZONE.items(), key=lambda x: x[1], reverse=True
        ):
            if player_points[i] >= score_limit:
                player_grade[i] = grade_name
                break


def run_attendance_system():
    try:
        lines = read_attendance_data_file()
        calculate_players_attendance_point(lines)
        calculate_players_bonus_point()
        judge_players_grade()
        print_player_point_grade()
        print_removed_player_list()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    run_attendance_system()
