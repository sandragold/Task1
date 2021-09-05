"""
Główny moduł zawierający logikę aplikacji.
"""

import os

from data_ops.io_ops.file_reader import FileReader
from data_ops.algorithms.basic import PairAnalyzer
from data_ops.io_ops.file_writer import FileWriter


def main():
    # Wczytaj dane ze ścieżki
    filepath = "/app/input_path.txt"
    file_reader = FileReader(path=filepath)
    data = file_reader.reader()
    # Zainicjalizuj klase oairreade danymi z data
    pair_analyzer = PairAnalyzer(data)
    # Oblicz opary
    output = pair_analyzer.find_pairs(12)
    # Zapisz output
    path_out = os.environ["PATHOUT"]
    FileWriter.writer(output, path_out)


if __name__ == "__main__":
    main()
