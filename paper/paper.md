% Key-Value-Stores
% Philipp Borgers \ Felix Höffken

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

Voldemort ist eine open-source Nachimplementierung von *Amazon Dynamo*, einem
verteilten Key-Value-Store, dessen Priorität eine geringe Latenzzeiz ist.
Entwickelt wird er von der *LinkedIn Corporation*. Der Code ist in Java
geschrieben und ist auf *github* einsehbar.
Für die Entwickler werden Treiber in Java, Ruby, PHP und C++ zur Verfügung
gestellt.

Voldemort nutzt *Consistent Hashing* zum verteilen und replizieren der Daten und
garantiert *Eventual Consistency*. Alle Knoten können Anfragen beantworten oder
- falls nötig - an andere Knoten weiterleiten

Voldemort bietet nur vier Operationen an, die mit den Daten interagieren können.

* PUT
* GET
* GET\_ALL
* DELETE

Hierbei bietet die *GET\_ALL* Operation die Möglichkeit mehrere Werte auf einmal auszulesen.

## Datenmodell

In einer Voldemort Datenbank können mehrere *Stores* existieren. In selbigen
werden Key-Value Paare gespeichert, wobei der Schlüssel eines solchen Paares in
dem Store eindeutig sein muss.
Wie die Daten gespeichert und übertragen werden kann in jedem Store eingestellt
werden. Von Haus aus wird das json-Format, die Java Serialisierung, Googles
Protobuff, das Avro Serialisierungssystem, das Speichern als String und als
Bytearray unterstützt.
Desweiteren existiert eine Schnittstelle, die jede/n Entwickler/in ermöglichen
soll eine eigene Serialisierungsmethode zu implementieren.

Es existieren mehrere Möglichkeiten die Daten zu persistieren. Standardmäßig
wird *BDB Java Edition* genutzt, allerdings ist auch eine *MySQL*-Datenbank ein
mögliches Backend. Eine weitere Möglichkeit ist, den Key-Value Store read-only
zu nutzen, was die Lesezugriffe beschleunigt. *LinkedIn* nutzt laut eigenen
Angaben fast ausschließlich diese Methode.
Hierzu muss die Datenbank per Hadoop generiert werden und kann ohne ausschlaten
des Systems übernommen werden.

## Eventual Consistency

Für jeden Store kann eingestellt werden, wie viele der Knoten, die Replikate
speichern, die neuen Daten erhalten haben müssen, bevor ein Schreibvorgang als
erfolgreich gilt.
Standardmäßig werden für Lese- und Schreibzugriffe eine Mindestquote von 50%
benötigt. So kann garantiert werden, dass das richtige Ergebnis gelesen wird.
*Eventual consistency* entsteht im Zusammenspiel mit *read-repair*. Hierbei
werden alle Knoten, die eine Antwort geben und noch veraltete Daten besitzen auf
den neusten Stand gebracht, bevor die Antwort an den Nutzer erfolgt. Ob ein Knoten eine veraltete Version besitzt wird mithilfe einer *Vector Clock* bestimmt.

Um die Konsistenz auch zu ermöglichen, falls ein Knoten offline ist, wird
*Hinted-Handoff* benutzt. Die Updates werden an einen Server geschickt, welcher
periodisch überprüft, ob der zuständige Knoten wieder erreichbar ist. Falls dies
zutrifft werden die Daten an den Server übertragen und auf den neusten Stand
gebracht.
Hierbei gibt es drei Möglichkeiten zu bestimmen, welcher Knoten hierfür genutzt
wird. Bei *Any-Handoff* wird zufällig irgendein erreichbarer Knoten genutzt. Bei
*Consistent-Handoff* wird -falls erreichbar- ein Server genutzt, der die
Replkate speichert. Bei *Proximity-Handoff* wird ein Knoten genutzt, der
geografisch nah am Offline-Knoten liegt. Diese Möglichkeit kann nur genutzt
werden, wenn den Knoten beim Start manuell ein Index zugeordnet wurde, der die geografische Lage beschreibt.



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

