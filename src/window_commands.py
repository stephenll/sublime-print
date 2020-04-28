#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin

import os


PKG_NAME = __package__.split('.')[0]


class PrintOpenDocs(sublime_plugin.WindowCommand):

    def run(self, resource_path='docs/README.en.md'):
        try:
            w = self.window
            v = w.active_view()
            import mdpopups
            preview_sheet = mdpopups.new_html_sheet(
                window=w,
                name='{}/{}'.format(PKG_NAME, resource_path),
                # TODO: update for py3.8
                contents=sublime.load_resource('Packages/{}/{}'.format(PKG_NAME, resource_path)),
                md=True
            )
        except Exception as e:
            # TODO: update for py3.8
            print('print: Exception: {}'.format(e))

    # def is_enabled(self): return bool

    def is_visible(self):
        try:
            import mdpopups
            return True
        except Exception as e:
            return False

    # def description(self): return str
    # def input(self, args): return CommandInputHandler or None


class PrintPreviewCodeInBrowser(sublime_plugin.WindowCommand):

    def run(self):
        try:
            w = self.window
            v = w.active_view()
            import mdpopups
            l = mdpopups.get_language_from_view(v)
            md_preview = mdpopups.syntax_highlight(
                view=v,
                src=v.substr(sublime.Region(0, v.size())),
                language=l
            )
            p = os.path.join(sublime.packages_path(), 'User', 'Print Preview.cache', 'index.html')
            os.makedirs(p[:p.rindex(os.path.sep)], exist_ok=True)
            with open(p, mode='w', newline='\n') as f:
                f.write(md_preview)
            # TODO: remove pathlib from dependencies.json for py3.8
            import pathlib
            w.run_command('open_url', { 'url': pathlib.Path(p).as_uri() })
        except Exception as e:
            # TODO: update for py3.8
            print('Print: Exception: {}'.format(e))

    # def is_enabled(self): return bool

    def is_visible(self):
        try:
            import mdpopups
            return True
        except Exception as e:
            return False

    # def description(self): return str
    # def input(self, args): return CommandInputHandler or None


class PrintPreviewMarkdownInBrowser(sublime_plugin.WindowCommand):

    def run(self):
        try:
            w = self.window
            v = w.active_view()
            if not v.settings().get('syntax').startswith('Packages/Markdown/'):
                return
            import mdpopups
            md_preview = mdpopups.md2html(
                view=v,
                markup=v.substr(sublime.Region(0, v.size())),
                template_vars=None,
                template_env_options=None
            )
            p = os.path.join(sublime.packages_path(), 'User', 'Print Preview.cache', 'index.html')
            os.makedirs(p[:p.rindex(os.path.sep)], exist_ok=True)
            with open(p, mode='w', newline='\n') as f:
                f.write(md_preview)
            # TODO: remove pathlib from dependencies.json for py3.8
            import pathlib
            w.run_command('open_url', { 'url': pathlib.Path(p).as_uri() })
        except Exception as e:
            # TODO: update for py3.8
            print('Print: Exception: {}'.format(e))

    # def is_enabled(self): return bool

    def is_visible(self):
        try:
            VERSION = int(sublime.version())
            if VERSION < 4065:
                return False
            import mdpopups
            return self.window.active_view().settings().get('syntax').startswith('Packages/Markdown/')
        except Exception as e:
            return False

    # def description(self): return str
    # def input(self, args): return CommandInputHandler or None


class PrintPreviewMarkdownViaHtmlSheet(sublime_plugin.WindowCommand):

    def run(self):
        try:
            w = self.window
            v = w.active_view()
            if not v.settings().get('syntax').startswith('Packages/Markdown/'):
                return
            import mdpopups
            preview_sheet = mdpopups.new_html_sheet(
                window=w,
                name='[print] mini-HTML Preview (read-only)',
                contents=v.substr(sublime.Region(0, v.size())),
                md=True
            )
            # w.run_command('new_pane')
        except Exception as e:
            # TODO: update for py3.8
            print('Print: Exception: {}'.format(e))

    # def is_enabled(self): return bool

    def is_visible(self):
        try:
            VERSION = int(sublime.version())
            if VERSION < 4065:
                return False
            import mdpopups
            return self.window.active_view().settings().get('syntax').startswith('Packages/Markdown/')
        except Exception as e:
            return False

    # def description(self): return str
    # def input(self, args): return CommandInputHandler or None
