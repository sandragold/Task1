"""
Moduł z bazowymi algorytmami obliczeniowymi.
"""


class PairAnalyzer:
    """
    Klasa przeszukująca zbiór liczb, których suma == `value_sum`

    Attributes:
        indata (list): lista przechowująca liczby naturalne (i 0).
    """

    def __init__(self, indata):
        self.indata = indata

    def find_pairs(self, value_sum):
        output_content = []
        inputfile2 = self.indata.copy()
        for i in self.indata:
            # Sprawdz czy element o indeksie "i" zawiera sie w drugiej liscie
            if i in inputfile2:
                # Jesli warunek spelniony to usun go z listy
                inputfile2.remove(i)
                # Definicja pary: suma i-tej liczby listy1 i x-tej liczby listy2 rowna jest zadanej sumie
                pary = [(i, x) for x in inputfile2 if i + x == value_sum]
                if len(pary):
                    # Dodaj wynik pary do listy i posortuj rosnąco
                    output_content.append(sorted(pary[0]))
                    # Usun wykorzystana liczbe z listy2
                    inputfile2.remove(pary[0][1])
        return output_content
