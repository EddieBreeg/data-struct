def modifyStruct(struct, path):
    if len(path)==2:
        struct[path[0]]=path[1]
        if path[1]==None:
            del struct[path[0]]
        return struct
    struct.setdefault(path[0], {})
    struct[path[0]]= modifyStruct(struct[path[0]], path[1:])
    if struct[path[0]]=={}:
        del struct[path[0]]
    return struct

def isValueIn(struct, value):
    if struct==value:
        return True

    elif type(struct)==list:
        for x in struct:
            if isValueIn(x, value):
                return True
        return False
    elif type(struct)==dict:
        for k in struct:
            if isValueIn(struct[k], value):
                return True
    return False

def pathToValue(struct, value):
    if struct==value:
        return [value]

    if type(struct)==dict:
        sequence=struct.keys()
    else:
        sequence=range(len(struct))

    for k in sequence:
        if isValueIn((sub := struct[k]), value):
            return [k] + pathToValue(sub, value)

def isKeyIn(struct, key):
    sequence=[]
    if type(struct)==list:
        sequence=range(len(struct))
    elif type(struct)==dict:
        sequence=struct.keys()
    for k in sequence:
        if k==key:
            return True
        elif isKeyIn(struct[k], key):
            return True
    return False

def getAll(struct, key):
    sequence = []
    if type(struct) == list:
        sequence = range(len(struct))
    elif type(struct) == dict:
        sequence = struct.keys()
    values=[]
    for k in sequence:
        if k==key:
            values.append(struct[k])
        else:
            values+=getAll(struct[k], key)
    return values