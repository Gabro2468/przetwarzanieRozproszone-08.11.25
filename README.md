# przetwarzanieRozproszone-08.11.25
Projekt na laboratoriach z dnia 08.11.2025. Dwa serwery które komunikują się ze sobą za pomocą Rest API i zwracają pełny opis produktu.

Włączamy dwa serwery - python serwerMagazyn.py, python serwerProdukt.py
Po czym z konsoli robimy - curl 127.0.0.1:8002/stock/{idProduktu}
Dostajemy odpowiedź albo 200 jeśli produkt jest w bazie, albo 404 jeśli go nie ma
