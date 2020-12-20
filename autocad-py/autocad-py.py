#from pyautocad import Autocad
#from pyautocad.types import APoint
#acad=Autocad()
#ms=acad.doc.ModelSpace
#utility=acad.doc.Utility
#ps=acad.doc.PaperSpace




def addlwpolyline(VerticesList):       
    return object.AddLightWeightPolyline(VerticesList)
def area(object):
    return object.Area
def length(object):
    return object.Length
def closed(object):
    return object.Closed
def setconstantwidth(object):
    object.ConstantWidth
def coordinate(object,index)
    return object.Coordinate(index)
def coordinates(object)
    return object.Coordinates
