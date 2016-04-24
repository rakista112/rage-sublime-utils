import sublime, sublime_plugin
from .listifier.listifier import Listifier

class JsonListifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        listifier = Listifier({
                'start' : '[',
                'end' : ']',
        })

        for region in self.view.sel():
            if not region.empty():
                self.view.replace(edit, 
                                         region,
                                         listifier.listify(self.view.substr(region)))

class SqlListifyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        listifier = Listifier({
                'start' : '(',
                'end' : ')',
        })
        
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(edit, 
                                         region,
                                         listifier.listify(self.view.substr(region)))                                        