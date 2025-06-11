def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list
print(extendList(4))