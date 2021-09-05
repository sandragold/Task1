"""
Moduł z funkcjonalnością zapisywania pliku.
"""


class FileWriter:
    """
    Klasa zawierająca metody do zapisu wyniku do pliku tekstowego.

    """

    @staticmethod
    def writer(output_content, file_name="pary_out.txt"):
        file_out = open(file_name, "w")
        file_out.write(str(output_content) + "\n")
