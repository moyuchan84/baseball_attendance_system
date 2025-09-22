import tempfile
import os
from mission2.baseball_file_reader import BaseballFileReader


def test_read_lines():
    # Arrange
    test_content = "Alice monday\nBob tuesday\n"
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as tmp:
        tmp.write(test_content)
        tmp_path = tmp.name

    # Act
    result = BaseballFileReader.read_lines(tmp_path)

    # Assert
    assert result == [["Alice", "monday"], ["Bob", "tuesday"]]
