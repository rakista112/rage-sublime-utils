import sublime, sublime_plugin
import re

class UnlistifyCommand(sublime_plugin.TextCommand):
    """This command removes all the separators and tags 
        and puts them all in a newline separated list"""
    def run(self, edit):
       
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(edit, 
                                         region, 
                                         self.unlistify(
                                            self.view.substr(region)))

    def unlistify(self, input):
        # 1. get the first tag/stop then identify the appropriate end tag
        # 2. get all elements
        # 3. remove all quotes
        # 4. join with newlines

        element_pattern = re.compile('[\'"](\S*)[\'"]')
        without_tags = input[1:-1]
        elements = element_pattern.findall(without_tags)
        return "\n".join(elements)
