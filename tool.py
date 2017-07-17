#!/usr/bin/python

TYPE_DRILL = 1
TYPE_MILL = 2

class Tool:
    def __init__(self, type):
        self.type = type

    def exportSCAD(self, x, y, depth):
        if self.type == TYPE_DRILL:
            scad = '\t// drilling\n'
            scad += '\ttranslate(['+str(x)+', '+str(y)+', -1*'+str(depth)+'])\n'
            scad += '\tcylinder(h='+str(depth)+'+0.01, d='+str(self.getDiameter())+');\n'
            return scad

    def getDiameter(self):
        return self.diameter

    def setDiameter(self, d):
        self.diameter = d
