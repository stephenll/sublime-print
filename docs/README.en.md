# `print` plug-in for [Sublime Text](https://www.sublimetext.com)

> Print a preview of your Sublime Text code in your browser.

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

* Markdown can be opened in a
  [mini-HTML](https://www.sublimetext.com/docs/3/minihtml.html)
  preview within Sublime Text
* Code is previewed in your default browser for printing

Look for `Print: Preview ...` in:

* the command palette
* or the context menu (right-click)

### Known issues with Markdown Preview

* the Markdown Preview is limited to mini-HTML
  * HTML comments break the preview (at that point)
* mdpopups uses PythonMarkdown which uses 4 spaces indentation

## Source Code

[github.com/jrappen/sublime-print](https://www.github.com/jrappen/sublime-print)

### License

See [`LICENSE`](https://github.com/jrappen/sublime-print/blob/master/LICENSE).

### Issues

Please use the command palette or the main menu to report an issue.

## Donations

[paypal.me/jrappen](https://www.paypal.me/jrappen)
