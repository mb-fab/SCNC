#!/usr/bin/python

TYPE_DRILL = 1
TYPE_MILL = 2

class Tool:
    def __init__(self, type):
        self.type = type

    def getDiameter(self):
        return self.diameter

    def setDiameter(self, d):
        self.diameter = d