## Basis Operationen und Anfrage Sprache

Auch in Riak stehen die grundlegenden Operationen eines Key-Value-Stores
zur Verfügung mit zwei kleinen Unterschieden: Die *list buckets* Funktion
liefert alle Bucket-Namen im System zurück und die *list keys* Funktion
bezieht sich nur auf einen Bucket des Systems. Anfragen können entweder über
eine HTTP-Schnittstelle oder über ein Binärprotokoll auf Basis von Googles
Protobuffern gestellt werden.

Darüber hinaus bietet Riak die Möglichkeit komplexere Anfragen zu stellen, die
sich auf Buckets bzw. den gesamten Datensatz des Clusters beziehen. Die
einfachste Art der Anfrage ist eine Map/Reduce-Anfrage über alle Objekte des
Clusters bzw. eines Buckets. Map/Reduce-Anfragen können in Erlang oder
Javascrpt geschrieben werden. Bezieht sich die Anfrage nur auf die
Primary-Keys der Key-Value-Paare nutzt man die sogenannten Key-Filter. Die
Key-Filter können auf die Indizes der Storage-Engines zurückgreifen
und so die Anfragen beschleunigen. Die Filter unterstützen die gängigen
Anfragen an einen Index (equal, less/greater then, member of) und können
durch logische Operatoren (and, or, not) beliebig kombiniert werden.
Außerdem bietet Riak die Möglichkeit *Secondary Indexes* anzulegen und
diese per Map/Reduce abzufragen. Es stehen zwei Index-Typen zur Verfügung für
binäre Daten und Integer. Die indizierten Daten sind unabhängig vom eigentlich
Wert (Value) der gespeichert wird (schema free). Für ein Key-Value-Paar
können mehrere Indizes erstellt werden. Indizes werden adhoc mit der ersten
Anfrage erstellt, die einen neuen Index enthält.

## Architektur

Ein Riak Cluster besteht aus einer Menge von "physikalischen"
Hosts auf denen Riak-Knoten laufe. Jede Riak-Instanz verwaltet mehrere
virtuelle Knoten (*vnodes*). Riak teilt den 160-bit großen Key-Space in
gleich große Partitionen (*partitions*) auf. Die Keys setzen sich aus dem
Bucket des Key-Value-Paares und dem Key zusammen. Die Anzahl an Partitionen auf
dem Ring ist vom Benutzer konfigurierbar. Zur Zeit gibt es noch keine
Möglichkeit Knoten des Clusters zu gewichten, sodass sie mehr Partitionen
als andere Knoten übernehmen. Der Zustand des Rings wird über eine
Gossip-Protokoll unter den Knoten ausgetauscht. Jeder Host des Clusters kann
als Koordinator für Clientanfragen fungieren und Anfragen an den Zuständigen
Host im Cluster weiterleiten.

Replikation erfolgt in Riak entlang des Rings. Die Anzahl an Replikaten ist auf
Ebene der Buckets konfigurierbar. Bei der Replikation spielen drei Werte
eine Rolle, durch die sich die Konsistenz des Systems mit beinflussen lässst.
Der N-Value definiert wie viele Instanzen eines Values sich im
System befinden sollen. Der W-Value definiert wie viele Knoten für ein
erfolgreiches Write des Values geantwortet haben müssen, sodass der
Koordinator den "Commit" an den Client weitergeben kann. Analog dazu
funktioniert der R-Value. Durch verändern der Werte lässt sich auch ein
streng konsistentes System erreichen.

Riak verfügt über zahlreiche Backends (Storage-Engines), die ausgetauscht bzw.
pro Bucket konfiguriert werden können. Die Backends zielen auf
unterschiedliche Usecases ab. Die drei wichtigesten Backends sind: Bitcask,
LevelDB und in-memory. Das Bitcask Backend hält alle Keys im Memory und schreibt
Daten erst ins Memory und dann gesammelt auf die Festplatte. Das LevelDB Backend
ist ein persistentes Backend bestehend aus einem Key-Value-Store. Das
in-memory Backend speichert Daten nur im RAM und ermöglicht es Daten eine
Time-To-Live mit zugeben.


