# print Erweiterung für [Sublime Text](https://www.sublimetext.com)

## Voraussetzungen

print ist als Erweiterung für die **neusten Build** von Sublime Text gedacht und erfordert im Moment **`Build 4065`** oder neuer.

* Lade [Sublime Text](https://www.sublimetext.com) herunter
  * (stable channel)
  * (dev channel)

## Installation

Die Verwendung von **Package Control** wird nicht zwingend vorausgesetzt, aber durchaus empfohlen, da es deine Erweiterungen (mit ihren Abhängigkeiten) aktuell hält.

### Installation über Package Control

* [Installiere Package Control](https://packagecontrol.io/installation)
  * Schließe und öffne Sublime Text nach der Installation von Package Control.
* Öffne die Befehlseingabe (`Tools > Command Palette`).
* Wähle `Package Control: Install Package`.
* Suche nach [`print` in Package Control](https://packagecontrol.io/packages/print) und wähle die Erweiterung aus, um sie zu installieren.

## Verwendung

print generiert eine Vorschau für das Drucken von Sublime Text Code.

* Markdown kann in einer Vorschau als
  [mini-HTML](https://www.sublimetext.com/docs/3/minihtml.html)
  geöffnet
* Code wird als Vorschau in deinen Standardbrowser kopiert

Du findest die Einträge `Print: Preview ...` in:

* der Befehlszeile (command palette)
* oder das Kontextmenü (rechts-Click)

### Bekannte Probleme mit der Markdown Vorschau

* the Markdown Preview is limited to mini-HTML
  * HTML comments break the preview (at that point)
* mdpopups uses PythonMarkdown which uses 4 spaces indentation

## Quellcode

[github.com/jrappen/sublime-print](https://www.github.com/jrappen/sublime-print)

### Lizenz

Siehe [`LICENSE`](https://github.com/jrappen/sublime-print/blob/master/LICENSE).

### Feedback

Verwende für Feedback bitte die Befehlseingabe (command palette) oder das Menü.

## Spenden

[paypal.me/jrappen](https://www.paypal.me/jrappen)
