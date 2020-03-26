[![License](https://img.shields.io/github/license/jrappen/sublime-print.svg?style=flat-square)](https://github.com/jrappen/sublime-print/blob/master/LICENSE)
[![Required ST Build](https://img.shields.io/badge/ST-Build%204065+-orange.svg?style=flat-square&logo=sublime-text)](https://www.sublimetext.com)
[![Downloads Package Control](https://img.shields.io/packagecontrol/dt/print.svg?style=flat-square)](https://packagecontrol.io/packages/print)
[![Latest tag](https://img.shields.io/github/tag/jrappen/sublime-print.svg?style=flat-square&logo=github)](https://github.com/jrappen/sublime-print/tags)
[![Donate via PayPal](https://img.shields.io/badge/paypal.me-jrappen-009cde.svg?style=flat-square&logo=paypal)](https://www.paypal.me/jrappen)
[![SublimeHQ Discord](https://img.shields.io/discord/280102180189634562?label=SublimeHQ%20Discord&logo=discord&style=flat-square)](https://discord.gg/D43Pecu)

# `print` plug-in for [Sublime Text](https://www.sublimetext.com)

> Print a preview of your Sublime Text code in your browser.

## Documentation

### English 🇺🇸🇬🇧🇨🇦🇦🇺🇳🇿

> Plugin documentation is available in English via the menu or command palette.

[`jrappen/sublime-print:docs/README.en.md@master`](https://github.com/jrappen/sublime-print/blob/master/docs/README.en.md)

### German (Deutsch) 🇩🇪🇦🇹🇨🇭

> Eine plug-in Dokumentation ist über das Menü oder die Kurzbefehleingabe (command palette) verfügbar.

[`jrappen/sublime-print:docs/README.de.md@master`](https://github.com/jrappen/sublime-print/blob/master/docs/README.de.md)

## Requirements

print targets and is tested against the **latest Build** of Sublime Text, currently requiring **`Build 4065`** or later.

* Download [Sublime Text](https://www.sublimetext.com)
    * (stable channel)
    * (dev channel)

## Installation

Using **Package Control** is not required, but recommended as it keeps your packages (with their dependencies) up-to-date!

### Installation via Package Control

* [Install Package Control](https://packagecontrol.io/installation)
    * Close and reopen Sublime Text after having installed Package Control.
* Open the Command Palette (`Tools > Command Palette`).
* Choose `Package Control: Install Package`.
* Search for [`print` on Package Control](https://packagecontrol.io/packages/print) and select to install.

## Usage

print generates a preview for printing your Sublime Text code.

* for Markdown as:
    * an HTML preview in your Browser
    * a [mini-HTML](https://www.sublimetext.com/docs/3/minihtml.html)
      preview within Sublime Text
* for Code in your default browser

Look for `Print: Preview ...` in:

* the command palette
* or the context menu (right-click)

### Usage: Preview Markdown in Sublime Text

![Screencast Markdown](./docs/md_side-by-side.gif)

### Usage: Preview code in browser for printing

![Screencast Code](./docs/code_in_browser.gif)

### Known issues with Markdown Preview

* the Markdown Preview is limited to
  [mini-HTML](https://www.sublimetext.com/docs/3/minihtml.html)
    * HTML comments break the preview (at that point)
* mdpopups uses PythonMarkdown which uses 4 spaces for indentation

## Source Code

[github.com/jrappen/sublime-print](https://www.github.com/jrappen/sublime-print)

### License

See [`LICENSE`](https://github.com/jrappen/sublime-print/blob/master/LICENSE).

### Issues

Please use the command palette or the main menu to report an issue.

## Donations

[paypal.me/jrappen](https://www.paypal.me/jrappen)
