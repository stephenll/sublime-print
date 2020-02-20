#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin

import os
import pathlib
import webbrowser


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
            webbrowser.open(pathlib.Path(p).as_uri())
        except Exception as e:
            print('Print: Exception: {}'.format(e))

    # def is_enabled(self): return bool

    def is_visible(self):
        try:
            import mdpopups
            return not self.window.active_view().settings().get('syntax').startswith('Packages/Markdown/')
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
            md_preview = mdpopups.md2html(
                view=v,
                markup=v.substr(sublime.Region(0, v.size())),
                template_vars=None,
                template_env_options=None,
                nl2br=True,
                allow_code_wrap=False
            )
            preview_sheet = w.new_html_sheet(
                name='Print Preview (read-only)',
                contents=md_preview,
                cmd='open_url',
                args=None,
                flags=0,
                group=-1
            )
            w.run_command('new_pane')
        except Exception as e:
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
