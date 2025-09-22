class BaseballFileReader:
    @staticmethod
    def read_lines(file_path):
        with open(file_path, encoding="utf-8") as f:
            return [line.strip().split() for line in f.readlines()]
