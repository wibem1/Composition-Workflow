# Prüfergebnis · 19.10.2026

Kandidaten: gemeinsamer Workflow-Kern 1.0.0, Composition Studio 1.1.0, AI Notation Studio 0.11.0, Maestro-Quellintegration auf Windows-Basis 2.5.1.

21 Prüfprogramme bestanden. Vollständige Ergebnisse und Ausgaben stehen in `results.json` und den Logdateien.

- Derselbe eingebettete Kern: 49 Prüfungen, 12 Zustandswechsel und fünf Textbeispiele in Python, Lua 5.4 und Qt-JavaScript.
- REAPER: Syntax und erster UI-Aufruf, gespeicherte Vorschläge, Quellkonflikt, einmaliges Anwenden, Laden und Überarbeitung, Modellkataloge mit Seitennavigation, Controller-/Tempoübertragung. 31 Import-/Updater-Prüfungen einschließlich vollständiger Rücknahme bei mehrdeutiger Übergangszuordnung. Anbieterparameter und Kostenrechnung: 32 Kostenprüfungen plus 28 Anbieter-/Denkstufen-Kombinationen.
- MuseScore: sechs Kompositionsmodi in je drei Arbeitsweisen, Originalnoten vor/nach dem erlaubten Bereich, Übergangstaktzahl, Ablehnung überspannender Linien, MusicXML-4.0-Schema, Analyseverlauf, fehlerhafte Rohantwort, Modellwahl, Quellkonflikte. Tatsächliche QML-Oberfläche und Starter mit Qt 5.15.19 und Qt 6.12.0 geladen und bedient. Hot-Update/Neustart mit Qt 5 geprüft.
- Maestro: alle 120 vorhandenen Engine-Tests und der DOM-Selbsttest bestanden. Der Kernel-Generator ist wiederholbar; ein erneuter Lauf verändert die erzeugten Dateien nicht.

Ausgelassen mangels passender Laufzeit: echter Windows-PowerShell-Diagnoseexport, Windows-QML-Exportprozess und reale LilyPond-Kompilierung. Deren unveränderte Aufruf-/Fehlerbehandlung wird teilweise durch Testobjekte geprüft.

Zusatzbefund außerhalb der 21 bestandenen Prüfprogramme: Der separate Hot-Update-Neustarttest unter Qt 6.12/Linux meldet beim Laden einer nachträglich geschriebenen QML-Datei „File name case mismatch“. Unter Qt 5 besteht derselbe Test. Der Starter und die manuell installierte aktuelle App funktionieren im Qt-6-Test. Deshalb werden diese Kandidaten als manuelle Installationspakete und nicht als Online-Update ausgeliefert. Kein Nachweis eines entsprechenden Fehlers im echten MuseScore auf Windows oder Mac.

Nicht ausgeführt: echte Provider-Anfragen, bezahlte Kompositionen, tatsächliche REAPER-/MuseScore-/Maestro-Sitzungen und musikalische Hörtests. Automatische Tests belegen technische Abläufe, nicht musikalische Qualität oder die konkrete Wiedergabe eines VST-Instruments.
