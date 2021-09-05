"""
Moduł testujący funkcjonalność odczytu wejściowego pliku testowego.
"""

import pytest
import os

from data_ops.io_ops.file_reader import FileReader

test_data = [
    (
        os.path.abspath("tests/fixtures/liczby_in.txt"),
        [1, 5, 3, 7, 9, 10, 2, 0, 4, 8, 0, 15, 4, 12],
    ),
    (
        os.path.abspath("tests/fixtures/liczby_in2.txt"),
        [1, 5, 3, 7, 9, 6, 10, 2, 12, 0, 4, 8, 0, 4, 12],
    ),
    (os.path.abspath("tests/fixtures/liczby_in3.txt"), [1, 11, 11]),
]

test_data2 = [
    ("/users/test\\fikst\\liczby_in.txt"),
    ("23423545353"),
    ("febsofeisioejfioej"),
]


@pytest.mark.parametrize("path,input_content", test_data)
def test_file_reader(path, input_content):
    filereader = FileReader(path=path)
    result = filereader.reader()
    assert result == input_content


@pytest.mark.parametrize("path", test_data2)
def test_missingfile(path):
    with pytest.raises(FileNotFoundError):
        filereader = FileReader(path=path)
        filereader.reader()
