# Composition Workflow

Gemeinsamer Workflow-Kern für drei Kompositionswerkzeuge:

- **Composition Studio (REAPER)** — Lua
- **AI Notation Studio (MuseScore)** — QML / JavaScript
- **Maestro Composition Lab** — Python

## Stand 19.10.2026

Referenzpaket: Composition-Workflow 1.0.0. Zugehörige Testfassungen: REAPER 1.1.0 und MuseScore 0.11.0. Maestro-Referenz auf Basis der Windows-Engine 2.5.1; die unabhängig entwickelte macOS-App bleibt unverändert.

Die verbindliche Spezifikation regelt Arbeitsmodi, Zustandswechsel, Originalschutz, Übergangstakte und musikalische Grundanweisungen. Die Host-Anbindungen bleiben getrennt und erhalten ihre jeweiligen Notenformate.

**Wichtig:** Automatisierte Kernprüfungen ersetzen keine echten Reaper-, MuseScore- und Maestro-Tests und keine musikalischen Hörtests.

## Noch ausstehend

Die vollständige Übernahme der vorhandenen Quellcode-Sammlung (Engine, Reaper, MuseScore, Maestro und Tests) wird vorbereitet. Dieses Repository enthält noch nicht den gesamten Quellbestand. Keine installierbare Version aus diesem Stand ableiten.

## Sicherheitsregeln

Keine API-Schlüssel, Benutzerprofile, persönlichen Diagnosen, generierten Laufzeitumgebungen oder Maschinenartefakte einchecken.

Ursprung: vom Projekteigentümer bereitgestelltes Archiv `Composition-Workflow-1.0.0-Quellcode`.