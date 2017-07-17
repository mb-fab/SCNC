#!/usr/bin/python

#
# Class Step implements one step of a job
#

class Step:
    def __init__(self, type):
        self.type = type

    def exportSVG(self):
        return '<circle x="'+str(self.x)+'" y="'+str(self.y)+'" r="'+str(self.tool.getDiameter())+'"/>\n'
