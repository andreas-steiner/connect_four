# Design

Eines unserer Ziele für dieses Projekt, war eine UI zu schaffen. Wir sind auf pygame 
gestoßen. Diese Library erfüllt genau diesen Zweck. Bevor wir aber unsere Ideen mit pygame 
realisieren konnten, mussten wir zuerst die Logik und die Spielabläufe schreiben 
bzw. uns überlegen wie wir das machen.

Zuerst haben wir eine abstrakte Klasse Board erstellt und definiert was wir
brauchen, damit ein Spiel funktionieren kann. Wir haben 
folgende Punkte als wichtig empfunden: <br>
* Es muss ein Spielbrett erstellen
* Steine sollen platziert werden
* Wir müssen überprüfen, ob die Steine richtig gesetzt wurden also richtige Reihe und Spalte
* Es müssen Gewinnbedingungen vorhanden sein
* es sollen unterschiedliche Farben verwendet werden für Spieler 1 und 2

Um diese Punkte zu verwirklichen, haben wir die Funktion make_board() erstellt. Diese generiert ein 
Array, welches nur aus Nullen besteht und eine Abmessung von 7 Spalten und 6 Reihen. 
Das ist der Grundstein für fast alle der folgenden Methoden. <br>
Als Nächstes wollen wir einen Stein setzten, dazu haben wir die Methode place_stone() erstellt.
Diese braucht das erstellte Board, die Koordinaten des Steines und einen Stein.
Die Koordinaten ergeben sich durch die Reihen und Spalten und der Stein ist ein Integer. <br>
Im nächsten Schritt wollten wir prüfen, ob der Stein richtig gesetzt wurde.
Dafür haben wir zwei Methoden loc_valid() und next_row(). Beide Methoden sind
essenziell, damit unser Spiel funktioniert. loc_valid() liefert ein Bool und
next_row() die Reihe, in welcher der Stein platziert wird. <br>
Die Methode win_cond() überprüft nach jeden Zug, ob eine der definierten Win Conditions erfüllt wurde
und dadurch ein Sieger bestimmt werden kann. Eine ähnliche Funktionalität hat die Methode draw(), die
nach jedem Spielzug überprüft, ob es zu einem Unentschieden gekommen ist. <br>
Nun zu Dingen, die wir damals noch nicht geplant hatten, wir haben zum Debuggen und zum verstehen
wo die Spielsteine landen, eine Funktion print_board() erstellt. <br>
Sowie die Funktionen um das Spielbrett zu rendern und das Spiel zu starten.
Diese haben uns großes Kopf zerbrechen bereitet. Nicht wegen der 
Komplexität der Funktionen, sondern weil pygame unseren Splashtext
nicht mehr anzeigen wollte, nachdem wir bestimmt haben, dass ein Spielfenster erst 
geöffnet wird, sobald bestimmt wurde, ob es ein Mehrspieler oder Einzelspieler Spiel ist.
Wir haben uns für das kleinere Übel entschieden und die Texte bei Siegen und 
Unentschieden werden nun korrekt angezeigt, jedoch wird nun das Fenster geöffnet und die 
Abfrage gleichzeitig gemacht.