# Scalaris

Scalaris ist ein verteilter in Erlang geschriebener Key-Value-Store. Er bietet
*ACID*-Eigenschaften und basiert auf einer *Distributed HashTable*. Die
Entwicklung begann im *Zuse Institut Berlin* mit EU-Fördermitteln. Allerdings
existiert inzwischen auch die Firma *onScale solutions GmbH*, die eine
kommerzielle Version anbieten.
Treiber existieren momentan für Erlang, Java, Python und Ruby.

Scalaris bietet nur die drei Standardoperationen eines Key-Value-Stores:
* insert
* lookup
* delete

Wobei zu beachten ist, dass die delete Funktion bisher nur in Erlang und Java
zur Verfügung steht. Die Entwickler haben die Funktion auf mehrfachen Wunsch der
Community eingeführt, obwohl es zu Inkonsistenzen kommen kann, wenn ein Datum
gelöscht und neu gespeichert wird, während ein Knoten offline ist.
Aufgrund der Versionsnummer wird der alte Wert als neuer angenommen und
zurückgegeben.

## Replikationen

Das P2P Layer ist für die Verteilung der Daten und Replikate verantwortlich.
*Chord#* ist die Grundlage des Systems. Es ist ein *verteiltes Wörterbuch*, bei
dem jedem Knoten ein zufälliger Schlüssel zugeordnet wird. Der Schlüssel kann
hierbei aus einem beliebigen Set bestehen, welches geordnet werden kann. Im
Normalfall werden Strings genutzt.
Jeder Knoten ist für die Replikate zwischen dem eigenen Schlüssel und dem
Schlüssel des Nachfolgers verantwortlich.
Knoten besitzen sogenannte *Finger* auf andere Knoten im Ring, wodurch die Suche
beschleunigt werden kann, indem, anstatt die Anfrage einfach an den
Nachfolgeknoten weiter zu gegeben, einige Knoten übersprungen werden können.

Zur Replikation wird *Symmetric Replication* genutzt, was bedeutet, dass die
Replikate nicht in den nachfolgenden Knoten liegen, sondern in regelmäßigen
Intervallen auf dem Ring. Die Anzahl der Replikate kann konfiguriert werden.

## Transaktionen

Die ACID-Eigenschaften von Scalaris werden mit Hilfe des *Paxos-Protokolls*
erreicht. Hierbei gibt es einen *Transaction Manager* und mehrere *Replicate Transaction Manager*, die im Falle eines Ausfalls des Transaction Managers seine Rolle übernehmen können.
Der Transaction Manager verschickt eine Update-Nachricht an die Knoten, die die
Replikate halten. Die Knoten blockieren die nötigen Daten und melden zurück ob
sie schreiben können, oder nicht. Melden sich mindestens 50% der Knoten zurück
und können schreiben, löst der Transaction Manager die Transaktion aus, sonst
bricht er die Operation ab.

## Konsistenz

Jedes Key-Value-Paar bestitzt eine Versionsnummer, die bei einem Update, welches
mittels insert aufgerufen wird, erhöht wird. Um einen erfolgreichen Lesezugriff
ausführen zu können müssen 50% der Knoten antworten. Das Paar mit der höchsten
Versionsnummer wird zurückgegeben. Da immer über 50% der Knoten den neusten
Zustand eines Paares haben müssen wird immer die aktuellste Version
zurückgegeben. Hierbei ist allerdings auf das schon angesprochene Problem beim
Löschen zu achten.
Die Daten sind nicht persistent. Zwar können die Daten auch auf die Festplatte
geschrieben werden zum Beispiel mit *Tokio Cabinet*, allerdings werden die
Updates erst im Arbeitsspeicher gehalten, bevor sie persistiert werden.
So können updates verloren gehen.
Dies bedeuted, dass immer mindestens 50% der Server erreichbar sein müssen, da
es sonst zu einem möglichen Datenverlust kommt.

# Summary
