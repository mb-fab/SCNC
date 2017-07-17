#!/usr/bin/python

#
# Class Step implements one step of a job
#

class Step:
    def __init__(self, type):
        self.type = type

    def exportSVG(self):
        style = 'style="fill:white; stroke:red; stroke-width:1; stroke-dasharray:1,1;"'
        return '<circle '+style+' cx="'+str(self.x)+'" cy="'+str(self.y)+'" r="'+str(self.tool.getDiameter())+'"/>\n'
