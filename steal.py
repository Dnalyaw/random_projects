
list1 = ['a','r','j','i','e']
list2 = ['k','a','r','i','g']
list3 = ['j','l','t','a','r']
list4 = ['i','m','a','r','w']

lists = [list1,list2,list3,list4]

def find_combo(lists):
    listpairs = []
    for list in lists:
        pairs = []
        for x in range(len(list)-1):
            pairs.append(f"{list[x]}{list[x+1]}")
        listpairs.append(pairs)
    return listpairs

def commonvalue(listpairs):
    values = []
    for LIST in range(len(listpairs)-1):
        for x in range(len(listpairs[LIST])):
            if listpairs[LIST][x] in values:
                continue
            elif listpairs[LIST][x] in listpairs[LIST+1] and LIST == 0:
                values.append(listpairs[LIST][x])
            elif listpairs[LIST][x] not in listpairs[LIST+1]:
                if listpairs[LIST][x] in values:
                    values.remove(listpairs[LIST][x])
    return values
print(commonvalue(find_combo(lists)))

