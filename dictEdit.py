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

def pathTo(struct, value):
    if struct==value:
        return [value]

    if type(struct)==dict:
        sequence=struct.keys()
    else:
        sequence=range(len(struct))

    for k in sequence:
        if isValueIn((sub := struct[k]), value):
            return [k] + pathTo(sub, value)

