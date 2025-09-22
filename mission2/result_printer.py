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
