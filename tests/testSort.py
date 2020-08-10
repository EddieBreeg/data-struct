from structLib import Struct
from datetime import datetime


def parseDate(string):
    content = [int(x) for x in string.split('-')]
    return datetime(year=content[2], month=content[1], day=content[0])


data = Struct({
    "10-08-2020": 1,
    "7-08-2020": 2,
    "1-07-2020": 3
})


def testSort():
    data.sort(function=parseDate)
    assert [x[1] for x in data] == [3, 2, 1]
