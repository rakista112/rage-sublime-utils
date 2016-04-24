class Listifier(object):
    """This class lets you configure how you wrap and split your strings"""
    def __init__(self, stops):
        self.stops = stops
        self.gap = '","'


    def listify(self, input):
        
        split_str = input.strip().split("\n")
        output = '{start}"{output}"{end}'.format(start = self.stops['start'],
                                                               output = self.gap.join(split_str),
                                                               end = self.stops['end'])
        return  output

    def modify_regions(self, view, edit):
        for region in view.sel():
            if not region.empty():
                view.replace(edit, 
                                   region,
                                   self.listify(view.substr(region)))
