from math import log

class Elf:
    def __init__(self, n):
        self.prev = None
        self.next = None
        self.n = n
    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev


elves = 3014387

elfList = list(map(Elf, range(1, elves+1)))
for i in range(elves):
    elfList[(i-1)%elves].next = elfList[(i+1)%elves].prev = elfList[i]

startElf = elfList[0]
midElf = elfList[elves//2]
for i in range(elves-1):
    midElf.delete()
    startElf=startElf.next
    midElf=midElf.next
    if ((elves-i) % 2) == 1:
        midElf=midElf.next

print(startElf.n)

n = int(log(elves, 3))
m = elves - 3**n
if m == 0:
    quickWay = elves
elif m <= 3**n:
    quickWay = m
else:
    quickWay = 2*m-3**n
print(quickWay)
