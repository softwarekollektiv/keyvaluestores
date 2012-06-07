% Key-Value-Stores
% Philipp Borgers \ Felix H...

# Abstract

# Key-Value-Stores



# Tokyo Cabinet

Tokyo Cabinet ist ein dateibasierter Key-Value Store.
Der C-Code steht unter einer LGPL-Lizenz und wird von FAL Labs verwaltet. Für
Toyko Cabinet stehen in den verschiedensten Programmiersprachen Treiber bereit.
Python, java, nodejs und ruby sind nur einige Beispiele. Inzwischen
wurde Tokyo Cabinet von seinem Nachfolger Kyoto Cabinet abgelöst,
behält jedoch immer noch seine Bedeutung bei durch seine Bekanntheit
unter vielen Entwicklern.

Tokyo Cabinet ist eine Bibliothek, die sich auf Prozessebene einbinden
lässt. Datenbanken werden in Dateien angelegt und verwaltet. Es stehen
insgesamt vier Varianten zur Verfügung um Datenbank anzulegen, die sich durch
die Art der Indizierung der Daten unterscheiden. Im Folgenden werden wir auf
die vier Datenbanktypen eingehen: B+Tree, hash, fixed-length, tables. Der
Vollständigkeit wegen sei noch erwähnt, dass es ebenfalls möglich ist
in-memory Datenbanken anzulegen.
Alle Datenbanktypen teilen sich ein gemeinsames
Interface, dass die Funktionen eines Key-Value-Stores abbildet:

* PUT
* GET
* DELETE
* KEYS

Die *KEYS* Operation erlaubt es dem Entwickler über alle Schlüssel des
Key-Value-Stores zu iterieren.

Alle Operationen von Tokyo-Cabinet sind thread safe. Das heißt, dass entweder
auf record oder Dateiebene Locks verwendet werden um den Zugriff auf die
Datenbank zu regeln. Darüber hinaus wird ACID für die Operationen
garantiert. Es gibt jedoch keine Transaktionen, die mehrere Operationen
zusammenfassen. Es wird ein Write-Ahead-Log verwendet um im Fall eines Absturz
das System wieder in einen gültigen Zustand zurückzuführen.

## Hash Datenbanken (TCHDB)

Im Fall der Hash Datenbank wird eine Hash-Funktion verwendet um auf die Daten
zuzugreifen. Die Zugriffszeit ist somit nur von der Zeit abhängig, die
die Hash-Funktion braucht um aus einem Schlüssel eine Position in der
Datenbank zu berechnen. Dies gilt für die drei Operation: put, get, delete.
Die Schlüssel mit denen die Datenbank arbeiten soll. müssen eindeutig sein.
Wird ein Schlüssel mehrfach verwendet, werden die Daten an der entsprechenden
Stelle überschrieben und somit verhindert, dass die Datenbank im ungünstigen
Fall zu einer Liste entartet. Die *KEYS*-Operation liefert die Keys der in
ungeordneter Reihenfolge zurück.

Um die Zugriffszeit zu minimieren werden Teile der Hash-Datenbank in
den Hauptspeicher gemapt (memory-mapping). Außerdem ist es möglich
Kompressionsalgorithmen zu verwenden, die die Daten für den User transparent
komprimieren. Zur Verfügung stehen z.B. deflate oder gzip.

Sollten trotz eindeutigen Keys durch die Hash-Funktion Kollisionen
erzeugt werden, kann Tokyo-Cabinet diese Kollision intern erkennen und
behandeln. Die kollidierenden Key-Value Paare werden in einem Binary Search
Tree verwaltet.

## B+Tree Datenbanken (TCBDB)

In B+Tree Datenbanken werden die Daten durch einen B+Tree indiziert und
somit in eine totale Ordnung gebracht. Die Pages des B+Trees werden
zusätzlich in einer
doppelt-verketteten List verwaltet. Die Verkettung der Pages erlaubt es
effizient den n-ten Nachbarn eines Knotens im B+Tree zu finden ohne den Baum
traversieren zu müssen. Im Falle der B+Tree Datenbanken ist es möglich einen
Key mehr als einmal zu verwenden, da die Ordnug im B+Tree auch für gleiche
Einträge definiert ist. Durch den B+Tree ist es möglich Range-Queries auf den
Keys auszuführen. Darüber hinaus ist es möglich Präfix-Anfragen zu stellen, die
Bedingungen an den Präfix der Keys stellen.

Die Pages des B+Trees werden in einem LRU-Cache
zwischengespeichert um den Zugriff auf häufig genutzte Pages zu beschleunigen.

## Fixed-length Datenbanken (TCFDB)

Fixed-length Datenbanken speichern einen Datensatz mit vordefinierter
Länge. Das heißt, dass die Records der Datenbank ebenfalls eine vordefinierte
Größe haben. Die Datensätze werden wie in einem Array durch einen Index
adressiert. Daraus ergibt sich, dass die Schlüssel der Fixed-length
Datenbank aus natürlichen Zahlen bestehen. Die Datenbank wird wie bei den
Hash Datenbanken in den Hauptspeicher gemapt um den Zugriff zu beschleunigen.

Die Fixed-length Datenbank hat die besten Eigenschaften in Bezug auf Speicher
und Zugriffszeit, birgt aber u.a. die Nachteil, dass sie nicht beliebig groß
werden kann und die Schlüssel in keiner Ordnung zueinander stehen.

## Table Datenbanken (TCTDB)

Die Table Datenbanken ermöglichen es Daten in Tabellen verwalten.
Jeder Datensatz in der Tabelle wird über einen Primary-Key indiziert. Ein
Datensatz (Row) in der Tabelle kann mehrere Spalten enthalten, die einen Namen
haben. Auf die Daten kann entweder über den Primary-Key zugegriffen
werden oder über die Spalten. Es ist möglich B+Tree Indizes über die Spalten
anzulegen um Anfragen, die sich auf Spalten beziehen zu beschleunigen.

# Voldemort

# Riak

Riak ist ein verteilter Key-Value-Store, der zur Zeit von *Bacho Technologies
Inc.* verwaltet und weiter entwickelt wird. Riak steht in zwei Varianten zur
Verfügung, einer Enterprise und einer Open-Source Version. Die Enterprise
Version unterstützt im Gegensatz zur Open-Source Version z.B. effiziente Replikation
über Rechenzentren hinweg. Für Entwickler stehen Treiber in verschieden
Sprachen zur Verfügung, z.B. Erlang, Java, Ruby, node.js.

Riak verteilt und repliziert Daten auf Basis von *Consistent Hashing* und
garantiert *Eventual Consistency*. Alle Knoten in einem Riak-Cluster sind
gleichwertig, d.h. jeder Knoten kann Anfragen eines Clients beantworten
bzw. an die zuständigen Knoten weiterleiten.

## Datenmodell

Riak verwaltet ausschließlich Key-Value Paare. Key-Value Paare werden in
sogenannten *Buckets* verwaltet. Replikationsfaktor, Write-Quorum etc.
lassen sich für einen Bucket konfigurieren. Es ist möglich sich alle Keys eines
Buckets zu erfragen. Jedem Key-Value-Paar sind außerdem Meta-Daten
zugeordnet, die u.a. die Vector Clock für ein Datum enthalten, aber auch
Informationen über den Content-Type oder ähnliches enthalten können. Riak
ermöglicht es mittels *Links* Beziehungen zwischen Key-Value Paaren zu
modellieren. Links können benannten werden und sind Foreign-Keys, also
Bucket-Key Tuple, die anderen Key-Value Paare referenzieren.

## 

# Scalaris

# Summary
