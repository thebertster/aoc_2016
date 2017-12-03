a = "11100010111110100"
#a = "10000"

diskLen = 35651584
#diskLen = 20

while (len(a)<diskLen):
    b = ""
    for i in range(len(a)-1,-1,-1):
        if a[i] == "1":
            b += "0"
        else:
            b+= "1"
    a = a + "0" + b

data = a[:diskLen]

checksum = data

while (len(checksum) % 2 == 0):
    newChecksum = ""
    for i in range(0, len(checksum), 2):
        if checksum[i] == checksum[i+1]:
            newChecksum += "1"
        else:
            newChecksum += "0"
    checksum = newChecksum

print(str(checksum))