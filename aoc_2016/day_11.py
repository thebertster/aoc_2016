class PuzzleState:
    def __init__(self,state,parent):
        if parent is None:
            self.Distance = 0
        else:
            self.Distance = parent.Distance + self.GetDistanceVector()
        self.State = state
        self.ToRoot = parent
        self.Iterated = False
        
        stateDict[GetDictHash(self.State)] = self
        
        #ShowState(state)
        #print(len(stateDict))
        #input("")

    def GetDistanceVector(self):
        return 1

    def VisitAllStates(self):
        # Iterate through all states reachable from the current state

        floor = (self.State) % floors

        for g1 in range(0, elements+1):
            for g2 in range(0, elements+1):
                if g1>0:
                    m1 = g1+elements
                else:
                    m1 = g1
                if g2>0:
                    m2 = g2+elements
                else:
                    m2 = g2

                # Loop through all possible single/pairs of object to move, but only consider combinations of objects which are on the current floor!

                if (g2>g1):
                    #Moving elevator and generator(s) only
                    if IsOnFloor(self.State, g1, g2):
                        if floor > 0:
                            newState = self.State - 1
                            if g1>0: newState -= (floors ** g1)
                            newState -= (floors ** g2)
                            self.VisitState(newState)
                        if floor < floors -1:
                            newState = self.State + 1
                            if g1>0: newState += (floors ** g1)
                            newState += (floors ** g2)
                            self.VisitState(newState)

                    #Moving elevator and microchip(s) only
                    if IsOnFloor(self.State, m1, m2):
                        if floor > 0:
                            newState = self.State - 1
                            if m1>0: newState -= (floors ** m1)
                            newState -= (floors ** m2)
                            self.VisitState(newState)
                        if floor < floors - 1:
                            newState = self.State + 1
                            if m1>0: newState += (floors ** m1)
                            newState += (floors ** m2)
                            self.VisitState(newState)

                #Moving elevator, a generator and a microchip
                if (g1>0 and m2>0):
                    if IsOnFloor(self.State, g1, m2):
                        if floor > 0 :
                            newState = self.State - 1
                            newState -= (floors ** g1)
                            newState -= (floors ** m2)
                            self.VisitState(newState)
                        if floor < floors -1 :
                            newState = self.State + 1
                            newState += (floors ** g1)
                            newState += (floors ** m2)
                            self.VisitState(newState)
            
        self.Iterated = True

    def VisitState(self,newState):
        # First of all, is the proposed state actually a valid one (i.e. doesn't result in a microchip frying?)

        if IsStateValid(newState):
            newDictHash = GetDictHash(newState)
            if newDictHash in stateDict:
                # Already visited this state, but check whether we have found a shorter path to it
                existingState = stateDict[newDictHash]
                newDistance = self.Distance + self.GetDistanceVector()
                if existingState.Distance > newDistance:
                    existingState.Distance = newDistance
                    existingState.ToRoot = self
            else:
                # New state - add as unvisited state in dictionary
                newPuzzleState = PuzzleState(newState,self)

def IsOnFloor(state, n1, n2):
    # Check whether the items n1, n2 are on the same floor as the elevator (ignore any n1/n2 = 0)

    if (n1 == 0 and n2 == 0): return False
    
    floor = state % floors
    if n1 == 0:
        n1Floor = floor
    else:
        n1Floor = int(state / floors ** n1) % floors
    if n2 == 0:
        n2Floor = floor
    else:
        n2Floor = int(state / floors ** n2) % floors
    return (n1Floor == floor and n2Floor == floor)
    

def IsStateValid(state):
    # Check whether the proposed state will fry any microchips, so check each microchip (m) in turn

    for m in range(1, elements+1):
        chipFloor = int(state / floors ** (m+elements)) % floors
        rtgFloor = int(state / floors ** m) % floors

        # Are chip m and generator m on different floors? If so, need to check whether there are any other generators on the same floor as chip m

        if chipFloor != rtgFloor:
            for g in range(1, elements+1):
                if m!=g:
                    rtgFloorCheck = int(state / floors ** g) % floors
                    if rtgFloorCheck == chipFloor:
                        # Oh dear, there is another generator on chip m's floor, so chip m will fry - state is not valid
                        return False

        # Otherwise, chip m is safe
        
    return True

def GetDictHash(state):
    if optimisedHash == False: return state
    hash = str(state % floors)
    for f in range(floors):
        lonelyM = 0
        lonelyG = 0
        pairedMG = 0
        for n in range(1, elements+1):
            chipFloor = int(state / floors ** (n+elements)) % floors
            rtgFloor = int(state / floors ** n) % floors
            if (chipFloor == f):
                if (rtgFloor == f):
                    pairedMG += 1
                else:
                    lonelyM += 1
            else:
                if (rtgFloor == f):
                    lonelyG += 1
        hash += ":" + str(lonelyM) + ":" + str(lonelyG) + ":" + str(pairedMG)

    return hash

def ShowState(state):
    # Prints a pretty view of the current state
    for floor in range(floors-1,-1,-1):
        print(floor+1,end=":")
        if state % floors == floor:
            print(" E ", end=" ")
        else:
            print("   ", end=" ")
        for e in range(1,elements+1):
            if int(state / floors ** e) % floors == floor:
                print("%sG" % elementNames[e-1], end=" ")
            else:
                print("   ", end=" ")
        for e in range(1,elements+1):
            if int(state / floors ** (e+elements)) % floors == floor:
                print("%sM" % elementNames[e-1], end=" ")
            else:
                print("   ", end=" ")
        print()
    print()


#elementNames = ["CO","PO","PR","RU","TH","EL","DI"]
elementNames = ["CO","PO","PR","RU","TH"]
#elementNames = ["A","B","C"]

optimisedHash = False

floors = 4
elements = len(elementNames)

# State is encoded in (elements * 2 + 1) digits in base <floors>

# ele = 0
# cog = 1
# pog = 2
# prg = 3
# rug = 4
# thg = 5
# elg = 6
# dig = 7
# com = 8 (6)
# pom = 9 (7)
# prm = 10 (8)
# rum = 11 (9)
# thm = 12 (10)
# elm = 13
# dig = 14

##startState = int('000011000000000',floors)
##finalState = int('333333333333333',floors)
startState = int('00032000320',floors)
finalState = int('03200032003',floors)
#startState = int('0320000',floors)
#finalState = int('1201233',floors)

ShowState(startState)

finalStateHash = GetDictHash(finalState)
print(finalStateHash)

stateDict = {}

curState = PuzzleState(startState,None)
print(GetDictHash(startState))

curState.VisitAllStates()

complete = False

# Exhaustively iterate through all valid states starting with startState until all valid states have been visited

while not(complete):
    complete = True

    keys = list(stateDict.keys())

    for key in keys:
        state = stateDict[key]
        if state.Iterated == False:
            state.VisitAllStates()
            complete = False

# Now we should have visited every possible state and identified the shortest path to reach each state, so did we visit the final state?

if finalStateHash in stateDict:
    state = stateDict[finalStateHash]

    # Print out the solution steps - have to walk backwards from the final state then display in reverse order

    solution = []

    while (not(state is None)):
        solution.insert(0,state)
        state = state.ToRoot

    for state in solution:
        ShowState(state.State)

    print("Got there in %d moves" % state.Distance)

else:
    print("Didn't get there! Oh dear!")

print()
print("Total number of states visited: %d" % (len(stateDict)))