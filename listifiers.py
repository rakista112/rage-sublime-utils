import sublime, sublime_plugin
from .listifier.listifier import Listifier

class JsonListifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        listifier = Listifier({
                'start' : '[',
                'end' : ']',
        })

        listifier.modify_regions(self.view, edit)

class SqlListifyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        listifier = Listifier({
                'start' : '(',
                'end' : ')',
        })
        
        listifier.modify_regions(self.view, edit)
