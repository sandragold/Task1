"""
Moduł z funkcjonalnością wczytywania pliku i wstępnej selekcji danych.
"""


class FileReader:
    """
    Klasa umożliwiająca operacje na pliku wejściowym dla alrgorytmu.

    Attributes:
        path (string): ścieżka do pliku wejściowego zawierającego liczby
    """

    def __init__(self, path):
        self.path = path

    def reader(self):
        input_content = []
        with open(self.path) as f:
            input_content_raw = f.read().splitlines()
            # Sprawdź czy wartości są string i cyfry skonwertuj na int (wymóg: naturalne)
            for element in input_content_raw:
                if element.isdigit():
                    input_content.append(int(element))
        return input_content
