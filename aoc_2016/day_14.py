import hashlib

def GetStretchedHash(hash):
    for h in range(2017):
        m = hashlib.md5()
        m.update(bytes(hash,"ascii"))
        hash = m.hexdigest()
    return hash


salt = "zpqevtbw"

keys = []
keyIndex = []
hashList = [ "" ] * 1000

i = 0
n = 0

while (n<64):
    test = salt + str(i)
    hash = GetStretchedHash(test)

    if (i>=1000):
        checkHash = hashList[i % 1000]
        repDigit = ""
        for c in range(2, len(checkHash)):
            if (checkHash[c] == checkHash[c-1]) and (checkHash[c] == checkHash[c-2]):
                repDigit = checkHash[c]
                
                break

        hashList[i % 1000] = hash
        
        if (repDigit != ""):
            lookFor = repDigit * 5
            for checkHash in hashList:
                if checkHash.find(lookFor) >= 0:
                    keyIndex.append(i-1000)
                    keys.append(hash)
                    n += 1
                    print("Key %d (index %d) = %s" % (n, i-1000, hash))
                    break
    else:
        hashList[i] = hash

    i += 1

print(keyIndex[63])

for key in keys:
    print(key)
    