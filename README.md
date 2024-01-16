# **Zadanie**
Aplikacja do raportowania absencji pracowników.
Napisać aplikację przyjmującą na wejściu plik CSV (comma-separated values), wczytującą dane pracowników i ich absencji **w konkretnym (__jednym__) roku**, a następnie generującą raport do nowego pliku CSV.
 

# **Wejście**

Przykładowe pliki CSV załączone z treścią zadania. Reprezentują okresy nieobecności pracowników z zakładzie pracy w danym roku. Poszczególne kolumny pliku .csv oznaczają kolejno:
 
- imię - string
- nazwisko - string
- pesel (unikalny identyfikator pracownika) - string, 11 cyfr
- data urodzenia - format: dd.mm.rrrr
- płeć – jeden znak, M - mężczyzna, K – kobieta 
- początek absencji, data od, format: dd.mm.rrrr
- koniec absencji, data do, format: dd.mm.rrrr
 
np.
Jan;Kowalski;71092958614;29.09.1971;M;3.02.2023;15.02.2023 
 

# **Wyjście**

W pliku wyjściowym z raportem należy podać łączną liczbę dni wynagrodzenia chorobowego i zasiłku chorobowego dla każdego z pracowników w wybranym przez użytkownika okresie.
Format danych w pliku:
Imie; Nazwisko; PESEL; Data urodzenia; Plec; Wiek; Liczba dni absencji; Liczba dni wynagrodzenia chorobowego; Liczba dni zasilku chorobowego


# **Algorytm wyliczania przysługujących dni wynagrodzenia chorobowego i zasiłku**

Za czas niezdolności do pracy, który trwa łącznie do 33 dni w ciągu roku kalendarzowego (a jeżeli ukończyłeś 50 rok życia – łącznie do 14 dni) wypłacane jest wynagrodzenie chorobowe. 
Zasiłek chorobowy przysługuje Ci od 34. lub odpowiednio od 15. dnia niezdolności do pracy w roku kalendarzowym.  
Jeśli ukończyłeś 50 rok życia, czternastodniowy okres wypłaty wynagrodzenia chorobowego przysługuje Ci począwszy od następnego roku kalendarzowego po roku, w którym ukończyłeś ten wiek. 
Okres 33 lub odpowiednio 14 dni niezdolności do pracy, za który zachowujesz prawo do wynagrodzenia chorobowego, ustala się sumując poszczególne okresy niezdolności do pracy w roku kalendarzowym, nawet jeżeli wystąpiły między nimi przerwy. 
Np.
Janusz ma 51 lat. Chorował w okresach: 01.01.2022 - 05.01.2022 oraz 10.02.2022 - 25.02.2022. Otrzymuje 14 dni wynagrodzenia chorobowego i 7 dni zasiłku chorobowego.
Grażynka ma 27 lat. Chorowała w okresach: 01.01.2022 - 05.01.2022 oraz 10.02.2022 - 25.02.2022. Otrzymuje 21 dni wynagrodzenia chorobowego i 0 dni zasiłku chorobowego.

