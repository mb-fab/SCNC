#!/usr/bin/python

from job import *
from tool import *

m = Job(300, 300, 5)

t1 = Tool(TYPE_DRILL)
t1.setDiameter(6)

m.drill(200, 200, 5, t1)

#m.export("demo.scad")
m.export("demo.svg")
#m.export("demo.dxf")
#m.export("demo.vcarve")
#m.export("demo.nc")
