from structLib import *
from datetime import datetime

def stringToDate(string):
    data=[int(x) for x in string.split('-')]
    return datetime(year=data[2], month=data[1], day=data[0])


with open('reports.json') as f:
    data=Struct.load(f)

data.sort(path=[0, "date"], function=stringToDate)
print(data)




