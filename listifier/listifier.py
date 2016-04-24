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
