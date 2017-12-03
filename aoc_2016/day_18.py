tiles = [ "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^." ]
#tiles = [ ".^^.^.^^^^" ]
rows = 400000

traps = [ "^^.", ".^^", "^..", "..^" ]

working = tiles[0]

safeTiles = working.count(".")

for i in range(rows-1):
    newRow = ""
    for j in range(len(working)):
        check = ("." if j == 0 else working[j-1]) + working[j] + ("." if j == len(working)-1 else working[j+1])
        if check in traps:
            newRow += "^"
        else:
            safeTiles += 1
            newRow += "."

    # tiles.append(newRow)
    working = newRow

print(safeTiles)