import sublime, sublime_plugin

class SqlListifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(edit, 
                                         region,
                                         self.listify(self.view.substr(region)))

    def listify(self, input):
        gap = "','"
        stops = {
            "start": "('",
            "end": "')"
        }
        split_str = input.split("\n")
        output = stops['start'] + gap.join(split_str) + stops['end']
        return  output
