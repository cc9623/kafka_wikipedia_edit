# Data Engineering Internship Coding Challenge
#### Exxeta Berlin

In diesem Projekt möchten wir eine Kafka-Umgebung initialisieren.
Wir wurden mit Sample-Daten über Wikipedia-Edits ausgestattet und möchten nun folgende Komponenten programmieren:
### Im file producer.py:
Ein Producer, der die Beispieldaten einliest und in zufälligem Abstand zwischen
0-1 Sekunde auf ein oder mehrere Kafka Topics emittiert.

### Im file consumer.py:
Ein Kafka Consumer, der diese Daten vom Topic liest, die folgenden Aggregationen
vornimmt und die Ergebnisse abspeichert:
− Globale Anzahl Edits pro Minute
− Anzahl Edits der deutschen Wikipedia pro Minute

### Anmerkung:
Aus Zeit gründen verzichten wir (vorerst) auf das docker-compose.yml file


### Fragen beantworten:

Mögliche Datenbank zur Speicherung der Daten? (Vor-/ Nachteile)

-> TimescaleDB: 
+:SQL-Support, integrierte Zeitreihenfunktion, Skalierbarkeit  
-:höherer Ressourcenverbrauch als zB Cassandra

Welches Datenmodell wäre deiner Meinung nach sinnvoll zur Ablage der Events?

->Zeitreihenmodell. Jedes Event wäre ein Datensatz mit einem Zeitstempel, der die Zeit der Änderung angibt, und 
zusätzlichen Metadaten wie der ID des Edits und der Sprache. 
 
Welche Topics wären sinnvoll? Beschreibe Vor-/Nachteile deiner Topic Struktur in Hinblick
auf zum Beispiel Skalierbarkeit.

->Zwei Topics: einmal nur deutsch und einmal Rest. Diese Struktur passt zur Partitionierung der Daten. Allerdings wäre 
es sehr umständlich noch Mal eine andere Sprache zu extrahieren, weil man die Topic-Struktur neu überarbeiten müsste
.Ein Topic pro Sprache wäre auch sehr umständlich. Deswegen entscheiden wir uns für insgesamt nur einen Topic. Bzgl. der 
Skalierbarkeit ist folgendes zur Ressourceneffizienz zu sagen: einerseits werden alle Ressourcen für ein Topic benutzt, 
statt auf mehrere aufzuteilen, wobei es sein kann, dass manche Topics weniger genutzt werden könnten. Andererseits 
könnte der rasante Anstieg von einer Sprache auch zu langsamer Verarbeitung für alle Sprachen führen.
