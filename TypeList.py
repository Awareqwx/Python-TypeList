def typeList(arr):
    ty = type(arr[0])
    string = None
    add = None
    listlist = None
    for i in arr:
        if type(i) != ty and ty != -1:
            ty = -1
        if type(i) == int:
            if add == None:
                add = 0
            add += i
        if type(i) == str:
            if string == None:
                string = ""
            string += " "
            string += i
        if type(i) == list:
            if listlist == None:
                listlist = []
            listlist.append(i)
    if ty != -1:
        if ty == int:
            print "The list contains only whole numbers"
        elif ty == float:
            print "The list contains only numbers with decimals"
        elif ty == str:
            print "The list contains words and such"
        elif ty == list:
            print "The list contains more lists"
        elif ty == complex:
            print "The list contains a bunch of imaginary friends"
        elif ty == set:
            print "The list contains a bunch of disorganized preschool lists"
        elif ty == frozenset:
            print "The list contains a bunch of refridgerated sets"
        elif ty == bytes:
            print "The list contanes a bunch of bite sized numbers"
        elif ty == bytearray:
            print "The list contains a bunch of arrays of bite sized numbers"
        elif ty == long:
            print "The list contains a bunch of really big whole numbers"
        elif ty == tuple:
            print "The list contains some angsty teenage lists"
        elif ty == dict:
            print "The list contains a high amount of definiton"
        elif ty == None:
            print "The list is completely empty"
        else:
            print "Nobody knows what it is this list contains"
    else:
        print "This list contains a bunch of different types of things"

    if add != None:
        print "Sum: " + str(add)
    if string != None:
        print "String: " + string
    if listlist != None:
        print "List of lists in the list: " + str(listlist)

typeList(['magical unicorns',19,'hello',98.98,'world'])
print
typeList([2,3,1,7,4,12])
print
typeList(['magical','unicorns'])