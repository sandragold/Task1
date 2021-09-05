"""
Moduł testujący funkcjonalność zapisu pliku tekstowego.
"""

import os
from data_ops.io_ops.file_writer import FileWriter


def test_create_file(tmp_path):
    # Zawartość tmp_path.py
    output_content = [1, 11, 0, 12]
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    FileWriter.writer(output_content, p)

    assert os.path.isfile(p)
    assert len(list(tmp_path.iterdir())) == 1
