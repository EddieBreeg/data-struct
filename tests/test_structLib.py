from structLib import Struct

data = Struct(
    {
        "element1": {
            "id": 0,
            "key": "blabla"
        },
        "element2": {
            "id": 47,
            "key": "foo"
        },
        "element3": {
            "id": 4,
            "key": "Hello world"
        }
    }
)


def test_get_item():
    assert data['element1', "id"] == 0


def test_set_item():
    data["bruh"] = {"id": 69}
    assert data['bruh'] == {"id": 69}


def test_del_item():
    del data['bruh']
    assert ('bruh' not in data)


def test_replace():
    data.replace('blabla', 'blabla2')
    assert data.isValueIn('blabla')


def test_replace2():
    assert data.replace('blabla', 'blabla2')["element1", "key"] == "blabla2"


def test_getAll():
    assert data.getAll("id") == [0, 47, 4]


def test_sort():
    data.sort(path="id")
    assert data.getAll("id") == [0, 4, 47]


def test_len():
    assert len(data) == 3


def test_iter():
    for x in data:
        assert data[x[0]] == x[1]


data2 = Struct(
    [
        {'id': 1},
        {'id': 2},
        {'id': "0"}
    ]
)


def test_sort2():
    assert [x['id'] for x in data2.sorted('id', int)] == ['0', 1, 2]
