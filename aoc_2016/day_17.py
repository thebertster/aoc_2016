import hashlib

passcode = "qzthpkfp"
dirs = "UDLR"
offsets = [ [0,-1], [0,+1] , [-1,0], [+1,0] ]
opens = "bcdef"

nodeList = [ ( 0, 0, "" ) ]

foundFirst = False

while (nodeList):
    newNodeList = []
    for node in nodeList:
        if node[0] == 3 and node[1] == 3:
            print("\rFound vault after %d moves" % len(node[2]),end="")
            if not(foundFirst):
                print(" - %s" % node[2])
                foundFirst = True
        else:
            m = hashlib.md5()
            m.update(bytes(passcode+node[2],"ascii"))
            hash = m.hexdigest()

            for i in range(len(dirs)):
                if hash[i] in opens:
                    x = int(node[0]) + int(offsets[i][0])
                    y = int(node[1]) + int(offsets[i][1])
                    if 0 <= x <= 3 and 0 <= y <= 3:
                        newNodeList.append(( x, y, node[2]+dirs[i] ))

    nodeList = newNodeList

print()
print("Finished!")  