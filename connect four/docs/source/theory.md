# Theorie

#### Frage Eins
Sie beginnen als EntwicklerIn in einem neuen Unternehmen und bekommen die
Verantwortung für ein Modul. Das Modul ist über eine lange Zeit hinweg gewachsen und
besteht nur aus sehr wenigen Klassen. Die Methoden dieser Klassen sind meist sehr lange,
oftmals einige hundert Zeilen oder länger, und sie sind auch eher spärlich dokumentiert. <br>
Was für Nachteile ergeben sich für Sie durch diesen Code? <br>
Welche grundlegenden Software
Design Prinzipien werden evtl. nicht eingehalten? <br><br>

#### Antwort:   
Nun bei diesem Beispiel wurden einige grundlegende Dinge missachtet.
Als Erstes werden kaum Klassen verwendet und ich nehme auch kaum oder gar keine Abstrakten Klassen,
es wurden auch die 5 SOLID-Prinzipien nicht eingehalten. All das führt dazu, das der Code sehr schwer
wartbar ist, die fehlende Dokumentation macht es zusätzlich noch schwerer herauszufinden was der Code genau
macht. KISS wäre schön, wenn es hier praktiziert werden würde, jedoch wurde das auch missachtet den der Code ist
weder simple noch small (KISS – Keep it simple and stupid/small). <br>
Das alles macht es nur sehr schwierig den Code zu verändern, erweitern und zu warten.
<br><br>


#### Frage Zwei
Für die vollständige Überarbeitung/Neuschreiben bleibt Ihnen keine Zeit, da sie ihr/e
Vorgesetze/r schon mit der Umsetzung des nächsten Features beauftragt hat. <br>
Wie würden Sie bei der Umsetzung vorgehen?

Antwort