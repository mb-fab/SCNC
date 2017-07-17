#!/usr/bin/python

from tool import *
from step import *

#
# Class model holds all properties of a CNC project
# and provides methods to manipulate it
#

class Job:
    #
    # Initialize CNC model
    #
    def __init__(self, x, y, z):

        # empty set of toolpaths
        self.toolpath = []

        # base material size
        self.sizeX = x
        self.sizeY = y
        self.sizeZ = z

    #
    # Drill a hole at given position with given tool
    #
    def drill(self, x, y, depth, tool):
        step = Step(TYPE_DRILL)
        step.x = x
        step.y = y
        step.depth = depth
        step.tool = tool
        self.toolpath.append(step)

    #
    # Export model as SVG
    #
    def exportSVG(self, filename):
        f = open(filename, "w")
        f.write('<svg width="'+str(self.sizeX)+'" height="'+str(self.sizeY)+'">\n')
        for step in self.toolpath:
            f.write(step.exportSVG())
        f.write('</svg>\n')
        f.close()

    #
    # Export model
    #
    def export(self, filename):
        if filename[-4:] == ".svg":
            self.exportSVG(filename)
