Autor: SANDRA BINIAS

# zadanie
Znajdź pary liczb naturalnych, których suma to 12. Raz użyta liczba nie może być wykorzystana ponownie.
Wynik posortowany (pierwsza liczba mniejsza od drugiej).

1. Aby uruchomić testy jednostkowe należy w głównym katalogu projektu wywołać komendę:

`pytest tests`

2. Aby zbudować obraz Dockera aplikacji należy w głównym katalogu projektu wywołać komendę:
`docker build -t <TWOJA_NAZWA_KONTENERA> .`

Przykład:
`docker build -t datumo .`

3. Aby uruchomić aplikację w kontenerze należy wywołać komendę:
`docker run -e PATHOUT="<NAZWA_PLIKU_WYJSCIOWEGO>" -v <ŚCIEŻKA_DO_PLIKU_WEJSCIOWEGO>:/app/input_path.txt -v <ŚCIEŻKA_DO_REPOYTORIUM>:/app <NAZWA_DOKERA>`

Przykład:
`docker run -e PATHOUT="wynik.txt" -v /Users/sandra.binias/liczby_in.txt:/app/input_path.txt -v /Users/sandra.binias/python_projects/zadanie_datumo:/app datumo`

WAŻNE:
ścieżka wolumenu `/app/input_path.txt` nie może ulec zmianie, gdyż jest zmienną operacyjną aplikacji.
