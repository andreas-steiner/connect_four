# Design

Um dieses Projekt umzusetzen haben wir uns, als Ziel gesetzt eine UI auch zu machen,
wir sind auf pygame gestoßen und haben sehr schnell gesehen das diese Library genau
das macht, was wir wollen. Bevor wir aber unsere Ideen mit pygame realisieren können,
mussten wir zuerst die Logik und die Spielabläufe schreiben 
bzw. uns überlegen wie wir das machen.

Wir haben als Erstes eine abstrakte Klasse Board erstellt und definiert was wir
brauchen damit ein Spiel funktionieren kann und wir haben 
folgendes als wichtig empfunden: <br>
* Es muss ein Spielbrett erstellen
* Steine sollen platziert werden
* Wir müssen überprüfen, ob die Steine richtig gesetzt wurden also richtige Reihe und Spalte
* Es müssen Gewinnbedingungen vorhanden sein
* es sollen unterschiedliche Farben verwendet werden für Spieler 1 und 2

Um diese Punkte zu verwirklichen, haben wir einfach begonnen 
und die Funktion make_board() erstellt diese generiert ein Array das nur aus Nullen 
besteht mit den Abmessungen von 7 Spalten und 6 Reihen. Das ist der Grundstein
für fast alle folgenden Methoden. <br>
Als Nächstes wollen wir einen Stein setzten, dazu haben wir place_stone() erstellt.
Diese Methode braucht das erstellte Board sowie die Koordinaten des Steines und einen Stein.
Als Koordinaten haben wir die Reihen und Spalten verwendet 
und der Einfachheit halber ist Stein nur ein Integer. <br>
Im nächsten Schritt wollten wir prüfen, ob der Stein richtig gesetzt wurde
dafür haben wir zwei Methoden loc_valid und next_row und beide diese Methoden sind
essenziell damit unser Spiel funktioniert loc_valid gibt mir ein Bool zurück und
next_row die Reihe, in welcher der Stein platziert wird. <br>
Es sollte natürlich auch einen Sieger geben dafür haben wir win_con() erstellt
und das wird jedes Mal ausgeführt, nachdem ein Stein gesetzt wurde und überprüft, 
ob es zu einem Sieg führt. Wir haben schnell gemerkt das es nicht immer einen Sieger
gibt deswegen wurde später die Funktion draw() erstellt. Ähnlich wie win_con() prüft 
draw() nach jeden Zug, ob es zu einem Unentschieden gekommen ist. <br>
Die Farben zu definieren war der einfachste Schritt wir haben gesehen pygame hätte gerne 
Tuples für diese das heißt diese haben wir definiert und geben wir als Tupel weiter.
Nun zu Dingen, die wir damals noch nicht geplant hatten, wir haben auch eine Funktion print_board()
erstellt fürs Debuggen und um zu verstehen, wo meine Steine landen. <br>
Sowie die Funktionen um das Spielbrett zu rendern und das Spiel zu starten.
Diese haben uns großes Kopf zerbrechen bereitet aber nicht wegen der 
Komplexität der Funktionen an sich, sondern weil pygame unseren Splashtext
nicht mehr anzeigen wollte, nachdem wir es so gemacht haben das ein Spielfenster erst 
geöffnet wird, sobald bestimmt wurde, ob es ein Mehrspieler oder Einzelspieler Spiel ist.
Wir haben uns für das kleinere Übel entschieden und die Texte bei Siegen und 
Unentschieden werden nun korrekt angezeigt, jedoch wird nun das Fenster geöffnet und die 
Abfrage gleichzeitig gemacht.
