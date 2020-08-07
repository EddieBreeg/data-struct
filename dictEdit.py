def modifyDict(dict, path):
    if len(path)==2:
        dict[path[0]]=path[1]
        if path[1]==None:
            del dict[path[0]]
        print(dict)
        return dict
    dict.setdefault(path[0], {})
    dict[path[0]]=modifyDict(dict[path[0]], path[1:])
    if dict[path[0]]=={}:
        del dict[path[0]]
    return dict


