from structLib import Struct
from datetime import datetime


def parseDate(string):
    content = [int(x) for x in string.split('-')]
    return datetime(year=content[2], month=content[1], day=content[0])


data = Struct({
    "10-08-2020": {'id': 2},
    "7-08-2020": {'id': 1},
    "1-07-2020": {'id': 3}
})


def test1():
    data.sort(function=parseDate)
    assert data.getAll("id") == [3, 1, 2]


def test2():
    data.sort('id')
    assert data.getAll("id") == [1, 2, 3]


# now if it's a list
data2 = Struct([1, 8, 3])


def test3():
    # Note that using Struct for a simple list like this is pointless
    assert [x for x in data2.sorted()] == [1, 3, 8]


data3 = Struct(
    [
        {"date": "10-08-2020"},
        {"date": "7-08-2020"},
        {"date": "1-07-2020"}
    ]
)


def test4():
    data3.sort("date", parseDate)
    assert [x["date"] for x in data3] == ["1-07-2020", "7-08-2020", "10-08-2020"]


