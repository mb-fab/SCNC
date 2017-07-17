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
        # open file for writing
        f = open(filename, "w")

        # write SVG preamble
        f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
        f.write('<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" ')
        f.write('width="'+str(self.sizeX)+'" height="'+str(self.sizeY)+'">\n')

        # export all toolpath steps to SVG
        for step in self.toolpath:
            f.write(step.exportSVG())

        # write SVG epilogue
        f.write('</svg>\n')
        f.close()

    #
    # Export model
    #
    def export(self, filename):
        if filename[-4:] == ".svg":
            self.exportSVG(filename)
