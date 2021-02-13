# Tests

Getestet wurde die Klasse PlayBoard und deren Funktionen. Hierfür wurden Variablen und eine Reihe von 
"Board States" als numpy array angelegt um den Code auf verschiedene Situationen zu testen.

#### test_draw():
Testet, ob die Funktion, die dafür Zuständig ist zu überprüfen, ob das derzeitige Spiel unentschieden 
ist, funktioniert.

#### test_win_cond():
Überprüft verschiedene Board States auf unterschiedliche win conditions, die nur eintreten können,
wenn 4 Steine eines Spielers entweder horizontal, diagonal oder vertikal nebeneinander liegen.

#### test_next_row(): und test_loc_val():
Überprüft, ob das Programm in der Lage ist zu bestimmen, ob ein Spielstein in ein bestimmtes Feld
gelegt werden kann.

#### test_place_stone():
Testet, ob die Funktion, die dafür zuständig ist den Stein eines Spielers zu platzieren funktioniert.