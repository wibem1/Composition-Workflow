# Maestro-Quellintegration des gemeinsamen Kerns

Entwicklungsreferenz auf Basis der bestätigten Windows-Engine 2.5.1. `workflow_core.py` wird aus `Engine/workflow-core` erzeugt. `workflows.py` verwendet gemeinsame Auftrag-, Zustands- und Anwendungsregeln sowie die musikalischen Grundanweisungen. Die nativen Lua-Schreiber, Rhythmus-/Ausdrucksprüfung, Originalbindung, Vorprüfung und Undo-Semantik bleiben erhalten.

Alle 120 vorhandenen Engine-Tests und der DOM-Selbsttest wurden geprüft. Ein Test, der nach einer erfolgreichen Anwendung absichtlich wieder eine frische Anwendung simuliert, setzt jetzt auch den neuen Vorschlagszustand zurück.

Dieser Ordner ist kein installierbares Desktop-Update. Die bestehende Maestro-App und die gesondert weiterentwickelte Mac-Version wurden nicht ersetzt. Die Quellintegration kann bei der nächsten regulären Maestro-Veröffentlichung übernommen werden.
