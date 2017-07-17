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
    # Export job as SVG
    #
    def exportSVG(self, filename):
        # SVG preamble
        svg = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
        svg += '<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" '
        svg += 'width="'+str(self.sizeX)+'" height="'+str(self.sizeY)+'">\n'

        # export all toolpath steps
        for step in self.toolpath:
            svg += step.exportSVG()

        # SVG epilogue
        svg += '</svg>\n'
        return svg

    #
    # Export job as OpenSCAD model
    #
    def exportSCAD(self, filename):
        # OpenSCAD preamble
        scad = '\n$fn=100;\n\ndifference()\n{\n'

        # base material
        scad += '\t// base material\n'
        scad += '\ttranslate([0, 0, -1*'+str(self.sizeZ)+'])\n'
        scad += '\tcube(['+str(self.sizeX)+', '+str(self.sizeY)+', '+str(self.sizeZ)+']);\n\n'

        # export all toolpath steps
        for step in self.toolpath:
            scad += step.exportSCAD()

        # OpenSCAD epilogue
        scad += '}\n'
        return scad

    #
    # Export job
    #
    def export(self, filename):
        # open file for writing
        f = open(filename, "w")
        content = ""

        # fill with export content
        if filename[-4:] == ".svg":
            content = self.exportSVG(filename)
        elif filename[-5:] == ".scad":
            content = self.exportSCAD(filename)

        # write export content and close file
        f.write(content)
        f.close()
