class Node:
    def __init__(self,x,y,toRoot):
        if (toRoot is None):
            self.d = 0
        else:
            self.d = toRoot.d + 1
        self.x = x
        self.y = y
        self.toRoot = toRoot
        self.nodeHash = ('%d:%d' % (x,y))
        unvisitedNodes[self.nodeHash] = self

    def Visit(self):
        unvisitedNodes.pop(self.nodeHash)
        visitedNodes[self.nodeHash] = self
        if self.x > 0:
            if IsUnvisitedSpace(self.x-1, self.y):
                newNode = Node(self.x-1, self.y, self)
        if self.y > 0:
            if IsUnvisitedSpace(self.x, self.y-1):
                newNode = Node(self.x, self.y-1, self)
        if IsUnvisitedSpace(self.x+1, self.y):
                newNode = Node(self.x+1, self.y, self)
        if IsUnvisitedSpace(self.x, self.y+1):
                newNode = Node(self.x, self.y+1, self)

def IsUnvisitedSpace(x,y):
    if IsSpace(x,y):
        nodeHash = '%d:%d' % (x,y)
        return (not(nodeHash in visitedNodes))
    else:
        return False

def IsSpace(x,y):
    q = x*x + 3*x + 2*x*y + y + y*y + magicNumber
    p = 0
    while q!=0:
        p = p ^ (q & 1)
        q = q>>1

    return (p == 0)


magicNumber = 1350

visitedNodes = { }
unvisitedNodes = { }

startNode = Node(1,1,None)
endNodeName = '31:39'

finished = False

for steps in range(51):

    keys = list(unvisitedNodes.keys())
    
    for key in keys:
        node = unvisitedNodes[key]
        node.Visit()

print("Number of steps = %d" % len(visitedNodes))
		