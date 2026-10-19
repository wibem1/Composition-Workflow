# GitHub-Import · 19.10.2026

Vollständige Übernahme des Referenzpakets Composition-Workflow 1.0.0: 194 identische Quelldateien aus den beiden GitHub-ZIPs sowie 24 ergänzende Validierungsdateien aus dem Quellcode-ZIP. Bestehende GitHub Actions, Ignore-Regeln und zusätzliche Kernprüfungen bleiben erhalten. README wurde an den abgeschlossenen Import angepasst.

## Aktuelle Prüfung

Alle 21 Prüfgruppen aus `validation/run_checks.py` mit Exitcode 0 ausgeführt (Qt im Offscreen-Modus). Zusätzlich sieben Python-Kernprüfungen und die Composition-Engine-Regression erfolgreich.

Umgebung: Python 3.12, Node.js 24, lupa, PySide6 6.12, PyQt5 5.15. Die ursprünglichen Prüfberichte unter `validation` wurden unverändert als Herkunftsnachweis erhalten.

Ausgelassen durch die vorhandenen Tests: echte LilyPond-Kompilierung ohne installierten Compiler, Windows-PowerShell-Diagnose und zugehörige Windows-Orchestrierung. Keine echten Host-Programmtests, bezahlten Provider-Aufrufe oder musikalischen Hörtests. Teststubs ersetzen keine laufende MuseScore-Installation.

## Einordnung

Gemeinsames Quellfundament, kein neuer installierbarer Release und kein Ersatz neuerer eigenständiger App-Versionen. Bestehende Updateverfahren der einzelnen Programme bleiben unberührt. Die Reaper-Oberfläche muss bei späterer Integration kompakt bleiben; zusätzliche Arbeitsaufträge sollen über das vorhandene Textfeld möglich sein.
