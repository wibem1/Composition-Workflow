# Composition Workflow

Gemeinsamer Workflow-Kern für drei Kompositionswerkzeuge:

- **Composition Studio (REAPER)** — Lua
- **AI Notation Studio (MuseScore)** — QML / JavaScript
- **Maestro Composition Lab** — Python

## Stand 19.10.2026

Referenzpaket: Composition-Workflow 1.0.0. Zugehörige Testfassungen: REAPER 1.1.0 und MuseScore 0.11.0. Maestro-Referenz auf Basis der Windows-Engine 2.5.1; die unabhängig entwickelte macOS-App bleibt unverändert.

Die verbindliche Spezifikation regelt Arbeitsmodi, Zustandswechsel, Originalschutz, Übergangstakte und musikalische Grundanweisungen. Die Host-Anbindungen bleiben getrennt und erhalten ihre jeweiligen Notenformate.

**Wichtig:** Automatisierte Kernprüfungen ersetzen keine echten Reaper-, MuseScore- und Maestro-Tests und keine musikalischen Hörtests.

## Vollständiger Quellimport · 19.10.2026

Die 194 Quelldateien aus `Composition-Workflow-1.0.0-GitHub-Quellen.zip` und die 24 ergänzenden Validierungsdateien aus `Composition-Workflow-1.0.0-Quellcode(1).zip` sind importiert. Das separate GitHub-Import-ZIP enthält dieselben 194 Quelldateien. Die bestehenden Kernprüfungen und GitHub Actions bleiben erhalten.

Dies ist ein gemeinsamer Referenzstand, kein Updatekanal für die einzelnen Programme. Neuere eigenständige Reaper-, MuseScore- und Maestro-Versionen werden durch diesen Import nicht ersetzt. Die kompakte Reaper-Oberfläche muss bei späterer Integration gesondert behandelt werden.

Die ursprünglichen Prüfberichte stehen unter `validation`; aktuelle Importprüfungen sind in `IMPORT-STATUS.md` dokumentiert. Native Programmtests und musikalische Hörtests bleiben erforderlich.

## Sicherheitsregeln

Keine API-Schlüssel, Benutzerprofile, persönlichen Diagnosen, generierten Laufzeitumgebungen oder Maschinenartefakte einchecken.

Ursprung: vom Projekteigentümer bereitgestelltes Archiv `Composition-Workflow-1.0.0-Quellcode`.REMOTE_CONTENT
