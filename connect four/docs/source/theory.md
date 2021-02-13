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

Bei diesem Beispiel wurden einige grundlegende Dinge missachtet.
Da keine kaum Klassen verwendet wurden, nehme ich an, dass die 5 SOLID-Prinzipen nicht eingehalten wurdne. 
Das führt dazu, das der Code sehr schwer wartbar ist. Die fehlende Dokumentation macht es zusätzlich noch 
schwerer herauszufinden was der Code genau macht. Es wäre gut gewesen, wenn Kiss praktiziert worden 
wäre, jedoch wurde auch das missachtet, denn der Code ist weder simple noch small 
(KISS – Keep it simple and stupid/small).
Das alles macht es nur sehr schwierig den Code zu verändern, erweitern und zu warten.

---

#### Frage Zwei

Für die vollständige Überarbeitung/Neuschreiben bleibt Ihnen keine Zeit, da sie ihr/e
Vorgesetze/r schon mit der Umsetzung des nächsten Features beauftragt hat. <br>
Wie würden Sie bei der Umsetzung vorgehen?<br>

#### Antwort

Da mir keine Zeit für eine vollständige Überarbeitung des Codes bleibt, sollten die 
anstehenden Features anhand der Software-Design-Prinzipien umgesetzt werden und 
der bereits bestehende Code nach und nach mithilfe von Refactoring. Wir wollen dadurch
die interne Struktur des Codes verbessern, ohne das externe Verhalten zu verändern.
