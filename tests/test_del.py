from structLib import Struct

data = Struct(
    {
        "bruh": {
            "id": "foo"
        }
    }
)
print(data['bruh', "id"])
del data['bruh', "id"]
print(data)